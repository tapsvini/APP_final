from src.util.MathUtil import MathUtility as math
from decimal import Decimal
from src.com.app.APPSummerProject.Coaster import Coaster
from math import sin
from math import cos
from math import pi

class CheersHelper:




    def calAlpha(self):          #To calculate the value of alpha

        """
        INPUT

        value_of_sin = Value of sin
        value_of_pi  = Value of pi

        """

        mathUtilObj = math();
        self.customalpha=(Decimal(mathUtilObj.findSin())+Decimal(mathUtilObj.chudnovskyBig(30)/2))*Decimal(180/3.14)
        return self.customalpha



    def calLength(self, value_of_alpha, coasterRadius):     # To calculate the value of alpha

        """
        INPUT

        value_of_alpha = value of angle made in between the two circle
        radius  = radius of Coaster

        """

        obj=math();
        self.customLength=2*coasterRadius*(1-obj.findCosine(value_of_alpha/2))
        return self.customLength



    def usingLibraryFunction(self,coasterRadius):    #Function to calculate length and alpha using inbuilt libraries
        alpha=(Decimal(sin(132.4135*pi/180))+Decimal(pi/2))*Decimal(180/pi)
        length=2*coasterRadius*(1-cos((alpha/2)*Decimal(pi/180)))
        return length


