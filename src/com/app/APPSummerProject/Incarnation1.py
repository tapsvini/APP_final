from src.util.UserInputUtil import InputUtility as iu
from src.util.FileUtil import FileUtility
from src.util.MathUtil import MathUtility
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

        no_of_terms = iu.int_rng_vldtn("Enter no of terms to calculate value of sin and cos(We are using Tayler series)"
                                          "(Min:1,Max450)\n(Hint:-More number of terms more accurate result will be,But also increases "
                                          "the time to calculate it)", 1, 450);

        """ Ask user whether to round off the value of calculated sin, cos or not"""

        round_off_true = iu.txt_vldtn("Do you want us to round "
                                             " off the value of sin and cos(Y/N)",
                                             ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);

        """If user agrees on rounding off the value"""

        round_off_digit=25

        if round_off_true == "y" or round_off_true == "Y" or round_off_true == "Yes" or round_off_true == "YES" \
                or round_off_true == "yes":

            """Ask number of digit to round off"""

            round_off_digit = iu.int_rng_vldtn("Please enter the number of digit you want to consider in "
                                                  "value of sin(Min 1, Max:27)", 1, 25);

        #length obtain using custom function
        custom_length=[]
        for x in range(radii_list.__len__()):
            custom_length.insert(x,cheersHelperObj.cal_length(cheersHelperObj.cal_alpha(no_of_terms,round_off_digit),
                                                       coaster_obj[x].get_radius(),no_of_terms,round_off_digit))
            file_text = file_text + FileUtility.form_txt_result(coaster_obj[x].get_radius(), custom_length[x])

        #length obtain using libraries calculation
        lib_length = []
        for x in range(radii_list.__len__()):
            lib_length.insert(x, CheersHelper.sol_use_lib_fun(radii_list[x]))

        for x in range(radii_list.__len__()):
            print("\nFor radius "+str(radii_list[x]))
            print("The absolute error is "+ str(MathUtility.abs_err(lib_length[x],custom_length[x])))
            print("The relative error is " + str(MathUtility.rel_err(lib_length[x], custom_length[x])))
            print("\n")

        print("\n\n" + file_text)

        save_in_file = iu.txt_vldtn("\nDo you want to save the result in text file(y/n)", ["y", "n"])

        if save_in_file == "y":
            file_name = input("Please enter the name of the file where you want to store the result");
            FileUtility.crt_txt_file(file_name, file_text)

        else:
            print("Thanks for using our Application!")


Incarnation1()





