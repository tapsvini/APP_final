from unittest import TestCase
from src.com.app.APPSummerProject.Coaster import Coaster


class TestCoaster(TestCase):

    """Test class to check the functionality of Coaster class and its methods"""

    def test_get_radius(self):
        """Function to test whether XML is creating properly or not

        :return:Pass if radius is coming properly
        """
        obj=Coaster(10);

        self.assertTrue(obj.get_radius(), 10)


    def test_get_area(self):

        """Test case to check weather area given by coaster class is right.

        :return:Pass if area is coming properly
        """
        obj = Coaster(10);
        self.assertEqual(int(obj.get_area()),int(314.1592653589793238462643384))
