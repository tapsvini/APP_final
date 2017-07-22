from src.util.UserInputUtil import InputUtility as iu
from src.util.FileUtil import FileUtility
from src.com.app.APPSummerProject.Coaster import Coaster
from src.com.app.APPSummerProject.Cheers import CheersHelper


class Incarnation1:

    """This class is the starting point of the Incarnation 1"""

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

        cheersHelperObj = CheersHelper();

        for x in range(radii_list.__len__()):
            custom_length = cheersHelperObj.cal_length(cheersHelperObj.cal_alpha(), coaster_obj[x].get_radius())
            file_text = file_text + FileUtility.form_txt_result(coaster_obj[x].get_radius(), custom_length)

        print("\n\n" + file_text)

        """To see the absolute error and relative error uncomment following code.

        #lib_fun_length=cheersHelperObj.sol_use_lib_fun(coasterObj.get_radius())
        #fileText1=FileUtility.form_txt_result(coaster_obj[x].get_radius(), lib_fun_length)
        #
        # print("Using Library function the results are\n\n")
        #
        # print(fileText1)
        #
        # abs_error=0
        # if (lib_fun_length-custom_length)<0:
        #     abs_error=-(lib_fun_length-custom_length)
        # else:
        #     abs_error = lib_fun_length - custom_length
        #
        # print("Absolute Error is ="+str(abs_error))
        #
        # print("Relative Error is ="+str(abs_error/lib_fun_length))

        """

        save_in_file = iu.txt_vldtn("\nDo you want to save the result in text file(y/n)", ["y", "n"])

        if save_in_file == "y":
            file_name = input("Please enter the name of the file where you want to store the result");
            FileUtility.crt_txt_file(file_name, file_text)

        else:
            print("Thanks for using our Application!")


Incarnation1()





