# import modules
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

### HOW TO USE
# Copy and Paste the name of the file in between the '' below
# EXAMPLE
# name = 'fileName'
# DO NOT inculde the file tag such as .pdf

name = ''

# images [] stores images from pdf
images = convert_from_path(name + '.pdf')

# create list [] to store text
textList = []

for image in images:
    # grab text from images using Tesseract's OCR
    text = pytesseract.image_to_string(image)

    # add text to list []
    textList.append(text)

    print(text)


# Create and save text to a text file
with open(name + '.txt', 'w', encoding='utf-8') as file:
    for text in textList:
        file.write(text + '\n\n')  # Add extra newline for separation between pages