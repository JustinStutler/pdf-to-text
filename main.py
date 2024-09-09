# import modules
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# images [] stores images from pdf
images = convert_from_path('text.pdf')

# create list [] to store text
textList = []

for image in images:
    # grab text from images using OCR
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # add text to list []
    textList.append(text)

    print(text)


# Create and save text to a text file
with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    for text in textList:
        file.write(text + '\n\n')  # Add extra newline for separation between pages