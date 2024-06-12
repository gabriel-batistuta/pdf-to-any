from pdf2docx import parse

def to_docx(pdf_file):
    pdf_file = "JOUERN 605.pdf"
    word_file = "output.docx"
    parse(pdf_file, word_file, start=0, end=None)