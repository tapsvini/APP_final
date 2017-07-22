from lxml import etree


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

        radius=Radis which is taken as input from user
        length=which is output after doing calculation

        """

        root = etree.Element('TestResult');
        child_radius = etree.Element('radius');
        child_radius.text = radius;
        root.append(child_radius);
        child = etree.Element('length');
        child.text = length;
        root.append(child);
        s = etree.tostring(root, pretty_print=True);
        return s



    def createXMLFile(self,filename,mode,text):         # Method to write text into given xml file name

        """
        INPUT

        filename=Filename where results should be saved
        mode=valid values w,a. whether to create new file or append the result in previous file.
        text= text which needs to be write into the filename
        """

        file = open(filename,mode);
        file.write(text);
        print (file);
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

        file = open(filename+".txt",mode);
        file.write(text);

        if mode=="w":
            print ("File "+filename+".txt"+" is created successfully!");
        else:
            print("File " + filename + ".txt" + " is appended successfully!");

        file.close();
