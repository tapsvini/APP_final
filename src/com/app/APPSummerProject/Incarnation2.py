from src.util.UserInputUtil import InputUtility as iu
from src.util.FileUtil import FileUtility
from src.com.app.APPSummerProject.Coaster import Coaster
from src.com.app.APPSummerProject.Cheers import CheersHelper


class Incarnation2:
    """This class is the starting point of the Incarnation 2"""

    def __init__(self):
        """Inilization of Incarnation1

        """

        """ask radius of coaster from the user"""
        radii_list = iu.list_int_vldtn("Enter Radius")

        file_text = ""

        """Object of coaster"""
        coaster_obj = []

        for x in range(radii_list.__len__()):
            coaster_obj.insert(x, Coaster(radii_list[x]))

        for x in range(radii_list.__len__()):
            length_lib = CheersHelper.sol_use_lib_fun(radii_list[x])
            file_text = file_text + FileUtility.generate_xml(coaster_obj[x].get_radius(), length_lib)

        print("Using Library function the results are\n\n")

        print(file_text)

        save_in_file = iu.txt_vldtn("\nDo you want to save the result in XML file(y/n)", ["y", "n"])

        if save_in_file == "y":
            file_name = input("Please enter the name of the file where you want to store the result");
            FileUtility.create_xml_file(file_name, file_text)

        else:
            print("Thanks for using our Application!")


Incarnation2()