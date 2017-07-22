


class InputUtility:
    """"The class provides functionality to put validation on user input"""

    @staticmethod
    def int_vldtn(message):

        """Function to validate integer input type from user.

        :param message: message to be shown when to ask for the input
        :type message:string
        :return: value of integer input given by user
        :type Int
        """

        while True:
            try:
                return int(input(message))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

    @staticmethod
    def txt_vldtn(message, valid_values=[]):

        """Function to validate input type from user with only valid values.

        :param message:message to be shown when to ask for the input
        :type message:string
        :param valid_values:List of valid values which is acceptable or are valid inputs
        :type valid_values:list
        :return: value of text input given by user
        :type String
        """

        while True:
            try:
                input_value=input(message);
                input_value_valid="false";
                for x in valid_values:
                    if input_value==x:
                        input_value_valid="true";
                if input_value_valid=="false":
                    raise Exception('invalidValue', 'Please enter only valid values')
                else:
                    return input_value
            except Exception as inst:
                x,y=inst.args
                print(y)

    @staticmethod
    def int_rng_vldtn(message, start, end):

        """Function to validate integer input type from user with only.

        :param message:message to be shown when to ask for the input
        :type message:string
        :param start:Starting point of range
        :type start:int
        :param end:Ending point of range
        :type end:int
        :return: value of integer input given by user
        :type Int
        """

        while True:
            try:
                input_value=InputUtility.int_vldtn(message);

                if start<=input_value<=end:
                    return input_value

                else:
                    raise Exception('invalidValue', 'Please enter only integer between the specified range')

            except Exception as inst:
                x,y=inst.args
                print(y)




