from PIL import Image
import pytesseract
import os
import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def image_to_text(originalPath,output_path):
    file = Image.open(originalPath)
    str = pytesseract.image_to_string(file, lang='eng')
    outputFile=output_path+os.path.basename(originalPath)
    f=open(outputFile+".txt","w+")
    f.write(str)
    f.close()
    return outputFile+".txt"

def pdf_to_text(originalPath,output_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    outputFile=output_path+os.path.basename(originalPath)
    with open(originalPath, 'rb') as fh:
        for page in PDFPage.get_pages(fh,caching=True,check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()

    f=open(outputFile+".txt","w+")
    a=text.split()
    c=0;
    for i in a:
        f.write('%s '%i)
        c+=1
        if c==5:
            f.write("\n")
            c=0
    f.close()
        # close open handles
    converter.close()
    fake_file_handle.close()
    return outputFile+".txt"
