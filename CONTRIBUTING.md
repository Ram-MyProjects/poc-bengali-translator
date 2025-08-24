# Contributing to Bengali to English Transliterator

Thank you for your interest in contributing to this project! We welcome contributions from the community.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request, please create an issue on GitHub with:
- A clear description of the problem or feature
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your environment details (OS, Python version, etc.)

### Contributing Code

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/poc-bengali-translator.git
   cd poc-bengali-translator
   ```

3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Set up the development environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

5. **Make your changes** and add tests if applicable

6. **Run the tests** to ensure everything works:
   ```bash
   python -m unittest discover tests
   python cli_translator.py --test
   ```

7. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: Clear description of your changes"
   ```

8. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request** on GitHub

## Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Testing
- Add tests for new functionality
- Ensure existing tests pass
- Test with various Bengali text samples

### Documentation
- Update README.md if adding new features
- Add inline comments for complex logic
- Update docstrings for modified functions

## Areas for Contribution

We welcome contributions in these areas:

### Transliteration Improvements
- Better handling of complex Bengali characters
- Improved word exception mappings
- Support for more regional dialects

### OCR Enhancements
- Better image preprocessing
- Support for different PDF formats
- Improved accuracy for handwritten text

### Performance Optimization
- Faster OCR processing
- Memory usage optimization
- Batch processing capabilities

### User Interface
- Web interface
- Desktop GUI application
- API improvements

### Testing and Quality
- More comprehensive test cases
- Performance benchmarks
- Code quality improvements

## Getting Help

If you need help or have questions:
- Check existing issues on GitHub
- Create a new issue with the "question" label
- Review the documentation in README.md

## Code of Conduct

Please be respectful and constructive in all interactions. We aim to create a welcoming environment for all contributors.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🙏
