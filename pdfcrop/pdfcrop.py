import tempfile
import os
import subprocess
import argparse
import shutil

# Check if pdfcrop is in PATH during import
if not shutil.which("pdfcrop"):
    raise FileNotFoundError("pdfcrop command not found. Make sure pdfcrop is installed.")


def pdfcrop(pdf_path, replace=False):
    """
    Crop a PDF file using the pdfcrop command-line tool.
    
    Args:
        pdf_path (str): Path to the PDF file to crop
        replace (bool): If True, replace the original file. If False, create a backup
            of the original file with .bak extension.
    
    Returns:
        None
    
    Raises:
        subprocess.CalledProcessError: If pdfcrop command fails
        FileNotFoundError: If the input PDF file doesn't exist
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_pdf = os.path.join(temp_dir, "temp.pdf")
        subprocess.run(["pdfcrop", pdf_path, temp_pdf], check=True)
        if replace is False:
            os.rename(pdf_path, pdf_path + ".bak")
        os.rename(temp_pdf, pdf_path)

def main():
    """Command-line entry point for pdfcrop."""
    parser = argparse.ArgumentParser(description="Crop PDF files using pdfcrop")
    parser.add_argument("pdf_path", help="Path to the PDF file to crop")
    parser.add_argument("--replace", "-r", action="store_true",
                      help="Replace the original file without creating a backup")
    
    args = parser.parse_args()
    try:
        pdfcrop(args.pdf_path, replace=args.replace)
        print(f"Successfully cropped {args.pdf_path}")
    except subprocess.CalledProcessError:
        print("Error: pdfcrop command failed. Make sure pdfcrop is installed.")
        exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()