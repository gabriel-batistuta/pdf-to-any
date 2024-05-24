import pypdf2htmlEX

def to_html(pdf_filepath):
    pdf = pypdf2htmlEX.PDF(pdf_filepath)
    pdf.to_html(drm=True)