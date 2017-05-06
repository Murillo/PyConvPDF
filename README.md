# PyConvPDF
This program will open source files and will save them in PDF files. Minimum version of python: 3.3.6
## Features:
* Set the folder and convert all file source in PDF files
* Show the structure (Coming soon)
## How to use the converter:
Below is code to instantiate the converter object and the main method to start the process.
```
import pyconv

folder = 'home/user/projectfolder'
destiny = 'home/user/filesconverted'
c = pyconv.ConvPdf(destiny)
c.convert(folder)
```
### View files converted:
```
print (c.convertedFiles)
```
### View checked folders:
```
print (c.checkedFolders)
```
## External libraries used:
### ReportLab open-source
```
pip install reportlab
```
