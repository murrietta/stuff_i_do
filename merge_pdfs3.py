import os
import PyPDF2 as pdf2
import re
import argparse

parser = argparse.ArgumentParser(description="Combine PDFs for OPPE")
parser.add_argument("--directory",type=str,default="",
					help="Directory containing PDFs to combine. Example: 'H:/mm/pdfDir/'")
args = parser.parse_args()

# Creating a routine that appends files to the output file
def append_pdf(bkmrk,input,output):
	bkmrk_pg = output.getNumPages()
	[output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]
	output.addBookmark(bkmrk,bkmrk_pg)

#if directory is specified then change to that directory
#otherwise current directory is used.
if args.directory != "":
	os.chdir(args.directory)

#create list of files in the folder
files = os.listdir(os.getcwd())

# Creating an object where pdf pages are appended to
output = pdf2.PdfFileWriter()

#start combined book with DEPARTMENT scorecard
regex = re.compile('2016 OPPE DEPARTMENT.')
deptInd = files.index([string for string in files if re.match(regex,string)][0])
append_pdf(files[deptInd].split(".pdf")[0],
		   pdf2.PdfFileReader(open(files[deptInd],"rb")),
		   output)

#remove the DEPARTMENT scorecard from the list
files.remove(files[deptInd])

#append the rest of the files
for filename in files:
    if filename.endswith(".pdf"): 
        append_pdf(filename.split(".pdf")[0],
				   pdf2.PdfFileReader(open(filename,"rb")),
				   output)

# Writing all the collected pages to a file
output.write(open("2016 OPPE ALL {0}.pdf".format(os.getcwd().split("\\")[-1]),"wb"))