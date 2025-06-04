import streamlit as st
import pytesseract
from PIL import Image

try:
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image')
        text = pytesseract.image_to_string(image)
        st.text_area("Extracted Text", text)
except pytesseract.TesseractNotFoundError:
    st.error("Tesseract OCR engine is not found. Please ensure it's installed correctly.")

#set the path location for the pytesseract executable file 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#file uploader in the streamlit UI
file_upload = st.file_uploader("Upload a image file")

#return  streamlit file upload status
st.success("Image is uploaded successfully", icon='✅')

#image file uploaded to PILLOW
image = Image.open(file_upload)

#Convert to grayscale image
file = image.convert('L')

#open upload image
st.write(file)

#extract text from the file upload
extracted_text = pytesseract.image_to_string(file)

#Display output text
st.write("Extracted text:\n\n",extracted_text)
