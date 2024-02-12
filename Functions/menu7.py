def menu7(dates):
    """This function prints a summary of all the dates that the user created throughout his or her duration of using this application"""

    #conditional statement which evaluates to True if the length of the list called dates is greater than one
    if len(dates) > 1:
        print("Here is a list of all the dates created by you in chronological order:")   

        #for loop which iterates over the integers between zero, inclusive, and the length of the list called dates, exclusive
        for i in range(0, len(dates)):
            #for loop which iterates over the integers between zero, inclusive, and the length of the list called dates, exclusive
            for j in range(0, len(dates)):
                #conditional statement which evaluates to True if date at index i is greater than or equal to the date at index j
                if dates[i] >= dates[j]:
                    #swapping dates at index i and j
                    dates[i], dates[j] = dates[j], dates[i]

        #reversing the order of the list called dates
        dates.reverse()

        #for loop which iterates over the integers between zero, inclusive, and the length of the list called dates, exclusive
        for i in range(0, len(dates)):
            print("> " + dates[i].show())

    #conditional statement which evaluates to True if the length of dates is equal to one or less
    else:
        print("Here is the singular date that you created: " + dates[0].show())