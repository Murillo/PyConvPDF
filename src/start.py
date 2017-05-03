# This program will open source codes and will save them in PDF files

# Import libraries
import os.path 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def createFiles(filename, destiny):
    path, name = os.path.split(filename)
    with open(filename, "r") as f:
        c = canvas.Canvas(destiny + name + ".pdf", pagesize=letter)
        c.drawString(30,750,"Program.cs")
        pos_x = 30
        pos_y = 720
        for line in f.readlines():
            new_line = line.replace('\n',' ').replace('\t', '    ').replace('\ufeff','')
            c.drawString(pos_x, pos_y, new_line)
            pos_y = pos_y - 15
        c.save()


if __name__ == "__main__":
    createFiles('tests/Program.cs', 'files/')
    
