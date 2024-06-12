from ast import Raise
from os import curdir
from os.path import basename, dirname, join, abspath
import pdfplumber
import platform
from pdfminer.pdfparser import PDFSyntaxError
import ghostscript

def _to_txt(file_path):

    def convert_pdf(input_path, output_path=None):
        if output_path is None:
            output_path = input_path
            args = [
                "-o", output_path,
                "-sDEVICE=pdfwrite",
                input_path
            ]
        ghostscript.Ghostscript(*args)

    txt = ''
    with open(file_path, 'rb') as fp:
        try:
            pdf = pdfplumber.open(fp)
        except PDFSyntaxError:
            # try:
            print('PDFSyntaxError, trying concert the pdf')
            convert_pdf(file_path)
            pdf = pdfplumber.open(fp)
            # except:
            #     raise Exception('unable to concert the pdf, aborting...')

    for page in pdf.pages:
        if not txt == '':
            txt += '\n'
        txt += page.extract_text()

    print(txt)
    return txt

def to_txt(file_path):
    return _to_txt(file_path)

def create_txt(file_path):
    if platform.system() == 'Windows':
        if "\\" not in file_path:
            file_path = file_path.replace('pdf', 'txt')
        else:
            file_path = join(dirname(file_path), basename(file_path).replace('pdf','txt'))
    
    else:
        if '/' not in file_path :
            file_path = file_path.replace('pdf', 'txt')
        file_path = join(dirname(file_path), basename(file_path).replace('pdf','txt'))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(_to_txt(file_path))

if __name__ == '__main__':
    print(abspath(curdir) + '/JOUERN 605.pdf')
    path = abspath(curdir) + "/"
    create_txt('JOUERN 605.pdf')