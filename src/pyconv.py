import os 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ConvPdf(object):

    # Constructor    
    def __init__(self, destiny):
        self.__convertedFiles = []
        self.__notConvertedFiles = []
        self.__checkedFolders = []
        self.__destiny = destiny
    
    # Methods
    def convert(self, folder=None, ignoreFiles=None):
        for f in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, f)):
                filename = "{}/{}".format(folder, f)
                self.createFile(filename)
            else:
                self.__checkedFolders.append("{}/{}".format(folder, f))
                self.convert("{}/{}".format(folder, f))

    def createFile(self, filename=None):
        try:
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
                self.__convertedFiles.append(filename)
        except:
            self.__notConvertedFiles.append(filename)

    # Properties
    def setDestiny(self, destiny):
        self.__destiny = destiny

    def getDestiny(self):
        return self.__destiny

    def setConvertedFiles(self, convertedFiles):
        self.__convertedFiles = convertedFiles

    def getConvertedFiles(self):
        return self.__convertedFiles

    def setCheckedFolders(self, checkedFolders):
        self.__checkedFolders = checkedFolders

    def getCheckedFolders(self):
        return self.__checkedFolders

    def setNotConvertedFiles(self, notConvertedFiles):
        self.__notConvertedFiles = notConvertedFiles

    def getNotConvertedFiles(self):
        return self.__notConvertedFiles

    destiny = property(getDestiny, setDestiny)
    convertedFiles = property(getConvertedFiles, setConvertedFiles)
    checkedFolders = property(getCheckedFolders, setCheckedFolders)
    notConvertedFiles = property(getNotConvertedFiles, setNotConvertedFiles)