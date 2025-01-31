from docx import Document

def convert_docx_to_markdown(input_path, output_path):
    """
    Converts a Word document (.docx) to a Markdown (.md) file.
    
    :param input_path: Path to the input .docx file.
    :param output_path: Path to the output .md file.
    """
    try:
        doc = Document(input_path)
        markdown_content = "\n\n".join([para.text for para in doc.paragraphs])
        
        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)
        
        print(f"Markdown file saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
