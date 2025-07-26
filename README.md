# PDFCrop

A Python wrapper for the pdfcrop command-line tool, useful for generating compact pdf figures through matplotlib. This package provides a simple interface to crop PDF files using the `pdfcrop` command-line utility.

## Prerequisites

- Python 3.6 or higher
- `pdfcrop` command-line tool (usually comes with TeX Live)

## Installation

```bash
pip install pdfcrop
```

## Usage

### As a Python module

```python
from pdfcrop import pdfcrop

# Crop a PDF file (creates a backup of the original)
pdfcrop("input.pdf")

# Crop a PDF file without creating a backup
pdfcrop("input.pdf", replace=True)
```

### From command line

```bash
pdfcrop-py input.pdf
```

## License

This project is licensed under the MIT License. 