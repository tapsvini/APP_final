from decimal import Decimal
from src.util.UserInputUtil import InputUtility


class MathUtility:


    def factorial(self,num):    # function to calculate the factorial of given number.

        """
        INPUT

        num=Number whose factorial is required

        """

        if num<1:
            return 1;

        else:
            return num * self.factorial(num-1);


    def roundno(self,num, point):   # Function for rounding off number to specific point

        """
        INPUT

        num=Number to be roundoff
        point = Total number needed after decimal point

        """

        scale = 10 ** point;

        return int(num * scale) / scale;


    def chudnovsky(self):   # Calculating value of pi using chudnovskyBig algorithm

        pi = 0;
        k = 0;
        round_of_true=0;
        input=InputUtility()
        # Number of iteration for chudnovskyBig algorithm to find value of pi
        no_of_iteration_for_accuracy = input.integerValidation(
            "We need number of iteration for calculating value of pi using chudnovskyBig al"
            "gorithm l(hint:More no of terms more accurate will be the value and will take "
            "more time to calculate it))");

        # Ask user whether to round off the value of calculated pi or not
        round_off_true = input.textValidation("Do you want us to round "
                                              " off the value(Y/N)",
                                              ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);
        # If user agrees on rounding off the value
        if round_off_true == "y" or round_off_true == "Y" or round_off_true == "Yes" or round_off_true == "YES" or \
                        round_off_true == "yes":
            # Ask number of digit to round off
            round_off = input.integerRangeValidation("Please enter the number of digit you want to consider in "
                                                      "value of pi(Min=1,Max:27)",1,27);
            round_of_true=1;


        while k < no_of_iteration_for_accuracy:
            pi += (Decimal(-1)**k)*(Decimal(self.factorial(6*k))/((self.factorial(k)**3)*(self.factorial(3*k)))*
                                    (13591409+545140134*k)/(640320**(3*k)));
            k += 1;
        pi = pi * Decimal(10005).sqrt()/4270934400;
        pi = pi**(-1);

        if round_of_true==1:
            return self.roundno(pi,round_off);

        else:
            return self.roundno(pi,27);



    def chudnovskyBig(self,no_of_iteration_for_accuracy):       # Calculating value of pi using chudnovskyBig algorithm

        pi = 0;
        k = 0;
        while k < no_of_iteration_for_accuracy:
            pi += (Decimal(-1)**k)*(Decimal(self.factorial(6*k))/((self.factorial(k)**3)*(self.factorial(3*k)))*
                                    (13591409+545140134*k)/(640320**(3*k)));
            k += 1;
        pi = pi * Decimal(10005).sqrt()/4270934400;
        pi = pi**(-1);

        return pi;


    def findSin(self):      # Calculating sin value using tayler series
        sine = 0;
        round_of_true = 0;
        input = InputUtility()

        #This value is calculated by hand and the description in provided in the documentation
        degree = 132.4135
        # degree = 30
        no_of_terms = input.integerRangeValidation("Enter no of terms to calculate value of sin(We are using Tayler series)"
                                              "(Min:1,Max450)\n(Hint:-More number of terms more accurate result will be,But also increases "
                                              "the time to calculate it)",1,450);

        # Ask user whether to round off the value of calculated sin or not
        round_off_sin_true = input.textValidation("Do you want us to round "
                                                  " off the value of sin(Y/N)",
                                                  ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);

        # If user agrees on rounding off the value
        if round_off_sin_true == "y" or round_off_sin_true == "Y" or round_off_sin_true == "Yes" or round_off_sin_true == "YES"\
                or round_off_sin_true == "yes":
            # Ask number of digit to round off
            round_off_digit = input.integerRangeValidation("Please enter the number of digit you want to consider in "
                                                      "value of sin(Min 1, Max:27)",1,27);
            round_of_true = 1;


        pi = self.chudnovskyBig(20);
        for i in range(no_of_terms):
            sign = (-1)**i;
            y=Decimal(degree)*(pi/180);
            sine = sine + ((y**(2*i+1))/self.factorial(2*i+1))*sign;

        if round_of_true==1:
            return self.roundno(sine,round_off_digit)
        else:
            return self.roundno(sine,27)


    def findCosine(self,degree):        # Calculating cos value using tayler series

        """
        INPUT

        degree=Cosine degree
        no_of_terms = no of terms to be calculated in tayler series
        rounding_upto = total digit in decimal

        """

        cosx = 1
        round_of_true = 0;
        input = InputUtility()
        sign = -1

        no_of_terms = input.integerRangeValidation("Enter no of terms to calculate value of cos(We are using Tayler series)"
            "(Min:1,Max450)\n(Hint:-More number of terms more accurate result will be,But also increases "
            "the time to calculate it)",1,450);

        # Ask user whether to round off the value of calculated sin or not
        round_off_cos_true = input.textValidation("Do you want us to round "
                                                  " off the value of cos(Y/N)",
                                                  ["y", "n", "Y", "N", "Yes", "yes", "YES", "NO", "no"]);

        # If user agrees on rounding off the value
        if round_off_cos_true == "y" or round_off_cos_true == "Y" or round_off_cos_true == "Yes" or \
                        round_off_cos_true == "YES" or round_off_cos_true == "yes":
            # Ask number of digit to round off
            round_off_digit = input.integerRangeValidation("Please enter the number of digit you want to consider in "
                                                           "value of cos(Min 1, Max:27)", 1, 27);
            round_of_true = 1;


        pi=self.chudnovskyBig(20);
        for i in range(2, no_of_terms, 2):
            y=degree*(pi/180)
            cosx = cosx + (sign*(y**i))/self.factorial(i)
            sign = -sign

        if round_of_true==1:
            return self.roundno(cosx,round_off_digit)
        else:
            return self.roundno(cosx,27)



