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
c.convert(folder, [])
```
It's possible set the extensions files that the converter will ignore in process. This is second parameter of convert method as array format.
```
c.convert(folder, ['xml','cs', 'java'])
```
### View files converted:
```
print (c.convertedFiles)
```
### View files not converted:
```
print (c.unconvertedFiles)
```
### View ignored files:
```
print (c.ignoredFiles)
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
