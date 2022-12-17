# This is the greeting message.
greeting = "Hi! This is a program for lists.\nPlease enter a number for one of the following options:"

# The options the user will be presented with.
options = ["View Lists", "Create List", "Modify Lists"]

def appmenu():  #prints the app menu - defined as a func. so it can be called when needed.
    for index, i in enumerate(options):
        print(str(index +1) + ". " + i)
def linebreak():
    print("-----\n")

print(greeting) #Prints the greeting, then lists the options with appropriate option number.

# MENU
appmenu()
linebreak()
choice = str(input())

menuopen = 0

while menuopen < 1:
    if choice == "1":
        menuopen = 1
        print(choice)
    elif choice == "2":
        menuopen = 1
        print(choice)    
    elif choice == "3":
        menuopen = 1 
        print(choice)
    else:
        print("Please only enter numerical numbers (Such as 1, 2 or 3)")
        appmenu()
        choice = str(input())