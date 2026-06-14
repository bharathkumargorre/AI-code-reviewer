from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(filename, analysis):

    pdf_name = f"{filename}_report.pdf"

    doc = SimpleDocTemplate(pdf_name)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Code Review Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Filename: {filename}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    data = [
        ["Bugs", analysis["bugs"]],
        ["Security", analysis["security"]],
        ["Performance", analysis["performance"]],
        ["Best Practices", analysis["best_practices"]],
        ["Quality Score", str(analysis["quality_score"])]
    ]

    table = Table(data)

    elements.append(table)

    doc.build(elements)

    return pdf_name