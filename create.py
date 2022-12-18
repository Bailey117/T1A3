# Contains functions to create a list 
def listmenu():
    typeoptions = ["To-Do", "Groceries", "Birthdays"]
    for index, i in enumerate(typeoptions):
        print(str(index +1) + ". " + i)

def createlist():
    print("You've chosen to CREATE a list.\nIf you would like to return to menu, enter 'menu' input at any time.")
    listname = str(input("Enter the name of your list.")).lower() + ".txt"

    loop = 0 #set to 1 to bypass this stage for testing
    while loop < 1:

        import os
        path = os.path.relpath("lists/" + listname)   #this checks if a file in path lists already exists with the desired list name. If it does, it asks if user wants to overwrite.
        fcheck = os.path.exists(path)

        if(fcheck):
            owloop = 0
            while owloop < 1:
                overwrite = input("A file with this name already exists. Do you wish to overwrite it? (y/n)\nNote: this CANNOT be UNDONE.").lower()
                if overwrite == "y":
                    os.remove(path)
                    f = open(os.path.relpath("lists/" + listname), 'w')
                    owloop = 1
                    loop = 1
                elif overwrite == "n":
                    listname = str(input("Enter the name of your list.")).lower() + ".txt"
                    owloop = 1
                    fcheck = ""
                else: 
                    print("You have inputted your answer incorrectly. Please only use the letters 'y' or 'n' to indicate yes/no.")
        else:
            print("False")
            f = open(os.path.relpath("lists/" + listname), 'w')
            loop = 1

    print("What kind of list would you like to make?")
    listmenu()
    listtype = str(input())


    lstypeloop = 0
    while lstypeloop < 1:
        if listtype == "1": #To-Do List                     print(listname[:len(listname) - 4]) for name - txt capitalize()
            lstypeloop = 1
            print("Creating To-Do List named '" + listname[:len(listname)-4].capitalize() + "'\n")
            f.write('#' + listname[:len(listname)-4].capitalize() + '\n')

        ########
        if listtype == "2": #Groceries List
            lstypeloop = 1
            print(listtype)

        ########
        if listtype == "3": #Birthdays List
            lstypeloop = 1
            print(listtype)

def todolist():
    print("todo")
def grocerylist():
    print("shop")
def birthdaylist():
    print("bday")