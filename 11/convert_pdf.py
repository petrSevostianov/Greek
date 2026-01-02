from pypdf import PdfReader
import sys

def pdf_to_markdown(pdf_path, output_path):
    """Convert PDF to Markdown format."""
    try:
        reader = PdfReader(pdf_path)
        
        # Extract text from all pages
        markdown_content = ""
        
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            if text.strip():
                markdown_content += text + "\n\n"
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Successfully converted PDF to Markdown: {output_path}")
        print(f"Total pages: {len(reader.pages)}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    pdf_path = r"d:\Greek\11\XP_Материалы урока 6_simple_Part_2-v1.pdf"
    output_path = r"d:\Greek\11\XP_Материалы урока 6_simple_Part_2-v1.md"
    
    pdf_to_markdown(pdf_path, output_path)
