#!/usr/bin/env python3
"""
Bengali to English Transliteration Tool with OCR Support

This module provides functionality to transliterate Bengali text to English
while preserving Bengali pronunciation. It can handle both text-based PDFs
and image-based PDFs using OCR (Optical Character Recognition).

Author: Bengali Translator Tool
Date: August 2025
"""

import os
import re
import sys
from typing import List, Dict, Optional
import PyPDF2
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# OCR imports
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import tempfile


class BengaliEnglishTransliterator:
    """
    A comprehensive Bengali to English transliteration tool that preserves
    Bengali pronunciation patterns.
    """
    
    def __init__(self):
        """Initialize the transliterator with Bengali-English mapping."""
        self.bengali_to_english_map = self._create_transliteration_map()
        self.word_exceptions = self._create_word_exceptions()
    
    def _create_transliteration_map(self) -> Dict[str, str]:
        """
        Create a comprehensive mapping of Bengali characters to English equivalents
        that preserve Bengali pronunciation.
        """
        return {
            # Vowels
            'অ': 'o',
            'আ': 'a',
            'ই': 'i',
            'ঈ': 'ee',
            'উ': 'u',
            'ঊ': 'oo',
            'ঋ': 'ri',
            'এ': 'e',
            'ঐ': 'oi',
            'ও': 'o',
            'ঔ': 'ou',
            
            # Vowel markers (kar)
            'া': 'a',
            'ি': 'i',
            'ী': 'ee',
            'ু': 'u',
            'ূ': 'oo',
            'ৃ': 'ri',
            'ে': 'e',
            'ৈ': 'oi',
            'ো': 'o',
            'ৌ': 'ou',
            
            # Consonants
            'ক': 'k',
            'খ': 'kh',
            'গ': 'g',
            'ঘ': 'gh',
            'ঙ': 'ng',
            'চ': 'ch',
            'ছ': 'chh',
            'জ': 'j',
            'ঝ': 'jh',
            'ঞ': 'ny',
            'ট': 't',
            'ঠ': 'th',
            'ড': 'd',
            'ঢ': 'dh',
            'ণ': 'n',
            'ত': 't',
            'থ': 'th',
            'দ': 'd',
            'ধ': 'dh',
            'ন': 'n',
            'প': 'p',
            'ফ': 'ph',
            'ব': 'b',
            'ভ': 'bh',
            'ম': 'm',
            'য': 'y',
            'র': 'r',
            'ল': 'l',
            'শ': 'sh',
            'ষ': 'sh',
            'স': 's',
            'হ': 'h',
            'ড়': 'r',
            'ঢ়': 'rh',
            'য়': 'y',
            'ৎ': 't',
            'ং': 'ng',
            'ঃ': 'h',
            '্': '',  # hasanta (virama)
            
            # Numbers
            '০': '0',
            '১': '1',
            '২': '2',
            '৩': '3',
            '৪': '4',
            '৫': '5',
            '৬': '6',
            '৭': '7',
            '৮': '8',
            '৯': '9',
            
            # Punctuation
            '।': '.',
            '॥': '..',
        }
    
    def _create_word_exceptions(self) -> Dict[str, str]:
        """
        Create a dictionary of common Bengali words with their preferred
        English transliterations to handle special cases.
        """
        return {
            'পথের': 'pother',
            'পাঁচালী': 'pachali',
            'নিশ্চিন্দিপুর': 'nishchindipur',
            'গ্রামের': 'gramer',
            'একেবারে': 'ekebare',
            'উত্তরপ্রান্তে': 'uttarprante',
            'বাংলা': 'bangla',
            'ভাষা': 'bhasha',
            'সাহিত্য': 'sahitya',
            'কবিতা': 'kobita',
            'গল্প': 'golpo',
            'উপন্যাস': 'uponnyas',
            'লেখক': 'lekhok',
            'কবি': 'kobi',
        }
    
    def transliterate_character(self, char: str) -> str:
        """
        Transliterate a single Bengali character to English.
        
        Args:
            char: Bengali character to transliterate
            
        Returns:
            English transliteration of the character
        """
        return self.bengali_to_english_map.get(char, char)
    
    def transliterate_word(self, word: str) -> str:
        """
        Transliterate a Bengali word to English, handling special cases.
        
        Args:
            word: Bengali word to transliterate
            
        Returns:
            English transliteration of the word
        """
        # Clean the word
        clean_word = word.strip()
        
        # Check for word exceptions first
        if clean_word in self.word_exceptions:
            return self.word_exceptions[clean_word]
        
        # Character-by-character transliteration
        result = ''
        i = 0
        while i < len(clean_word):
            char = clean_word[i]
            
            # Handle conjunct consonants (যুক্তাক্ষর)
            if i < len(clean_word) - 2 and clean_word[i + 1] == '্':
                # This is a conjunct consonant
                first_consonant = self.transliterate_character(char)
                second_consonant = self.transliterate_character(clean_word[i + 2])
                result += first_consonant + second_consonant
                i += 3
            else:
                result += self.transliterate_character(char)
                i += 1
        
        return result
    
    def transliterate_text(self, text: str) -> str:
        """
        Transliterate Bengali text to English.
        
        Args:
            text: Bengali text to transliterate
            
        Returns:
            English transliteration of the text
        """
        # Split text into words while preserving whitespace and punctuation
        words = re.findall(r'\S+|\s+', text)
        
        transliterated_words = []
        for word in words:
            if word.isspace():
                transliterated_words.append(word)
            else:
                transliterated_words.append(self.transliterate_word(word))
        
        return ''.join(transliterated_words)
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text from the PDF
            
        Raises:
            FileNotFoundError: If the PDF file doesn't exist
            Exception: If there's an error reading the PDF
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n"
                
                return text
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    
    def extract_text_from_pdf_with_ocr(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file using OCR for image-based PDFs.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text from the PDF using OCR
            
        Raises:
            FileNotFoundError: If the PDF file doesn't exist
            Exception: If there's an error reading the PDF or performing OCR
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        try:
            print("🔍 Converting PDF pages to images...")
            # Convert PDF to images
            images = convert_from_path(pdf_path, dpi=300)
            
            extracted_text = ""
            total_pages = len(images)
            
            print(f"📄 Processing {total_pages} pages with OCR...")
            
            for i, image in enumerate(images, 1):
                print(f"  Processing page {i}/{total_pages}...")
                
                # Perform OCR on the image with Bengali language
                # Use both Bengali and English for better accuracy
                page_text = pytesseract.image_to_string(
                    image, 
                    lang='ben+eng',  # Bengali + English
                    config='--psm 6'  # Assume a single uniform block of text
                )
                
                extracted_text += page_text + "\n\n"
            
            print("✅ OCR text extraction completed!")
            return extracted_text
            
        except Exception as e:
            raise Exception(f"Error performing OCR on PDF: {str(e)}")
    
    def smart_extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Smart text extraction that tries regular extraction first, 
        then falls back to OCR if no meaningful text is found.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text from the PDF
        """
        try:
            # First, try regular text extraction
            text = self.extract_text_from_pdf(pdf_path)
            
            # Check if meaningful text was extracted
            # If the text is very short or mostly empty, it's likely an image-based PDF
            clean_text = text.strip()
            if len(clean_text) > 50 and any(c.isalnum() for c in clean_text):
                print("📝 Regular text extraction successful!")
                return text
            else:
                print("📸 PDF appears to be image-based, switching to OCR...")
                return self.extract_text_from_pdf_with_ocr(pdf_path)
                
        except Exception as e:
            print(f"❌ Regular text extraction failed: {e}")
            print("📸 Trying OCR extraction...")
            return self.extract_text_from_pdf_with_ocr(pdf_path)
    
    def create_transliterated_pdf(self, text: str, output_path: str, 
                                title: str = "Bengali to English Transliteration") -> None:
        """
        Create a PDF with the transliterated text.
        
        Args:
            text: Transliterated text to include in the PDF
            output_path: Path where the output PDF should be saved
            title: Title for the PDF document
        """
        try:
            # Create the PDF document
            doc = SimpleDocTemplate(output_path, pagesize=A4,
                                  rightMargin=72, leftMargin=72,
                                  topMargin=72, bottomMargin=18)
            
            # Get styles
            styles = getSampleStyleSheet()
            
            # Create custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1  # Center alignment
            )
            
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=12,
                spaceAfter=12,
                alignment=0  # Left alignment
            )
            
            # Build the content
            story = []
            
            # Add title
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 12))
            
            # Add transliterated text
            paragraphs = text.split('\n')
            for para in paragraphs:
                if para.strip():
                    story.append(Paragraph(para.strip(), body_style))
                else:
                    story.append(Spacer(1, 12))
            
            # Build the PDF
            doc.build(story)
            
        except Exception as e:
            raise Exception(f"Error creating PDF: {str(e)}")
    
    def translate_pdf(self, input_pdf_path: str, output_pdf_path: str) -> None:
        """
        Complete workflow: Extract Bengali text from PDF, transliterate to English,
        and save as a new PDF.
        
        Args:
            input_pdf_path: Path to the input Bengali PDF
            output_pdf_path: Path where the transliterated PDF should be saved
        """
        try:
            print(f"Reading Bengali PDF from: {input_pdf_path}")
            bengali_text = self.smart_extract_text_from_pdf(input_pdf_path)
            
            print("Transliterating Bengali text to English...")
            transliterated_text = self.transliterate_text(bengali_text)
            
            print(f"Creating transliterated PDF at: {output_pdf_path}")
            self.create_transliterated_pdf(
                transliterated_text, 
                output_pdf_path,
                "Bengali to English Transliteration"
            )
            
            print("Translation completed successfully!")
            
        except Exception as e:
            print(f"Error during translation: {str(e)}")
            raise


def main():
    """
    Main function to run the Bengali to English transliterator.
    """
    # Initialize the transliterator
    translator = BengaliEnglishTransliterator()
    
    # Define input and output paths
    input_pdf = "/Users/ramjana/dev/poc_bengali_translator/input/bengali-female-script.pdf"
    output_pdf = "/Users/ramjana/dev/poc_bengali_translator/output/transliterated_output.pdf"
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    
    try:
        # Perform the translation
        translator.translate_pdf(input_pdf, output_pdf)
        
        print(f"\n✅ Translation completed!")
        print(f"📥 Input: {input_pdf}")
        print(f"📤 Output: {output_pdf}")
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        print("Please check if the input PDF file exists at the specified path.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
