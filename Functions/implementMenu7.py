import string

def implementMenu7(dates):
    """This functions implements a portion of menu option seven and gets a valid integer index from the user that is associated with a date.  The function takes in one mutable parameter of type list containing elements of type Date"""

    #declaration and initialization of local variables
    flag = flag2 = False

    #while loop which runs while flag is equal to False
    while flag == False:
        #getting date index from user
        validIndex = input("When prompted, enter the index (the number) associated with the date.\nWhich date would you like to work with? > ")

        #for loop which iterates over the integers between zero, inclusive, and the length of the dates list, exclusive
        for i in range(0, len(validIndex)):
            #conditional statement which evaluates to True if any character within validIndex is not found in the string called string.digits
            if validIndex[i] not in string.digits:
                flag2 = True

        #conditional statement which evaluates to True if flag2 is False
        if flag2 == False:
            #converting validIndex from a string object to an integer object
            validIndex = int(validIndex)

            #conditional statement which evaluates to True if the value of validIndex is greater than or equal to zero and less than the length of the dates list
            if validIndex >= 0 and validIndex < len(dates):
                flag = True

        #conditional statement which evaluates to True if flag2 is True
        else:
            print("A date at that index does not exist. Try again.")
            flag2 = False  

    #returning validIndex
    return validIndex                