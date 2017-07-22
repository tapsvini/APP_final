from src.util.MathUtil import MathUtility
from decimal import Decimal
from math import sin
from math import cos
from math import pi

class CheersHelper:
    """The class provides helper function to solve the cheers problem like calculating value of alpha and length."""

    def cal_alpha(self,no_of_iteration,round_off):

        """Function to calculate the value of alpha.

        :param no_of_iteration: Number of terms for calculating sin and pi using tayler series
        :type no_of_iteration:Int
        :param round_off: Till how many decimal place we have to calculate value of sin
        :type round_off:Int
        :return:value of alpha
        :type Decimal
        """

        self.custom_alpha= (Decimal(MathUtility.find_sin(no_of_iteration,round_off)) + Decimal(MathUtility.chudnovsky_big(no_of_iteration) / 2)) * Decimal(180 / MathUtility.chudnovsky_big(no_of_iteration))
        return self.custom_alpha



    def cal_length(self, value_of_alpha, cstr_radius,no_of_terms,round_off_digit):

        """Function to calculate the value of alpha.

        :param value_of_alpha:value of angle made in between the two circle
        :type value_of_alpha:decimal
        :param cstr_radius:radius of Coaster
        :type cstr_radius:int
        :param no_of_terms: Number of terms for calculating sin,cos and pi using tayler series
        :type no_of_terms:Int
        :param round_off_digit: Till how many decimal place we have to calculate value of sin,cos
        :type round_off_digit:Int
        :return: value of length require to get area of overlap region equals to half of one of the circle
        :type Decimal
        """

        self.customLength=2*cstr_radius*(1 - MathUtility.find_cos((value_of_alpha / 2),no_of_terms,round_off_digit))
        return self.customLength

    @staticmethod
    def sol_use_lib_fun(cstr_radius):

        """Function to calculate length and alpha using inbuilt libraries.

        :param cstr_radius:Radius of the coaster
        :type cstr_radius:int
        :return: returns the value of length require to get area of overlap region equals to half using inbuilt library
        function
        :type Decimal
        """

        alpha=(Decimal(sin(132.4135*pi/180))+Decimal(pi/2))*Decimal(180/pi)
        length=2*cstr_radius*(1-cos((alpha/2)*Decimal(pi/180)))
        return length


