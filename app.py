import streamlit as st
import pytesseract
from PIL import Image

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