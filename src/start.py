# This program will open source codes and will save them in PDF files

# Import libraries
import pyconv

# Start application
if __name__ == "__main__":
    folder = '/home/murillo/anaconda3/git/ConvPDF/tests'
    destiny = '/home/murillo/anaconda3/git/ConvPDF/files'
    c = pyconv.ConvPdf(destiny)
    c.convert(folder)
    
