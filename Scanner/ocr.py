from PIL import Image
import pytesseract
import cv2

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # image=input('Define image name for ocr')
    # image='output'+'/'+image
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
image=input('Define image name for ocr')
image='./output'+'/'+image
print(ocr_core(image))