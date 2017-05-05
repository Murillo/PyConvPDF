import os 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ConvPdf(object):

    # Constructor    
    def __init__(self, destiny):
        self.__files = []
        self.__folders = []
        self.__destiny = destiny
    
    # Methods
    def convert(self, folder=None):
        for f in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, f)):
                filename = "{}/{}".format(folder, f)
                self.__files.append(filename)
                self.createFile(filename)
            else:
                self.__folders.append("{}/{}".format(folder, f))
                self.convert("{}/{}".format(folder, f))

    def createFile(self, filename=None):
        path, name = os.path.split(filename)
        with open(filename, "r") as f:
            c = canvas.Canvas(self.__destiny + "/" + name + ".pdf", pagesize=letter)
            c.drawString(30,750,name)
            pos_x = 30
            pos_y = start_y = 720
            for line in f.readlines():
                if pos_y > 30:
                    new_line = line.replace('\n',' ').replace('\t', '    ').replace('\ufeff','')
                    c.drawString(pos_x, pos_y, new_line)
                    pos_y = pos_y - 15
                else:
                    pos_y = 720
                    c.showPage()                
            c.save()

    def structure(self):
        return self.__folders, self.__files

    # Properties
    def setDestiny(self, destiny):
        self.__destiny = destiny

    def getDestiny(self):
        return self.__destiny

    destiny = property(getDestiny, setDestiny)