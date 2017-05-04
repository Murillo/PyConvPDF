import os 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ConvPdf(object):
    
    def __init__(self):
        self.files = []
        self.folders = []
    
    def convert(self, folder=None, destiny=None):
        for f in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, f)):
                self.files.append("{}/{}".format(folder, f))
                print ('File: ' + f)
            else:
                self.folders.append("{}/{}".format(folder, f))
                print ("Call: " + f)
                self.convert("{}/{}".format(folder, f), destiny)

    def convertFile(self, file=None, destiny=None):
        # with open(folder, "r") as f:
        #     c = canvas.Canvas(destiny + name + ".pdf", pagesize=letter)
        #     c.drawString(30,750,"Program.cs")
        #     pos_x = 30
        #     pos_y = 720
        #     for line in f.readlines():
        #         new_line = line.replace('\n',' ').replace('\t', '    ').replace('\ufeff','')
        #         c.drawString(pos_x, pos_y, new_line)
        #         pos_y = pos_y - 15
        #     c.save()
        pass

    def structure(self):
        pass