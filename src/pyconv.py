import os 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ConvPdf(object):

    # Constructor    
    def __init__(self, destiny):
        self.__convertedFiles = []
        self.__ignoredFiles = []
        self.__notConvertedFiles = []
        self.__checkedFolders = []
        self.__destiny = destiny
    
    # Methods
    def convert(self, folder, ignoreFiles):
        """
        Converts all files that are in the specified folder in the first parameter
        """
        for f in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, f)):
                filename = "{}/{}".format(folder, f)
                if os.path.splitext(filename)[1][1:] not in ignoreFiles:
                    self.createFile(filename)
                else:
                    self.__ignoredFiles.append(filename)
            else:
                self.__checkedFolders.append("{}/{}".format(folder, f))
                self.convert("{}/{}".format(folder, f), ignoreFiles)

    def createFile(self, filename=None):
        """
        Converts to PDF only the file entered in the parameter
        """
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

    def setUnconvertedFiles(self, notConvertedFiles):
        self.__notConvertedFiles = notConvertedFiles

    def getUnconvertedFiles(self):
        return self.__notConvertedFiles

    def setIgnoredFiles(self, ignoredFiles):
        self.__ignoredFiles = ignoredFiles

    def getIgnoredFiles(self):
        return self.__ignoredFiles

    destiny = property(getDestiny, setDestiny)
    convertedFiles = property(getConvertedFiles, setConvertedFiles)
    checkedFolders = property(getCheckedFolders, setCheckedFolders)
    unconvertedFiles = property(getUnconvertedFiles, setUnconvertedFiles)
    ignoredFiles = property(getIgnoredFiles, setIgnoredFiles)