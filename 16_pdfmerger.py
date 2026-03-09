from PyPDF2 import PdfWriter
# PyPDF2 extention

merge = PdfWriter()

mergedpdf=[]
n=int(input("Enter number pdf to merge:"))
for i in range(1,n+1):
    name=input("Enter a pdf name:")
    mergedpdf.append(name)
    
for i in mergedpdf:
    merge.append(i)    
    
merge.write("merged_pdf.pdf")   
merge.close() 
