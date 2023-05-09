import PyPDF2

pdffiles = ["Python-Cheat-Sheet.pdf","best_practices_for_python_coding_in_hands_on_lite.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    pdfFile = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')





