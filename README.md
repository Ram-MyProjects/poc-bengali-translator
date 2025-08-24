# Bengali to English Transliterator

[![CI/CD Pipeline](https://github.com/Ram-MyProjects/poc-bengali-translator/actions/workflows/ci.yml/badge.svg)](https://github.com/Ram-MyProjects/poc-bengali-translator/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A comprehensive Python tool for transliterating Bengali text to English while preserving Bengali pronunciation patterns. This tool can process PDF files containing Bengali text and generate transliterated output in PDF format.

## Features

- 🔤 **Accurate Transliteration**: Converts Bengali script to English while maintaining authentic Bengali pronunciation
- 📄 **PDF Processing**: Extracts text from Bengali PDFs and creates transliterated PDF output
- 🖼️ **OCR Support**: Handles image-based PDFs using Tesseract OCR with Bengali language support
- 🧠 **Smart Detection**: Automatically detects whether a PDF contains extractable text or images
- 🎯 **Special Cases**: Handles common Bengali words with proper transliteration exceptions
- 🔧 **Flexible Interface**: Command-line interface and Python API
- ✅ **Well Tested**: Comprehensive test suite with examples

## Examples

**Input Bengali Text:**
```
পথের পাঁচালী
নিশ্চিন্দিপুর গ্রামের একেবারে উত্তরপ্রান্তে
```

**Output Transliterated Text:**
```
Pother Pachali
Nishchindipur gramer ekebare uttarprante
```

## Installation

### Prerequisites

**System Requirements:**
- Python 3.8 or higher
- macOS, Linux, or Windows
- Homebrew (for macOS) or equivalent package manager

**System Dependencies:**
```bash
# On macOS
brew install tesseract tesseract-lang poppler

# On Ubuntu/Debian
sudo apt-get install tesseract-ocr tesseract-ocr-ben poppler-utils

# On Windows
# Install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
# Install poppler from: https://blog.alivate.com.au/poppler-windows/
```

### Project Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd poc_bengali_translator
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

**Basic usage with default files:**
```bash
python cli_translator.py
```

**Specify input and output files:**
```bash
python cli_translator.py input_bengali.pdf output_transliterated.pdf
```

**Specify only input file (output will be auto-generated):**
```bash
python cli_translator.py my_bengali_document.pdf
```

**Run quick test:**
```bash
python cli_translator.py --test
```

### Python API

```python
from src.bengali_english_translator import BengaliEnglishTransliterator

# Initialize the transliterator
translator = BengaliEnglishTransliterator()

# Transliterate a single word
result = translator.transliterate_word("পথের")
print(result)  # Output: pother

# Transliterate a sentence
result = translator.transliterate_text("পথের পাঁচালী")
print(result)  # Output: pother pachali

# Process a PDF file
translator.translate_pdf("input.pdf", "output.pdf")
```

## Project Structure

```
poc_bengali_translator/
├── src/
│   ├── bengali_english_translator.py  # Main transliterator class
│   └── main.py                        # Original main file
├── tests/
│   ├── test_bengali_translator.py     # Comprehensive tests
│   └── test_main.py                   # Original test file
├── output/                            # Generated output files
├── cli_translator.py                  # Command-line interface
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## Dependencies

- **PyPDF2**: For reading PDF files
- **reportlab**: For creating PDF files
- **indic-transliteration**: For advanced Indic script processing
- **python-bidi**: For bidirectional text support
- **pytesseract**: Python wrapper for Tesseract OCR
- **Pillow**: Python Imaging Library for image processing
- **pdf2image**: Convert PDF pages to images
- **Tesseract OCR**: OCR engine (system dependency - installed via Homebrew)

## How It Works

1. **Smart Detection**: First attempts regular text extraction from PDF
2. **OCR Fallback**: If PDF contains images, automatically switches to OCR
3. **Image Conversion**: Converts PDF pages to high-resolution images
4. **Text Extraction**: Uses Tesseract OCR with Bengali language support
5. **Character Mapping**: Maps Bengali characters to English equivalents preserving pronunciation
6. **Word Processing**: Handles special cases and common Bengali words
7. **Conjunct Processing**: Properly handles Bengali conjunct consonants (যুক্তাক্ষর)
8. **PDF Generation**: Creates formatted PDF output using ReportLab

## Transliteration Rules

The tool follows these key principles:

- **Vowels**: অ → o, আ → a, ই → i, ঈ → ee, etc.
- **Consonants**: ক → k, খ → kh, গ → g, ঘ → gh, etc.
- **Conjuncts**: যুক্তাক্ষর are properly separated
- **Special Words**: Common words have preferred transliterations

## Testing

**Run all tests:**
```bash
python -m unittest discover tests
```

**Run specific test:**
```bash
python tests/test_bengali_translator.py
```

**Quick functionality test:**
```bash
python cli_translator.py --test
```

## Example Files

The tool comes with example files in the `output/` directory:
- `sample_bengali_text.pdf`: Sample Bengali text for testing
- `transliterated_sample.pdf`: Transliterated output example

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

### Quick Start for Contributors

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/poc-bengali-translator.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes and add tests
5. Run tests: `python -m unittest discover tests`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:
- 🐛 [Report a bug](https://github.com/Ram-MyProjects/poc-bengali-translator/issues/new?template=bug_report.yml)
- 💡 [Request a feature](https://github.com/Ram-MyProjects/poc-bengali-translator/issues/new?template=feature_request.yml)
- 📖 Check the [documentation](README.md)
- 💬 Start a [discussion](https://github.com/Ram-MyProjects/poc-bengali-translator/discussions)

## Acknowledgments

- Tesseract OCR team for excellent Bengali OCR support
- Bengali language community for feedback and testing
- Open source contributors who make projects like this possible

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
