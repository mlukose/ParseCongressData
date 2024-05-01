import subprocess
import os

def convert_pdf_xml(pdf_input, xml_output):
    subprocess.run(['pdftohtml.exe', "-xml", "-i", "-hidden", "-enc", "UTF-8", pdf_input, xml_output])

""" def convert_xml_txt(xml_input, txt_output):
    # To do, convert the go source code to an exe and run the subprocess using that.
    subprocess.run(['go', 'run', 'C:\\Users\\lukos\\Desktop\\Congress Research\\parseOldCongressionalRecord-main\\main.go', xml_input, txt_output], shell=True)
 """
def main():
    # Paths to input and output directories/folders
    pdf_directory = 'pdf_files_test'
    xml_directory = 'xml_files'

    # Gets list of all files in directory
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    #To Add later: Check if an xml and txt directory exists, and if it does not then create one for both
    
    # Convert PDF to XML using pdftohtml program
    for pdf in pdf_files:
        # Construct input and output paths
        pdf_path = os.path.join(pdf_directory, pdf)
        xml_file = os.path.splitext(pdf)[0] + '.xml'
        xml_path = os.path.join(xml_directory, xml_file)

        # Convert PDF to XML
        convert_pdf_xml(pdf_path, xml_path)


if __name__ == "__main__":
    main()
