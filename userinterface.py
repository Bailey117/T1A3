# This is the greeting message.
greeting = "\nHi! This is a program for lists.\nPlease enter a number for one of the following options:"

# The options the user will be presented with.
options = ["View Lists", "Create List", "Exit Program"]

def appmenu():  #prints the app menu - defined as a func. so it can be called when needed.
    for index, i in enumerate(options):
        print(str(index +1) + ". " + i)
def linebreak():
    print("-----\n")

print(greeting) #Prints the greeting, then lists the options with appropriate option number.

# MENU
linebreak()
appmenu()
linebreak()
choice = str(input())

menuopen = 0

while menuopen < 1:
    if choice == "1": #View List
        menuopen = 1
        import view
        view.chooselist()
    elif choice == "2": #Create List
        menuopen = 1
        import create
        create.createlist()   
    elif choice =="3": #Exit Program
        print("Exiting Program...")
        menuopen = 1 
        break
    else:
        print("Please only enter numerical numbers (Such as 1, 2 or 3)")
        appmenu()
        choice = str(input())