from src.util.UserInputUtil import InputUtility
from src.util.FileUtil import FileUtility
from src.com.app.APPSummerProject.Coaster import Coaster
from src.com.app.APPSummerProject.Cheers import CheersHelper

"""For validation of input"""

cust_input=InputUtility();

"""ask radius of coaster from the user"""

radius=cust_input.int_vldtn("Please enter the radius of the circle(Only numbers)")

"""Object of coaster"""

coasterObj=Coaster(radius);

"""to calculate alpha and lenght require to get area of overlap region, which will be half of one of the coaster"""

cheersHelperObj=CheersHelper();

"""for creating text file"""

fileUtilObj=FileUtility();

length=cheersHelperObj.sol_use_lib_fun(coasterObj.get_radius())

fileText1=fileUtilObj.formt_txt_result(radius, length)

print("Using Library function the results are\n\n")

print(fileText1)

save_in_file=cust_input.txt_vldtn("\nDo you want to save the result in XML file(y/n)", ["y", "n"])

if save_in_file=="y":
    mode_of_file=cust_input.txt_vldtn("Do you want to append the result to previous file or do you want to create a new file(a/w)", ["a", "w"])
    file_name=input("Please enter the name of the file where you want to store the result");
    fileUtilObj.create_xml_file(file_name, mode_of_file, fileUtilObj.generate_xml(radius, length))

else:
    print("Thanks for using our Application!")


