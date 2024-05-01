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
    txt_directory = 'txt_files'

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

        #Create input and output paths for xml to txt
        #text_file = os.path.splitext(pdf)[0] + '.txt' #Use pdf here because we are just taing the name of the file not actually using the pdf. (If I used xml file it would end up with name.xml.txt which is not ideal )
        #text_path = os.path.join(txt_directory, text_file)

        #Convert the xml to txt
        #convert_xml_txt(xml_path, text_path)
    
    #xml_files = [x for x in os.listdir(xml_directory) if x.endswith('.pdf')]
    
    """ for xml in xml_files:
        xml_path = os.path.join(xml_directory, xml)
        txt_file = os.path.splitext(xml)[0] + '.txt'
        txt_path = os.path.join(txt_directory, txt_file)

        convert_xml_txt(xml_path, txt_path) """


if __name__ == "__main__":
    main()