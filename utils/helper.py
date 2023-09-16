from docx2pdf import convert


class Word2Pdf:

    def convert_word_to_pdf(word_path,pdf_path):
        try:
            convert(word_path,pdf_path)
            print(f"Conversion Successfully. PDF saved at {pdf_path}")
        except Exception as e:
            print(f"An error occured:{e}")

