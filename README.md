# OCR Project Documentation

## Overview

This project implements an Optical Character Recognition (OCR) system using Python. It allows users to upload image files (PNG, JPG) or PDF documents and extract text from them. Currently, the system supports English language only.

## Contents

The project consists of three main files:

1. `README.md`: Project description and setup instructions
2. `app.py`: Main application script
3. `requirements.txt`: List of required Python packages

## Setup

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   streamlit run app.py
   ```

## Application Details

### Inputs

- Image file (PNG, JPG) or PDF document

### Process

1. The application uses Streamlit to create a web-based user interface.
2. Users can upload an image file through the provided file uploader.
3. The uploaded image is processed using the PIL (Python Imaging Library) and converted to grayscale.
4. Pytesseract is used to perform OCR on the processed image.

### Outputs

- Extracted text from the uploaded image

## Code Structure

### `app.py`

- Sets up the Streamlit user interface
- Handles file upload
- Processes the uploaded image
- Performs OCR using Pytesseract
- Displays the extracted text

### `requirements.txt`

Lists the required Python packages:
- PILLOW
- Pytesseract
- streamlit

## Usage Notes

- Ensure that Tesseract OCR is installed on your system and the path is correctly set in the `app.py` file.
- The application is currently configured for Windows systems. Adjust the Tesseract path if using a different operating system.
- This version only supports English language OCR. Modifications would be needed for multi-language support.

## Limitations

- OCR accuracy may vary depending on the quality and clarity of the uploaded image.
- The system is designed for English text only.
- Large files or complex documents may take longer to process.
