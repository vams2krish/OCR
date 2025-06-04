import streamlit as st
import pytesseract
from PIL import Image
import platform

# Set Tesseract path for Windows only
if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("OCR Image Text Extractor")

file_upload = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg"])

if file_upload is not None:
    st.success("Image is uploaded successfully", icon='✅')

    image = Image.open(file_upload)
    gray_image = image.convert('L')
    st.image(gray_image, caption='Grayscale Image')

    # Extract text
    extracted_text = pytesseract.image_to_string(gray_image)
    st.write("### Extracted Text")
    st.text(extracted_text)
else:
    st.info("Please upload an image to begin.")
