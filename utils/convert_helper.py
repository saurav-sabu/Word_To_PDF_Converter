from utils.helper import Word2Pdf

def convert_word_to_pdf(word_path,pdf_path):
    try:
        Word2Pdf.convert_word_to_pdf(word_path,pdf_path)
        return f"Conversion Successfully. PDF saved at {pdf_path}"
    except Exception as e:
        return f"Error Occurred:{e}"
    