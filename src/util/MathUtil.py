from decimal import Decimal
from src.util.UserInputUtil import InputUtility


class MathUtility:
    """This class provides the functionality to calculate value of sin and cos using tayler series, calculate value of
    pi using chudnovsky algorithm or to find the factorial and round off number of a number"""
    @staticmethod
    def factorial(num):

        """Function to calculate the factorial of given number.

        :param num:Number whose factorial is required
        :type num:int
        :return: factorial of a number
        :type Int
        """

        if num<1:
            return 1;

        else:
            return num * MathUtility.factorial(num-1);

    @staticmethod
    def roundno(num, point):

        """Function for rounding off number to specific point.

        :param num:Number to be roundoff
        :type num:int
        :param point:Total number needed after decimal point
        :type point:int
        :return:round off number
        :type Decimal
        """

        scale = 10 ** point;

        return int(num * scale) / scale;

    @staticmethod
    def chudnovsky():

        """Calculating value of pi using chudnovsky_big algorithm.

        :return: value of pi
        :type Decimal
        """

        pi = 0;
        k = 0;
        round_of_true=0;
        input=InputUtility()

        """Number of iteration for chudnovsky_big algorithm to find value of pi"""

        no_of_iteration_for_accuracy = input.int_vldtn(
            "We need number of iteration for calculating value of pi using chudnovsky_big al"
            "gorithm l(hint:More no of terms more accurate will be the value and will take "
            "more time to calculate it))");

        """ Ask user whether to round off the value of calculated pi or not"""

        round_off_true = input.txt_vldtn("Do you want us to round "
                                              " off the value(Y/N)",
                                         ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);
        """ If user agrees on rounding off the value"""
        if round_off_true == "y" or round_off_true == "Y" or round_off_true == "Yes" or round_off_true == "YES" or \
                        round_off_true == "yes":

            """ Ask number of digit to round off"""

            round_off = input.int_rng_vldtn("Please enter the number of digit you want to consider in "
                                                      "value of pi(Min=1,Max:27)", 1, 27);
            round_of_true=1;


        while k < no_of_iteration_for_accuracy:
            pi += (Decimal(-1)**k)*(Decimal(MathUtility.factorial(6*k))/((MathUtility.factorial(k)**3)*
                                        (MathUtility.factorial(3*k)))*(13591409+545140134*k)/(640320**(3*k)));
            k += 1;
        pi = pi * Decimal(10005).sqrt()/4270934400;
        pi = pi**(-1);

        if round_of_true==1:
            return MathUtility.roundno(pi,round_off);

        else:
            return MathUtility.roundno(pi,27);

    @staticmethod
    def chudnovsky_big(no_of_iteration_for_accuracy):

        """Function to calculate value of pi using chudnovsky_big algorithm.

        :param no_of_iteration_for_accuracy: no of iteration for calculating value of pi using chudnovsky_big algorithm
        :type no_of_iteration_for_accuracy:int
        :return: value of pi
        :type Decimal
        """

        pi = 0;
        k = 0;
        while k < no_of_iteration_for_accuracy:
            pi += (Decimal(-1)**k)*(Decimal(MathUtility.factorial(6*k))/((MathUtility.factorial(k)**3)*
                                                (MathUtility.factorial(3*k)))*(13591409+545140134*k)/(640320**(3*k)));
            k += 1;
        pi = pi * Decimal(10005).sqrt()/4270934400;
        pi = pi**(-1);

        return pi;

    @staticmethod
    def find_sin():

        """Function to calculate sin value using tayler series.

        :return: Value of sin using tayler series
        :type Decimal
        """

        sine = 0;
        round_of_true = 0;
        input = InputUtility()

        """This value is calculated by hand and the description in provided in the documentation"""
        degree = 132.4135

        no_of_terms = input.int_rng_vldtn("Enter no of terms to calculate value of sin(We are using Tayler series)"
                                              "(Min:1,Max450)\n(Hint:-More number of terms more accurate result will be,But also increases "
                                              "the time to calculate it)", 1, 450);

        """ Ask user whether to round off the value of calculated sin or not"""

        round_off_sin_true = input.txt_vldtn("Do you want us to round "
                                                  " off the value of sin(Y/N)",
                                             ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);

        """If user agrees on rounding off the value"""

        if round_off_sin_true == "y" or round_off_sin_true == "Y" or round_off_sin_true == "Yes" or round_off_sin_true == "YES"\
                or round_off_sin_true == "yes":

            """Ask number of digit to round off"""

            round_off_digit = input.int_rng_vldtn("Please enter the number of digit you want to consider in "
                                                      "value of sin(Min 1, Max:27)", 1, 27);
            round_of_true = 1;


        pi = MathUtility.chudnovsky_big(20);
        for i in range(no_of_terms):
            sign = (-1)**i;
            y=Decimal(degree)*(pi/180);
            sine = sine + ((y**(2*i+1))/MathUtility.factorial(2*i+1))*sign;

        if round_of_true==1:
            return MathUtility.roundno(sine,round_off_digit)
        else:
            return MathUtility.roundno(sine,27)

    @staticmethod
    def find_cos(degree):

        """Function to calculat cos value using tayler series.

        :param degree: value of alpha in radianas whose cosine value is needed
        :type degree:decimal
        :return: value of cosine
        :type Decimal
        """

        cosx = 1
        round_of_true = 0;
        input = InputUtility()
        sign = -1

        no_of_terms = input.int_rng_vldtn("Enter no of terms to calculate value of cos(We are using Tayler series)"
            "(Min:1,Max450)\n(Hint:-More number of terms more accurate result will be,But also increases "
            "the time to calculate it)", 1, 450);

        """Ask user whether to round off the value of calculated sin or not"""

        round_off_cos_true = input.txt_vldtn("Do you want us to round "
                                                  " off the value of cos(Y/N)",
                                             ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);

        """If user agrees on rounding off the value"""

        if round_off_cos_true == "y" or round_off_cos_true == "Y" or round_off_cos_true == "Yes" or \
                        round_off_cos_true == "YES" or round_off_cos_true == "yes":

            """Ask number of digit to round off"""

            round_off_digit = input.int_rng_vldtn("Please enter the number of digit you want to consider in "
                                                           "value of cos(Min 1, Max:27)", 1, 27);
            round_of_true = 1;


        pi=MathUtility.chudnovsky_big(20);
        for i in range(2, no_of_terms, 2):
            y=degree*(pi/180)
            cosx = cosx + (sign*(y**i))/MathUtility.factorial(i)
            sign = -sign

        if round_of_true==1:
            return MathUtility.roundno(cosx,round_off_digit)
        else:
            return MathUtility.roundno(cosx,27)



