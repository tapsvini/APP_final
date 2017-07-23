from unittest import TestCase
from src.com.app.APPSummerProject.Cheers import CheersHelper
import math


class TestCheersHelper(TestCase):

    """Test Cases to test whether cheersHelper functionlity working properly or not"""

    def test_cal_alpha(self):

        """Test case to check weather alpha value is coming accurate.

        :return:Pass if alpha is coming properly
        """

        obj=CheersHelper()
        self.assertEqual(math.ceil(obj.cal_alpha(52,2)), int(132.415))

    def test_cal_length(self):

        """Test case to check weather length value is coming accurate.

        :return:Pass if length is coming properly
        """

        obj = CheersHelper()
        self.assertEqual(math.ceil(obj.cal_length(obj.cal_alpha(34,2),45,34,2)), int(54.0))

    def test_sol_use_lib_fun(self):

        """Test case to check weather length value is coming accurate using inbuild funtion.

        :return:Pass if length is coming properly
        """

        obj = CheersHelper()
        self.assertEqual(math.ceil(obj.sol_use_lib_fun(45)), int(54.0))
