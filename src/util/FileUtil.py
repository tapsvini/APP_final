from lxml import etree
import os
from yattag import Doc, indent


class FileUtility:
    """The class provides the basic functions to deal with file like creation of xml or text file, validating xml file
    finding weather file exist or not"""


    @staticmethod
    def validate_xml(filename):

        """Function to validate generated Xml with dtd.

        :param filename:filename(which should be xml) which is required to be validated with full path
        :type filename:string
        :return: True if xml file is validated else False.
        :type: Boolean
        """

        parser = etree.XMLParser(dtd_validation=True);
        tree = etree.parse(filename, parser);
        try:
            if tree:
                return True
            else:
                return False
        except Exception as inst:
            x, y = inst.args
            print(y)


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
    def create_xml_file(filename,text):

        """Function to write text into given xml file name.

        :param filename:Filename where results should be saved
        :type filename:string
        :param mode:valid values w,a. whether to create new file or append the result in previous file.
        :type mode:string
        :param text:text which needs to be write into the filename
        :type text:string
        :return: success or failure string depending on whether xml file is created and validated or not.
        :type String
        """
        if filename != "test":
            filepath = os.path.join('../../../../resources/result/XMLFile', filename + ".xml")
        else:
            filepath=filename

        xml_head_txt="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+"<!DOCTYPE Cheers SYSTEM \"cheers.dtd\">\n<Cheers>"

        file = open(filepath, "w");

        file.write(xml_head_txt+str(text)+"\n</Cheers>");
        print ("File "+filename+".xml created successfully. Thanks for using our application!");
        file.close();

        if filename=="test" or FileUtility.validate_xml(filepath):
            print("Your XML file has been validated with cheers.dtd scheme!")
            return "Success"
        else:
            print("XML file formed is not validated and may contain error")
            return "Failure"



    @staticmethod
    def form_txt_result(radius, length):

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
    def crt_txt_file(filename,text):

        """Function to write text into given file name.

        :param filename:Filename where results should be saved
        :type filename:string
        :param text:text which needs to be write into the filename
        :type text:string
        :return: success or unsuccess message.
        :type String
        """

        filepath = os.path.join('../resources/result/TestFile', filename+".txt")
        file = open(filepath,"w");
        file.write(text);

        print ("File "+filename+".txt"+" is created successfully!. Thanks for using our application!")

        file.close();

        return "Success"