from Classes import Date
from Functions import menu, menu1, menu5, menu7, validIndex

def implementation(userInput, dates):
    """This function determines how the program should flow depending on the user's menu selection.  This function takes in two arguments: the user's menu selection of type string and a list of dates created by the user, containing elements of type Date"""

    #declaring and initializing variable by calling validIndex function
    index = validIndex.validIndex(dates, userInput)

    #conditional statement which evaluates to True if the user's menu selection is "1"
    if userInput == "1":
        #calling menu1 function
        menu1.menu1(dates)

    #conditional statement which evaluates to True if the user's menu selection is "2"
    elif userInput == "2":
        #setting the format for which the dates should be displayed
        Date.setFormat()

    #conditional statement which evaluates to True if the user's menu selection is "3"
    elif userInput == "3":
        #printing date at specified index
        print("Date " + str(index) + ": " + dates[index].show())

    #conditional statement which evaluates to True if the user's menu selection is "4"
    elif userInput == "4":
        #incrementing the date specified index by a specified number of days
        dates[index].increment()   

    #conditional statement which evaluates to True if the user's menu selection is "5"
    elif userInput == "5":
        #calling menu5 function
        menu5.menu5(dates)

    #conditional statement which evaluates to True if the user's menu selection is "6"
    elif userInput == "6":
        #calling menu function
        menu() 

    #conditional statement which evaluates to True if the user's menu selection is "7"
    elif userInput == "7":
        #calling menu7 function
        menu7.menu7(dates)  

    #conditional statement which evaluates to True if the user's menu selection is invalid
    else:
        print("Invalid entry.  Try again.")          