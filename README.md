# Word To PDF Converter

## Table of Contents

- Introduction
- Features
- Modules Used
- Usage
- Support

## Introduction

The Word to PDF Converter is a versatile and user-friendly tool that simplifies the process of converting Microsoft Word documents (both .doc and .docx formats) into high-quality PDF files. This project was developed to provide a seamless and efficient solution for individuals and organizations seeking to convert their documents while maintaining formatting and document integrity.

## Features

- Converts Word documents to PDF with high fidelity.
- Supports both .doc and .docx formats.
- Preserves formatting, fonts, images, and layout.
- User-friendly web interface for easy conversion.

## Modules Used

- **Frontend and Backend**:
  - Python: The entire website is built using Python.
  - Gradio: Employs Gradio to create a seamless and interactive user interface while simultaneously handling backend logic.
  - docx2pdf: Utilizes docx2pdf for converting Word documents to PDF format.

- **Version Control**:
  - Git: Git is used for version control and collaboration among developers.

## Usage

The Word to PDF Converter allows you to easily convert Microsoft Word documents to PDF format on your local system. Follow these steps to use the converter:

### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your computer:

- **Python**: You need Python installed. If you don't have Python, download it from python.org.

- **Virtual Environment (Optional)**: It's recommended to create a virtual environment to isolate the project dependencies. To create a virtual environment, run:
```virtualenv venv```

Activate the virtual environment:

- On Windows:
```venv\Scripts\activate```

- On macOS and Linux:
```source venv/bin/activate```

- **Install Dependencies**: Install the required Python packages by running:
```pip install -r requirements.txt```

### Running the Converter

1. Open a terminal and navigate to the directory where the converter script is located.

2. Run the converter script by executing the following command:
```python gradio_app.py```

3. A website will be opened.

4. Click the "Upload Word Document" button to select the Word document you want to convert.

5. Wait for the conversion process to complete.

6. It will be downloaded in your local system.

## Screenshots

<img src="https://github.com/saurav-sabu/Word_To_PDF_Converter/blob/main/starter.PNG" alt="UI" title="UI DESIGN">

<img src="https://github.com/saurav-sabu/Word_To_PDF_Converter/blob/main/usage.PNG" alt="USAGE" title="USAGE">

## Support

If you have any questions, encounter issues, or need assistance, you can contact at saurav.sabu9@gmail.com. I am here to help you with any inquiries or problems you may have.

Thank you for using the Word to PDF Converter Website. We hope simplifies your document conversion tasks and enhances your workflow.
