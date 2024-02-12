from Functions import validIndex, implementMenu7

def menu5(dates):
    """This function compares two instances of Date, which are selected by the user, and then prints some information regarding the difference.  If both dates are identical, then a statement saying so will be printed to the screen.  The function takes in one mutable argument of type list, containing elements of type Date."""
    
    #declaration and initialization of variables
    index1 = index2 = 0

    #conditional statement which evaluates to True if the length of the list called dates is greater than two
    if len(dates) > 2:
        print("You will be prompted to enter two indices that are associated with the dates you wish to compare.")
        
        #calling validIndex function to get two valid indices from the user
        index1 = validIndex.validIndex(dates)
        index2 = implementMenu7.implementMenu7(dates)

        #comparing two instances of Date at index1 and index2
        dates[index1].compare(dates[index2])

    #conditional statement which evaluates to True if the length of the list called dates is equal to two
    elif len(dates) == 2:
        #comparing two instances of Date at index1 and index2
        dates[0].compare(dates[1])

    #conditional statement which evaluates to True if the length of the list called dates is one
    else:
        print("Only one date has been created; therefore, it cannot be compared to anything else.")    