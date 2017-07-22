from src.util.MathUtil import MathUtility

class Coaster:
    def __init__(self,radius):
        self.__radius=radius;

    def getRadius(self):         #Get radius of the coaster
        return self.__radius;

    def getArea(self):          #Get area of the coaster
        obj=MathUtility();
        return obj.chudnovskyBig(15)*self.__radius*self.__radius

    def getPerimeter(self):     #Get perimeter of the coaster
        obj=MathUtility();
        return 2*obj.chudnovskyBig(15)*self.__radius