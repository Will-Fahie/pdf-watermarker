import PyPDF2
import os
import sys


# watermarks each pdf
def watermarker(pdf, watermark):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf, "rb"))
    watermark_reader = PyPDF2.PdfFileReader(open(watermark, "rb"))
    output = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page.mergePage(watermark_reader.getPage(0))
        output.addPage(page)

    with open("watermarked.pdf", "wb") as file:
        output.write(file)


# checks if a file path exists
def path_exists(path):
    if os.path.exists(path):
        return True
    else:
        print("PDF file path does not exist")
        return False


if __name__ == "__main__":

    # checks whether file paths are already given as arguments
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        watermark_path = sys.argv[2]
        watermarker(pdf_path, watermark_path)

    # if not, asks user for them
    else:
        # loops until a valid paths are received
        while True:
            pdf_path = input("Enter PDF file path: ")
            if path_exists(pdf_path):
                break

        while True:
            watermark_path = input("Enter watermark file path: ")
            if path_exists(watermark_path):
                break

        # when two valid paths are received, the watermarker is run
        watermarker(pdf_path, watermark_path)
