from src.util.UserInputUtil import InputUtility
from src.util.FileUtil import FileUtility
from src.com.app.APPSummerProject.Coaster import Coaster
from src.com.app.APPSummerProject.Cheers import CheersHelper

#For validation of input
cust_input=InputUtility();


#ask radius of coaster from the user
radius=cust_input.integerValidation("Please enter the radius of the circle(Only numbers)")

#Object of coaster
coasterObj=Coaster(radius);

#to calculate alpha and lenght require to get area of overlap region, which will be half of one of the coaster
cheersHelperObj=CheersHelper();

#for creating text file
fileUtilObj=FileUtility();

custom_length=cheersHelperObj.calLength(cheersHelperObj.calAlpha(),coasterObj.getRadius())
fileText=fileUtilObj.formateTextResult(radius,custom_length)

lib_fun_length=cheersHelperObj.usingLibraryFunction(coasterObj.getRadius())

fileText1=fileUtilObj.formateTextResult(radius,lib_fun_length)

print("\n\n"+fileText)

#To see the absolute error and relative error uncomment following code.

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

save_in_file=cust_input.textValidation("\nDo you want to save the result in text file(y/n)",["y","n"])

if save_in_file=="y":
    mode_of_file=cust_input.textValidation("Do you want to append the result to previous file or do you want to create a new file(a/w)",["a","w"])
    file_name=input("Please enter the name of the file where you want to store the result");
    fileUtilObj.createTxtFile(file_name,mode_of_file,fileText)

else:
    print("Thanks for using our Application!")


