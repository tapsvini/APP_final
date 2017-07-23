from unittest import TestCase
from src.util.MathUtil import MathUtility

class TestMathUtility(TestCase):
    def test_factorial(self):
        """Test case to check weather factorial of number is accurate.

        :return:Pass if factorial of value is accurate.
        """
        num=5
        self.assertEqual(MathUtility.factorial(5),120)

    def test_roundno(self):

        """Test case to check weather rounding off number is accurate.

        :return:Pass if rounding of value is accurate.
        """

        num=3.1432
        self.assertEqual(MathUtility.roundno(num,2),3.14)

    def test_chudnovsky_big(self):

        """Test case to check weather pi value is cacluting right.

        :return:Pass if pi value is accurate.
        """

        self.assertEqual(int(MathUtility.chudnovsky_big(30)), int(3.14))

    def test_find_sin(self):
        """Test case to check value of sin

        :return:Pass if value of sin is accurate.
        """
        self.assertEqual(int(MathUtility.find_sin(22, 2)), int(0))

    def test_find_cos(self):
        """Test case to check value of cos

        :return:Pass if valueo of cos is accurate.
        """
        self.assertEqual(MathUtility.find_cos(30,22,2),0.86)

    def test_abs_err(self):
        """Test case to check absolute error working fine

        :return:Pass if absolute error is accurate.
        """
        self.assertEqual(MathUtility.abs_err(2,1),1)

    def test_rel_err(self):

        """Test case to check relative error working fine

        :return:Pass if relative error is accurate.
        """

        self.assertEqual(MathUtility.rel_err(2, 1), 0.5)

