# Example
# This program will open source codes and will save them in PDF files

# Import libraries
import pyconv
import sys

# Start application
if __name__ == "__main__":
    if len(sys.argv) == 3:
        folder = sys.argv[1]
        destiny = sys.argv[2]
        c = pyconv.ConvPdf(destiny)
        c.convert(folder,['cs'])

        # Show the checked folders and converted files
        print ("Checked Folders: ")
        print (c.checkedFolders)

        print ("Converted files: ")
        print (c.convertedFiles)

        print ("Unconverted files: ")
        print (c.unconvertedFiles)

        print ("Igonred files: ")
        print (c.ignoredFiles)
    else:
        print ("You need set the folder to convert source files in PDF files")
    
