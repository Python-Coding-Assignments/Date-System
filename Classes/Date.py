import string
from datetime import date

class Date:
    """Class definition for Date"""

    #declaration and initialization of class variable
    formatType = "D"

    def __init__(self, *arguments):
        """Constructor that instantiates an instance of Date"""

        #conditional statement which evaluates to True if the number of arbitrary arguments passed to the constructor is equal to zero
        if len(arguments) == 0:
            self.__month = 1
            self.__day = 1
            self.__year = 2000

        #conditional statement which evaluates to True if the number of arbitrary arguments passed to the constructor is equal to three    
        elif len(arguments) == 3:   
            #conditional statement which evaluates to True if the new instance of Date is an actual date
            if self.validDate(arguments[0], arguments[1], arguments[2]) == True:
                self.__month = arguments[0]
                self.__day = arguments[1]
                self.__year = arguments[2]

            #conditional statement which evaluates to True if the new instance of date is not a valid date    
            else:
                self.__month = 1
                self.__day = 1
                self.__year = 2000    

    def setter(self, month, day, year):
        """This instance method is a setter that sets the private instance variables month, day, and year to a value.  This method takes in three additional parameters: month, day, and year"""

        #conditional statement which evaluates to True if the date being passed to the setter is valid
        if self.validDate(month, day, year) == True:
            self.__month = month
            self.__day = day
            self.__year = year

        #conditional statement which evaluates to True if the conditional statement above evaluates to False    
        else:
            self.__month = 1
            self.__day = 1
            self.__year = 2000   

    def getMonth(self):
        """This instance method is a getter which returns the private member attribute month"""

        return self.__month

    def getDay(self):
        """This instance method is a getter which returns the private member attribute day"""

        return self.__day

    def getYear(self):
        """This instance method is a getter which returns the private member attribute year"""

        return self.__year         

    def show(self):
        """This instance method displays the instance's attributes to the screen in a specified format"""

        #declaration and initialization of local variables
        strMonth = strDay = strYear = returnStr = ""
        totalDays = 0
        dictionary = {1: "Jan ", 2: "Feb ", 3: "Mar ", 4: "Apr ", 5: "May ", 6: "June ", 7: "July ", 8: "Aug ", 9: "Sep ", 10: "Oct ", 11: "Nov ", 12: "Dec "}
        dictionary2 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        #conditional statement which evaluates to True if the class variable formatType is equal to "D"
        if Date.formatType == "D":
            returnStr = str(self.__month) + "/" + str(self.__day) + "/" + str(self.__year)

        #conditional statement which evaluates to True if the class variable formatType is equal to "T"    
        elif Date.formatType == "T":
            #converting instance variables of type integer to type string
            strMonth = str(self.__month)
            strDay = str(self.__day)
            strYear = str(self.__year)

            #conditional statement which checks if the length of the string strMonth is equal to one
            if len(strMonth) == 1:
                strMonth = "0" + strMonth

            #conditional statement which checks if the length of the string strDay is equal to one    
            if len(strDay) == 1:
                strDay = "0" + strDay    

            #conditional statement which checks if the length of the string strYear is equal to one
            if len(strYear) == 1:
                strYear = "0" + strYear

            #conditional statement which checks if the length of the string strYear is greater than two    
            elif len(strYear) > 2:
                strYear = strYear[2:]     

            returnStr = strMonth + "/" + strDay + "/" + strYear

        #conditional statement which evaluates to True if the class variable formatType is equal to "L"    
        elif Date.formatType == "L":
            #for loop which iterates over each key-value pair of the dictionary
            for key, value in dictionary.items():
                #conditional statement which checks if the predefined key within the dictionary is equal to the instance's private attribute called month
                if key == self.__month:
                    strMonth = value       

            returnStr = strMonth + str(self.__day) + ", " + str(self.__year)

        #conditional statement which evaluates to True if the class variable formatType is equal to "J"
        elif Date.formatType == "J":
            #re-initialization of strYear variable
            strYear = str(self.__year)

            #conditional statement which evaluates to True if the length of strYear is equal to one
            if len(strYear) == 1:
                strYear = "0" + strYear

            #slicing string
            strYear = strYear[-2:]

            #for loop which iterates over each key-value pair within dictionary2
            for key, value in dictionary2.items():
                #conditional statement which evaluates to True if self.__month is greater than key
                if self.__month > key:
                    totalDays += value

                #conditional statement which evaluates to True if self.__month is equal to key    
                elif key == self.__month:
                    totalDays += self.__day
                    
                    #conditional statement which evaluates to True if the following conditions are met
                    if ((self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0) and ((self.__month == 2 and self.__day == 29) or self.__month > 2):
                        self.__day += 1    

            #converting totalDays from type integer to type string
            totalDays = str(totalDays)  

            #conditional statement which evaluates to True if the length of totalDays is equal to one 
            if len(totalDays) == 1:
                totalDays = "00" + totalDays

            #conditional statement which evaluates to True if the length of totalDays is equal to two    
            elif len(totalDays) == 2:
                totalDays = "0" + totalDays 

            returnStr = strYear + "-" + totalDays

        #returning returnStr
        return returnStr       

    def increment(self):
        """This instance method increments the instance's date by a specified number of days"""

        #declaration and initialization of local variables
        value = ""
        flag = flag2 = False

        #while loop which runs while flag is False
        while flag == False:
            #getting value from user
            value = input("How much would you like to increment " + self.show() + " by (in days)?: ")
            
            #for loop which iterates over each integer starting from zero, inclusive, to the length of the user's string input called value, exclusive
            for i in range(0, len(value)):
                #conditional statement which evaluates to True if value's character at index i is not contained within the predefined string called string.digits
                if value[i] not in string.digits:
                    flag2 = True

            #conditional statement which evaluates to True if flag2 is False
            if flag2 == False:
                #converting value from type string to type integer
                value = int(value)

                #conditional statement which evaluates to True if value is greater than zero
                if value > 0:
                    flag = True

            flag2 = False                

        print(self.show() + " incremented by " + str(value) + " days!")
        
        #for loop which iterates over the integers between zero, inclusive, and the integer value, exclusive
        for i in range(0, value):
            #conditional statement which evaluates to True if the following conditions are met
            if (self.__month == 1 or self.__month == 3 or self.__month == 5 or self.__month == 7 or self.__month == 8 or self.__month == 10 or self.__month == 12) and self.__day < 31:
                self.__day += 1

            #conditional statement which evaluates to True if the following conditions are met    
            elif (self.__month == 4 or self.__month == 6 or self.__month == 9 or self.__month == 11) and self.__day < 30:      
                self.__day += 1

            #conditional statement which evaluates to True if the following conditions are met    
            elif self.__month == 2:
                #conditional statement which evaluates to True if the following conditions are met
                if ((self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0) and self.__day < 29:
                    self.__day += 1

                #conditional statement which evaluates to True if the private instance variable called day is less than 28    
                elif self.__day < 28:    
                    self.__day += 1  

                #conditional statement which evaluates to True if the above conditional statements evaluate to False    
                else:
                    self.__month += 1
                    self.__day = 1
            
            #conditional statement which evaluates to True if none of the conditional statements above evaluate to False
            else:
                #conditional statement which evaluates to True the instance variable month is equal to twelve
                if self.__month == 12:
                    self.__year += 1
                    self.__month = 1

                #conditional statement which evaluates to True if the instance variable month does not equal twelve    
                else:
                    self.__month += 1 

                self.__day = 1                             

    def compare(self, other):
        """This instance method compares two instances of type Date.  The method's call takes in one additional argument called other which is simply an instance of Date"""

        #declaration and initialization of local variables
        difference = 0
        date1 = date(self.__year, self.__month, self.__day)
        date2 = date(other.__year, other.__month, other.__day)

        difference = date1 - date2

        #conditional statement which evaluates to True if the difference between both dates is greater than one
        if difference.days > 1:
            print(self.show() + " and " + other.show() + " are " + str(difference.days) + " days apart.")

        #conditional statement which evaluates to True if the difference between both dates is equal to one
        elif difference.days == 1:
            print(self.show() + " and " + other.show() + " are " + str(difference.days) + " day apart.")

        #conditional statement which evaluates to True if both dates are the same
        elif difference.days == 0:
            print("Both of these dates are the same!")

        #conditional statement which evaluates to True if the difference between both dates is equal to negative one
        elif difference.days == -1:
            print(self.show() + " and " + other.show() + " are " + str(difference.days) + " day apart.")

        #conditional statement which evaluates to True if the difference between both dates is less than negative one    
        else:
            print(self.show() + " and " + other.show() + " are " + str(abs(difference.days)) + " days apart.")

    def __ge__(self, other):
        """This instance method overloads the greater than or equal to operator so that it can support two variables of type Date.  This method takes in one additional parameter called other which is of type Date"""

        #declaration and initialization of local variable
        flag = False

        #conditional statement which evaluates to True if self's value for year is greater than other's value for year
        if self.__year > other.__year:
            flag = True

        #conditional statement which evaluates to True if self's value for year is equal to other's value for year    
        elif self.__year == other.__year:
            ##conditional statement which evaluates to True if self's value for month is greater than other's value for month
            if self.__month > other.__month:
                flag = True

            #conditional statement which evaluates to True if self's value for month is equal to other's value for month    
            elif self.__month == other.__month:
                #conditional statement which evaluates to True if self's value for day is greater than or equal to other's value for day
                if self.__day >= other.__day:
                    flag = True
                
                #conditional statement which evaluates to True if self's value for day is less than other's value for day
                else:
                    flag = False   
            
            #conditional statement which evaluates to True if self's value for month is less than other's value for month
            else:
                flag = False
        
        #conditional statement which evaluates to True if self's value for year is less than other's value for year
        else:
            flag = False

        #returning flag
        return flag                            

    @classmethod
    def setFormat(cls):
        """This class method sets the format for which the dates should be displayed"""

        #declaration and initialization of local variable
        flag = False

        #printing menu to the screen
        print("--------------------------------------------")
        print("|   Name          Format         Example   |")
        print("|  Default        M/D/Y         10/4/1998  |") 
        print("| Two-Digit      mm/dd/yy       10/04/98   |")
        print("|   Long        month D, Y     Oct 4, 1998 |")
        print("|  Julian         yy-jdd         98-278    |") 
        print("--------------------------------------------")  
        print("Enter either D, T, or L when prompted for your selection.")
        print("------------------------")
        print("| D - Default format   |")
        print("| T - Two-Digit format |")
        print("| L - Long format      |")
        print("| J - Julian format    |")
        print("------------------------")

        #while loop which runs while flag is False
        while flag == False:
            #getting format type from user
            cls.formatType = input("Selection > ")

            #conditional statement which evaluates to True if user's input is equal to either "D", "T", "L", or "J"
            if cls.formatType == "D" or cls.formatType == "T" or cls.formatType == "L" or cls.formatType == "J":
                flag = True    

    @staticmethod
    def validDate(month, day, year):
        """This static method validates whether the instance's private instance variables are valid.  The method then returns a boolean value where True represents a valid date and False represents an invalid date"""

        #declaration and initialization of local variable
        flag = True

        #conditional statement which evaluates to True if the following conditions are met
        if (month > 0 and month < 13) and year >= 0:
            #conditional statement which evaluates to True if the following conditions are met
            if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 1 or day > 31):     
                flag = False

            #conditional statement which evaluates to True if the following conditions are met    
            elif (month == 4 or month == 6 or month == 9 or month == 11) and (day < 1 or day > 30):
                flag = False 

            #conditional statement which evaluates to True if month is equal to two    
            elif month == 2:
                #conditional statement which evaluates to True if the following conditions are met
                if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and (day < 1 or day > 29):
                    flag = False

                #conditional statement which evaluates to True if the following conditions are met    
                elif not((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and (day < 1 or day > 28):    
                    flag = False     
        
        #conditional statement which evaluates to True if the previous condition evaluates to False    
        else:
            flag = False     

        #returning flag
        return flag        