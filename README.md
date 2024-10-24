# PDF to Text Conversion Using Python

This project extracts text from PDF files using Optical Character Recognition (OCR) with Tesseract. The script converts PDF pages to images and then applies Tesseract to extract the text. The text is saved into a `.txt` file with a similar name as the original PDF.

## How to Use

1. **Install required dependencies**:
    Make sure you have the following Python packages installed:

    ```bash
    pip install pdf2image pillow pytesseract
    ```

2. **Tesseract Installation**:
    If you haven't installed Tesseract yet, you need to download and install it. 
    - For Windows, download the installer from the official [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).
    - Make sure to add Tesseract to your system's PATH.

3. **Prepare your PDF**:
    - Copy the PDF file you want to extract text from into the project directory.
    - Open the script and input the name of your PDF file (without the `.pdf` extension) into the `name` variable.

    ```python
    name = 'your_pdf_file_name'
    ```

4. **Run the script**:
    - Once the PDF name is set, run the script:

    ```bash
    python pdf_to_text.py
    ```

    The script will convert the PDF pages to images, extract the text from each page, and save the output to a `.txt` file.
