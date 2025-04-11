from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(data):
    filename = "reports/report_2025.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Exemple de tableau avec pandas
    df = pd.DataFrame(data)
    table_data = [df.columns.to_list()] + df.values.tolist()
    table = Table(table_data)
    elements.append(table)

    # Génération du PDF
    doc.build(elements)
    return filename