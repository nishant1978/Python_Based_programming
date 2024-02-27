import PyPDF2
import sys
import os

inputs = sys.argv
print(os.getcwd)
def combine_Pdf(pdfList):
    merger = PyPDF2.PdfMerger()
    for pdf in pdfList:
        print(pdf)
        merger.append(pdf)
    #merger.write('super.pdf')

combine_Pdf(inputs) 