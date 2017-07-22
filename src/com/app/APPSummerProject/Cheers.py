from src.util.MathUtil import MathUtility
from decimal import Decimal
from math import sin
from math import cos
from math import pi

class CheersHelper:

    def cal_alpha(self):

        """Function to calculate the value of alpha.

        :return:value of alpha
        """

        self.customalpha= (Decimal(MathUtility.find_sin()) + Decimal(MathUtility.chudnovsky_big(30) / 2)) * Decimal(180 / 3.14)
        return self.customalpha



    def cal_length(self, value_of_alpha, cstr_radius):

        """Function to calculate the value of alpha.

        :param value_of_alpha:value of angle made in between the two circle
        :type value_of_alpha:decimal
        :param cstr_radius:radius of Coaster
        :type cstr_radius:int
        :return: value of length require to get area of overlap region equals to half of one of the circle
        """

        self.customLength=2*cstr_radius*(1 - MathUtility.find_cos(value_of_alpha / 2))
        return self.customLength

    @staticmethod
    def sol_use_lib_fun(cstr_radius):

        """Function to calculate length and alpha using inbuilt libraries.

        :param cstr_radius:Radius of the coaster
        :type cstr_radius:int
        :return: returns the value of length require to get area of overlap region equals to half using inbuilt library
        function
        """

        alpha=(Decimal(sin(132.4135*pi/180))+Decimal(pi/2))*Decimal(180/pi)
        length=2*cstr_radius*(1-cos((alpha/2)*Decimal(pi/180)))
        return length


