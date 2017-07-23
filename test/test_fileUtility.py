from unittest import TestCase
from src.util.FileUtil import FileUtility


class TestFileUtility(TestCase):

    """Test cases to test the functionality of FileUtility class"""

    def test_validate_xml(self):

        """Function to test validation of xml is working properly

        :return:Pass if validation of xml is working properly
        """
        self.assertTrue(int(FileUtility.validate_xml("../resources/result/XMLFile/result.xml")), 1)

    def test_generate_xml(self):

        """Function to test whether xml text is generating properly or not

        :return:Pass if proper xml file text is generating
        """

        str = "<TestResult>\n<Radiuss>5</Radius>\n<Length>10</Length>\n<TestResult>"
        self.assertTrue(FileUtility.generate_xml(10,5),str)

    def test_file_exists(self):

        """Function to test whether file exist function working properly or not

        :return:Pass if file exist function is working properly
        """

        self.assertTrue(int(FileUtility.file_exists("../resources/result/XMLFile/result.xml")), 1)

    def test_file_exists1(self):

        """Function to test whether file exist function working properly or not(Negative case)

        :return:Pass if file exist function is working properly
        """

        self.assertTrue(str(int(FileUtility.file_exists("../resources/result/XMLFile/hel.xml"))), str(0))

    def test_create_xml_file(self):

        """Function to test whether XML is creating properly or not

        :return:Pass if XML file creation is working properly
        """
        str = "<TestResult>\n<Radiuss>5</Radius>\n<Length>10</Length>\n<TestResult>"
        self.assertTrue((FileUtility.create_xml_file("test",str)),"Success")

    def test_form_txt_result(self):

        """Function to test whether plain text for result is working or not

        :return:Pass if proper plain text result is working right
        """

        str="The Radius entered by you is = 12\nThe length require for overlapping area to be half of one circle = 15.897105436465978"
        self.assertTrue((FileUtility.form_txt_result(12,15.897105436465978)), str)

    def test_crt_txt_file(self):

        """Function to  test whether creation of plain text file is working properly or not.

        :return:Pass if proper plain text file is creating.
        """
        str ="The Radius entered by you is = 12\nThe length require for overlapping area to be half of one circle = 15.897105436465978"
        self.assertTrue((FileUtility.crt_txt_file("test", str)), "Success")
