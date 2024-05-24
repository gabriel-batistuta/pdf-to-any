import os

class TestPDF:
    def __init__(self) -> None:
        this_dir = os.getcwd()
        if 'main.py' in os.listdir(this_dir):
            if this_dir[-1] == '/':
                self.filepath = this_dir + 'lib/assets/Test.pdf'
            else:
                self.filepath = this_dir + '/lib/assets/Test.pdf'
        elif 'pdf.py' in os.listdir(this_dir):
            if this_dir[-1] == '/':
                self.filepath = this_dir + 'assets/Test.pdf'
            else:
                self.filepath = this_dir + '/assets/Test.pdf'
        else:
            raise FileNotFoundError(f'No pdf file found in {this_dir}.\n Please try execute in the root path or on the module folder')
        
    def __str__(self) -> str:
        return f'a pdf file for demo tests.'

if __name__ == '__main__':
    pdf = TestPDF()
    with open(pdf.filepath, 'rb') as file:
        print(pdf.filepath)
        print(pdf)