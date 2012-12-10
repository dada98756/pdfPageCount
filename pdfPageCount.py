from pyPdf import PdfFileReader
import sys

def main():
	filename = sys.argv[1]
#	if (filename[-4:] != ".pdf"):
#		return "Error: Not a valid PDF file."
	try:
		fp = file(filename, 'rb')
		pdf_f = PdfFileReader(fp)
	except IOError as e:
		return "Error: Unable to process file "+filename
	except e:
		return "Error: Unable to read PDF File"
	return pdf_f.getNumPages()

if __name__ == "__main__":
    print main()