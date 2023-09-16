from utils.convert_helper import convert_word_to_pdf
import gradio as gr
import os 

def gradio_word2pdf(word_path):
    try:
        input_path = word_path.name
        output_path = f"C:\\Users\\{os.getlogin()}\\Downloads\\output.pdf"

        result_message = convert_word_to_pdf(input_path,output_path)
        return result_message
    
    except Exception as e:
        return f"An error occured:{e}"


interface = gr.Interface(fn=gradio_word2pdf,
                         inputs=gr.inputs.File(label="Input Word Document",type="file"),
                         outputs=gr.outputs.Textbox(label="Conversion Status"),
                         live=True,
                         title="Word To PDF Convertor",
                         description="Convert Word document to PDF files")

if __name__ == "__main__":
    interface.launch()

