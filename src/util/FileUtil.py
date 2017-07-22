from lxml import etree
import os


class FileUtility:


    def validateXML(self,filename):         #Function to validate generated Xml with dtd
        """
        INPUT

        filename=filename(which should be xml) which is required to be validated

        """
        parser = etree.XMLParser(dtd_validation=True);
        tree = etree.parse(filename, parser);
        if tree:
            print("Validated");
        else:
            print("Not Validated");





    def generateXml(self,radius,length):        # Function to generate XML

        """
        INPUT

        radius=Radius which is taken as input from user
        length=which is output after doing calculation

        """

        # create XML
        root = etree.Element('TestResult')
        child1 = etree.SubElement(root, "Radius")
        child1.text=str(radius)
        child2 = etree.SubElement(root, "Length")
        child2.text = str(length)

        # pretty string
        s=etree.tostring(root, pretty_print=True)

        return s



    def createXMLFile(self,filename,mode,text):         # Method to write text into given xml file name

        """
        INPUT

        filename=Filename where results should be saved
        mode=valid values w,a. whether to create new file or append the result in previous file.
        text= text which needs to be write into the filename
        """

        filepath = os.path.join('../../../../resources/result/XMLFile', filename + ".xml")
        file = open(filepath, mode);
        file.write(str(text));
        if mode=="w":
            print ("File "+filename+".xml created successfully");
        else:
            print("File " + filename + ".xml appended successfully");

        file.close();


    def formateTextResult(self,radius,length):   # Method to format the output of the program for writing into text file

        """
        INPUT

        radius=Radius of coaster
        length=lenght which is required to overlap two coaster with equal radii to get halp overlapping area.
        """

        return "The Radius entered by you is = "+str(radius)+" \nThe length require for overlapping area to be half of " \
                                                             "one circle = "+str(length)+"\n\n"



    def createTxtFile(self,filename,mode,text):     # Method to write text into given file name

        """
        INPUT

        filename=Filename where results should be saved
        mode=valid values w,a. whether to create new file or append the result in previous file.
        text= text which needs to be write into the filename
        """
        filepath = os.path.join('../resources/result/TestFile', filename+".txt")
        file = open(filepath,mode);
        file.write(text);

        if mode=="w":
            print ("File "+filename+".txt"+" is created successfully!");
        else:
            print("File " + filename + ".txt" + " is appended successfully!");

        file.close();


obj=FileUtility()
print(obj.generateXml(2,4))

# print(obj.createXMLFile("hello","w",obj.generateXml()))
