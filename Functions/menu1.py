from Classes import Date
import string

def menu1(dates):
    """This function enables the user to create a date and provides implementation to ensure a valid date is inputted by the user.  The function takes in one mutable argument which is a list called dates containing elements of only type Date"""

    #declaration and initialization of local variables
    date = month = day = year = ""
    numBackSlashes = 0
    flag = flag2 = flag3 = False
    listOfInputs = []
    dateObject = Date()

    print("You are now creating a new date!\nEnter the date in one of the following formats:")

    #for loop which iterates over the variables between zero, inclusive, and five, exclusive
    for i in range(0, 5):
        #conditional statement which evaluates to True if i is equal to either zero or four
        if i == 0 or i == 4:
            print("--------------")

        #conditional statement which evaluates to True if i is equal to one    
        elif i == 1:
            print("|  1/4/2000  |")

        #conditional statement which evaluates to True if i is equal to two    
        elif i == 2:  
            print("| 01/04/0065 |")   

        #conditional statement which evaluates to True if i is equal to three     
        else:
            print("| 12/31/1845 |")

    print("* Note, there can be no spaces between the integers, and there must be a backslash separating the month, day, and year. *")

    #while loop which runs until flag is no longer equal to False
    while flag == False:
        #getting date entry from user and stripping whitespaces from both ends of the user's input
        date = input("Date Entry > ")
        date.strip()

        #for loop which iterates over the integers between zero, exclusive, and the length of date, exclusive
        for i in range(0, len(date)):
            #conditional statement which evaluates to True if the character at index i in date is not contained in the predefined list string.digits and is not equal to "/"
            if date[i] not in string.digits and date[i] != "/":
                flag2 = True

        #conditional statement which evaluates to True if flag2 is equal to False
        if flag2 == False:
            #for loop which iterates over the integers between zero, exclusive, and the length of date, exclusive
            for i in range(0, len(date)):
                #conditional statement which evaluates to True if numBackSlashes is equal to zero and the character at index i of date is not equal to "/"
                if numBackSlashes == 0 and date[i] != "/":
                    month += date[i]

                #conditional statement which evaluates to True if numBackSlashes is equal to one and the character at index i of date is not equal to "/"    
                elif numBackSlashes == 1 and date[i] != "/":
                    day += date[i]
                
                #conditional statement which evaluates to True if numBackSlashes is equal to two and the character at index i of date is not equal to "/"
                elif numBackSlashes == 2 and date[i] != "/":
                    year += date[i]
                
                #conditional statement which evaluates to True if the character at index i of date is equal to "/"
                elif date[i] == "/": 
                    numBackSlashes += 1   
            
            #conditional statement which evaluates to True if the following conditions are met
            if numBackSlashes == 2 and len(month) > 0 and len(day) > 0 and len(year) > 0:
                #for loop which iterates over the integers between zero, inclusive, and the length of listOfInputs, exclusive
                for i in range(0, len(listOfInputs)):
                    flag3 = False

                    #for loop which iterates over the integers between zero, inclusive, and the length of listOfInputs[i], exclusive
                    for j in range(0, len(listOfInputs[i])):
                        #conditional statement which evaluates to True if listOfInputs[i][j] is equal to "0" and flag3 is False
                        if listOfInputs[i][j] == "0" and flag3 == False:
                            listOfInputs[i][j].replace("0", "")

                        #conditional statement which evaluates to True if listOfInputs[i][j] is equal to "0"    
                        elif listOfInputs[i][j] != "0":
                            flag3 = True    

                #conditional statement which evaluates to True if the function validDate returns True
                if dateObject.validDate(int(month), int(day), int(year)) == True:
                    #setting month, day, and year to instance of date and appending this instance to list called dates
                    dateObject.setter(int(month), int(day), int(year))
                    dates.append(dateObject)

                    flag = True

                #conditional statement which evaluates to True if the conditional statement above evaluates to False    
                else:
                    print("Invalid date. Try again.")

            #conditional statement which evaluates to True if the conditional statement above evaluates to False
            else:
                print("Invalid date. Try again.") 

        #conditional statement which evaluates to True if the conditional statement above evaluates to False
        else:
            print("Invalid date. Try again.")      

        #resetting some local variables for next time the while loop runs
        flag2 = False
        month = day = year = ""
        numBackSlashes = 0
