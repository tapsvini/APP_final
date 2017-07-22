from lxml import etree
import os
from yattag import Doc, indent


class FileUtility:
    """The class provides the basic functions to deal with file like creation of xml or text file, validating xml file
    finding weather file exist or not"""

    @staticmethod
    def validate_xml(filename):

        """Function to validate generated Xml with dtd.

        :param filename:filename(which should be xml) which is required to be validated
        :type filename:string
        :return: Print 'Validated' if it is wel formed and checked with schema, else 'Not Validated'
        :type: void
        """

        parser = etree.XMLParser(dtd_validation=True);
        tree = etree.parse(filename, parser);
        if tree:
            print("Validated");
        else:
            print("Not Validated");

    @staticmethod
    def generate_xml(radius, length):

        """Function to generate XML.

        :param radius: Radius which is taken as input from user
        :type radius:int
        :param length: which is output after doing calculation
        :type length: int
        :return: string formatted for xml document
        :type string
        """

        doc, tag, text = Doc().tagtext()

        with tag('TestResult'):
            with tag('Radius'):
                text(str(radius))
            with tag('Length'):
                text(str(length))

        result = indent(
            doc.getvalue(),
            indentation=' ' * 4,
            newline='\r\n'
        )

        return "\n"+result

    @staticmethod
    def file_exists(file_path):

        """Function will tell weather file already exists or not.

        :param file_path: full path of the file with name
        :type file_path:string
        :return: true if file exists, else false
        :type Boolean
        """

        return os.path.exists(file_path)

    @staticmethod
    def create_xml_file(filename, mode, text):

        """Function to write text into given xml file name.

        :param filename:Filename where results should be saved
        :type filename:string
        :param mode:valid values w,a. whether to create new file or append the result in previous file.
        :type mode:string
        :param text:text which needs to be write into the filename
        :type text:string
        :return: print success or unsuccess message depending on whether xml file is created or not.
        :type void
        """

        filepath = os.path.join('../../../../resources/result/XMLFile', filename + ".xml")
        file_exist=os.path.exists(filepath)

        xml_head_txt="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+"<!DOCTYPE TestResult SYSTEM \"sample.dtd\">\n"


        file = open(filepath, mode);

        if mode=="w":
            file.write(xml_head_txt+str(text));
            print ("File "+filename+".xml created successfully. Thanks for using our application!");
        else:
            if file_exist:
                file.write(str(text));
                print("File " + filename + ".xml appended successfully. Thanks for using our application!");
            else:
                file.write(xml_head_txt+str(text));
                print("File " + filename + ".xml created successfully. Thanks for using our application!");

        file.close();

    @staticmethod
    def formt_txt_result(radius, length):

        """Function to format the output of the program for writing into text file.

        :param radius: Radius of coaster
        :type radius:int
        :param length: length which is required to overlap two coaster with equal radii to get halp overlapping area.
        :type length:int
        :return: string which can be directly written into text file
        :type String
        """

        return "The Radius entered by you is = "+str(radius)+" \nThe length require for overlapping area to be half of " \
                                                             "one circle = "+str(length)+"\n\n"

    @staticmethod
    def crt_txt_file(filename, mode, text):

        """Function to write text into given file name.

        :param filename:Filename where results should be saved
        :type filename:string
        :param mode:valid values w,a. whether to create new file or append the result in previous file.
        :type mode:string
        :param text:text which needs to be write into the filename
        :type text:string
        :return: print success or unsuccess message.
        :type void
        """

        filepath = os.path.join('../resources/result/TestFile', filename+".txt")
        file = open(filepath,mode);
        file.write(text);

        if mode=="w":
            print ("File "+filename+".txt"+" is created successfully!. Thanks for using our application!");
        else:
            print("File " + filename + ".txt" + " is appended successfully!. Thanks for using our application!");

        file.close();



# print(FileUtility.validate_xml("result.xml"))
print(FileUtility.crt_txt_file.__doc__)