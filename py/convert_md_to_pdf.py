from markdown import markdown
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.units import inch
import os

def md_to_pdf(md_file_path: str) -> None:
    """
    Reads a Markdown file, converts it to PDF, and saves it locally with a font size of 12.

    Parameters:
    - md_file_path (str): Path to the Markdown file.

    Returns:
    - None: The function saves a PDF file with the same name as the .md file.
    """
    # Read the Markdown file content
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown(md_content)
    
    # Create a PDF document with the same name as the .md file
    pdf_file_path = os.path.splitext(md_file_path)[0] + '.pdf'
    pdf = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    
    # Set up styles with font size 12
    styles = getSampleStyleSheet()
    normal_style = ParagraphStyle(
        'Normal',
        fontSize=12,
        leading=14,
        spaceAfter=0.5 * inch,
    )
    
    # Split HTML content into paragraphs and add page breaks for a multi-page PDF
    story = []
    paragraphs = html_content.splitlines()
    
    for paragraph in paragraphs:
        if paragraph.strip():  # Add paragraph if it's not empty
            story.append(Paragraph(paragraph, normal_style))
            story.append(PageBreak())  # Adding a page break after each paragraph
    
    # Build the PDF
    pdf.build(story)
    print(f"PDF saved as {pdf_file_path}")



print(os.listdir("../docs/midterm/"))

md_to_pdf("../docs/midterm/ta_review_session_2024_11_02_saturday.md")