#!/usr/bin/env python3
"""
Test script for the Bengali to English Transliterator.

This script demonstrates the transliteration functionality with sample Bengali text.
"""

import sys
import os

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from bengali_english_translator import BengaliEnglishTransliterator


def test_transliteration():
    """Test the transliteration functionality with sample text."""
    
    # Initialize the transliterator
    translator = BengaliEnglishTransliterator()
    
    # Test cases
    test_cases = [
        "পথের পাঁচালী",
        "নিশ্চিন্দিপুর গ্রামের একেবারে উত্তরপ্রান্তে",
        "বাংলা ভাষা সুন্দর",
        "আমি বাংলায় গান গাই",
        "রবীন্দ্রনাথ ঠাকুর একজন মহান কবি",
        "বাংলাদেশ আমার প্রিয় দেশ"
    ]
    
    print("Bengali to English Transliteration Test")
    print("=" * 50)
    
    for i, bengali_text in enumerate(test_cases, 1):
        transliterated = translator.transliterate_text(bengali_text)
        print(f"{i}. Bengali: {bengali_text}")
        print(f"   English: {transliterated}")
        print()
    
    # Test individual word transliteration
    print("Individual Word Tests:")
    print("-" * 30)
    
    individual_words = ["পথের", "পাঁচালী", "গ্রামের", "বাংলা", "ভাষা"]
    
    for word in individual_words:
        transliterated = translator.transliterate_word(word)
        print(f"{word} → {transliterated}")
    
    print("\n✅ Transliteration test completed!")


def create_sample_text_pdf():
    """Create a sample PDF with Bengali text for testing."""
    
    # Sample Bengali text
    sample_text = """পথের পাঁচালী
    
নিশ্চিন্দিপুর গ্রামের একেবারে উত্তরপ্রান্তে রায়চৌধুরী পরিবারের বাড়ি। বাড়িটি পুরনো, তবে বেশ বড়। চারদিকে প্রাচীন আমগাছ, জামগাছ আর তালগাছের সারি।

এই বাড়িতে থাকেন সর্বজয়া আর তার পরিবার। সর্বজয়া একজন সহজ-সরল গ্রাম্য মহিলা। তার স্বামী হরিহর রায় একজন দরিদ্র ব্রাহ্মণ। তারা দুই সন্তানের বাবা-মা - দুর্গা আর অপু।

বাংলা সাহিত্যের এই অমর সৃষ্টি বিভূতিভূষণ বন্দ্যোপাধ্যায়ের কলমে জীবন্ত হয়ে উঠেছে।"""
    
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.pagesizes import A4
    
    output_path = "/Users/ramjana/dev/poc_bengali_translator/output/sample_bengali_text.pdf"
    
    # Create the PDF document
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom style for Bengali text
    bengali_style = ParagraphStyle(
        'BengaliText',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=12,
        alignment=0
    )
    
    # Build the content
    story = []
    
    # Add the Bengali text
    paragraphs = sample_text.split('\n')
    for para in paragraphs:
        if para.strip():
            story.append(Paragraph(para.strip(), bengali_style))
        else:
            story.append(Spacer(1, 12))
    
    # Build the PDF
    doc.build(story)
    
    print(f"✅ Sample Bengali PDF created at: {output_path}")
    return output_path


def main():
    """Main function to run the tests."""
    
    print("Bengali to English Transliterator - Test Suite")
    print("=" * 60)
    
    # Test transliteration functionality
    test_transliteration()
    
    # Create a sample PDF
    print("\nCreating sample Bengali PDF...")
    sample_pdf_path = create_sample_text_pdf()
    
    # Test the full PDF translation workflow
    print("\nTesting PDF translation workflow...")
    
    translator = BengaliEnglishTransliterator()
    output_pdf_path = "/Users/ramjana/dev/poc_bengali_translator/output/transliterated_sample.pdf"
    
    try:
        translator.translate_pdf(sample_pdf_path, output_pdf_path)
        print(f"✅ PDF translation completed!")
        print(f"📥 Input: {sample_pdf_path}")
        print(f"📤 Output: {output_pdf_path}")
    except Exception as e:
        print(f"❌ Error during PDF translation: {e}")


if __name__ == "__main__":
    main()
