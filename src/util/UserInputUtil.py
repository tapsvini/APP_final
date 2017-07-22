


class InputUtility:

    def integerValidation(self,message):        # Function to validate integer input type from user

        """
        INPUT

        message=message to be shown when to ask for the input

        """

        while True:
            try:
                return int(input(message))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")



    def textValidation(self,message,valid_values=[]):       # Function to validate input type from user with only valid values

        """
        INPUT

        message=message to be shown when to ask for the input
        valid_values=List of valid values which is acceptable or are valid inputs

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


    def integerRangeValidation(self,message,start,end): # Function to validate integer input type from user with only
        # values between start and end

        """
        INPUT

        message=message to be shown when to ask for the input
        Start=Starting point of range
        end=Ending point of range

        """

        while True:
            try:
                input_value=self.integerValidation(message);

                if start<=input_value<=end:
                    return input_value

                else:
                    raise Exception('invalidValue', 'Please enter only integer between the specified range')

            except Exception as inst:
                x,y=inst.args
                print(y)




