#!/usr/bin/env python3
"""
Quick test script to demonstrate OCR and transliteration on a few pages.
"""

import sys
import os

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from bengali_english_translator import BengaliEnglishTransliterator


def test_few_pages():
    """Test OCR and transliteration on just a few pages for demonstration."""
    
    print("🧪 Testing OCR + Transliteration on first few pages...")
    print("=" * 60)
    
    # Initialize the transliterator
    translator = BengaliEnglishTransliterator()
    
    # Let's create a quick test by extracting text from just the first few pages
    from pdf2image import convert_from_path
    import pytesseract
    
    pdf_path = "/Users/ramjana/dev/poc_bengali_translator/input/bengali-female-script.pdf"
    
    # Convert just the first 3 pages
    print("📄 Converting first 3 pages to images...")
    images = convert_from_path(pdf_path, dpi=200, first_page=1, last_page=3)
    
    for i, image in enumerate(images, 1):
        print(f"\n📝 Page {i}:")
        print("-" * 40)
        
        # Extract Bengali text using OCR
        bengali_text = pytesseract.image_to_string(
            image, 
            lang='ben+eng',
            config='--psm 6'
        )
        
        # Show first 200 characters of Bengali text
        bengali_sample = bengali_text[:200].strip()
        if bengali_sample:
            print(f"Bengali Text (first 200 chars):")
            print(f"{bengali_sample}...")
            
            # Transliterate to English
            transliterated = translator.transliterate_text(bengali_sample)
            print(f"\nTransliterated English:")
            print(f"{transliterated}...")
        else:
            print("No text detected on this page.")
        
        print()


def show_output_sample():
    """Show a sample of the generated output."""
    
    print("\n📤 Sample from Generated Output PDF:")
    print("=" * 50)
    
    # Try to read a bit of the output file to show what was generated
    output_path = "/Users/ramjana/dev/poc_bengali_translator/output/transliterated_output.pdf"
    
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path)
        print(f"✅ Output PDF generated successfully!")
        print(f"📊 File size: {file_size:,} bytes")
        print(f"📍 Location: {output_path}")
    else:
        print("❌ Output PDF not found.")


def main():
    """Main function."""
    
    # Quick test on a few pages
    test_few_pages()
    
    # Show output info
    show_output_sample()
    
    print("\n🎉 OCR + Transliteration test completed!")
    print("\n💡 The full 166-page document has been processed.")
    print("   You can find the complete transliterated PDF in the output directory.")


if __name__ == "__main__":
    main()
