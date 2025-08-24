#!/usr/bin/env python3
"""
Command-line interface for the Bengali to English Transliterator.

Usage:
    python cli_translator.py input.pdf output.pdf
    python cli_translator.py input.pdf  # Output will be input_transliterated.pdf
    python cli_translator.py  # Will use default files
"""

import sys
import os
import argparse
from pathlib import Path

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from bengali_english_translator import BengaliEnglishTransliterator


def main():
    """Main CLI function."""
    
    parser = argparse.ArgumentParser(
        description="Transliterate Bengali PDF to English while preserving pronunciation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli_translator.py input.pdf output.pdf
  python cli_translator.py bengali.pdf
  python cli_translator.py
  
The tool will:
1. Extract Bengali text from the input PDF
2. Transliterate it to English preserving Bengali pronunciation
3. Create a new PDF with the transliterated text
        """
    )
    
    parser.add_argument(
        'input_pdf',
        nargs='?',
        default='/Users/ramjana/dev/poc_translator/bengali-female-script.pdf',
        help='Path to the input Bengali PDF file (default: bengali-female-script.pdf)'
    )
    
    parser.add_argument(
        'output_pdf',
        nargs='?',
        help='Path to the output transliterated PDF file (default: input_transliterated.pdf)'
    )
    
    parser.add_argument(
        '--test',
        action='store_true',
        help='Run a quick test with sample Bengali text'
    )
    
    args = parser.parse_args()
    
    if args.test:
        run_quick_test()
        return
    
    # Set default output path if not provided
    if args.output_pdf is None:
        input_path = Path(args.input_pdf)
        output_dir = Path('/Users/ramjana/dev/poc_bengali_translator/output')
        output_dir.mkdir(exist_ok=True)
        args.output_pdf = output_dir / f"{input_path.stem}_transliterated.pdf"
    
    # Check if input file exists
    if not os.path.exists(args.input_pdf):
        print(f"❌ Error: Input file not found: {args.input_pdf}")
        print("Please provide a valid path to a Bengali PDF file.")
        return 1
    
    # Initialize the transliterator
    translator = BengaliEnglishTransliterator()
    
    try:
        print("🔄 Starting Bengali to English transliteration...")
        print(f"📥 Input: {args.input_pdf}")
        print(f"📤 Output: {args.output_pdf}")
        print()
        
        # Perform the translation
        translator.translate_pdf(args.input_pdf, str(args.output_pdf))
        
        print("\n✅ Translation completed successfully!")
        print(f"📄 Transliterated PDF saved at: {args.output_pdf}")
        
    except Exception as e:
        print(f"❌ Error during translation: {e}")
        return 1
    
    return 0


def run_quick_test():
    """Run a quick test with sample Bengali text."""
    
    print("🧪 Running quick transliteration test...")
    print("=" * 50)
    
    translator = BengaliEnglishTransliterator()
    
    test_cases = [
        "পথের পাঁচালী",
        "নিশ্চিন্দিপুর গ্রামের একেবারে উত্তরপ্রান্তে",
        "বাংলা ভাষা অত্যন্ত সুন্দর",
        "রবীন্দ্রনাথ ঠাকুর বিশ্বকবি"
    ]
    
    for i, bengali_text in enumerate(test_cases, 1):
        transliterated = translator.transliterate_text(bengali_text)
        print(f"{i}. {bengali_text}")
        print(f"   → {transliterated}")
        print()
    
    print("✅ Test completed!")


if __name__ == "__main__":
    sys.exit(main())
