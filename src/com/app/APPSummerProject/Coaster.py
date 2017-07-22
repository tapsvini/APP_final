from src.util.MathUtil import MathUtility

class Coaster:
    def __init__(self,radius):
        self.__radius=radius;

    def get_radius(self):
        """Function to get radius of the coaster.

        :return:value of coaster radius
        """

        return self.__radius;

    def get_area(self):

        """Function to get area of the coaster.

        :return:value of area of coaster
        """

        obj=MathUtility();
        return obj.chudnovsky_big(15) * self.__radius * self.__radius
