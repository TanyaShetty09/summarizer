from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY

def generate_pdf(text: str, filename: str):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    
    # Use standard font (Helvetica) - no external files needed
    style = ParagraphStyle(
        name='Normal',
        fontName='Helvetica',
        fontSize=12,
        leading=14,
        alignment=TA_JUSTIFY,
    )
    
    elements.append(Paragraph(text, style))
    elements.append(Spacer(1, 12))
    
    doc.build(elements)