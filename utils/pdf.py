from fpdf import FPDF

def create_post_pdf(posts: list[str], filename: str = "nurox_post.pdf") -> str:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i, post in enumerate(posts, 1):
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(0, 10, f"Пост {i}", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, post)
        pdf.ln(5)

    path = f"/tmp/{filename}"
    pdf.output(path)
    return path
