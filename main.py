from Functions import implementation, menu, menu1

#declaration and initialization of variables
dates = []
userInput = ""

#welcoming user to application
print("Welcome to the Date Application!\nBegin by creating a date.\n")

#calling menu1 and menu functions
menu1(dates)
print()
menu()

#while loop which runs until the value of userInput is equal to the string "7"
while userInput != "7":
    #getting user input from user
    userInput = input("\nMenu Selection: ")
    
    #calling implementation function
    implementation(userInput, dates)