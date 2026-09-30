import pytesseract
from PIL import Image

# Point Tesseract to the binary (if not in PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

# Open an image
image = Image.open('WhatsApp Image 2026-02-28 at 15.08.41.jpeg')

# Extract text
text = pytesseract.image_to_string(image)
print(text)