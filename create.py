# Contains functions to create a list 
def listmenu():
    typeoptions = ["To-Do", "Groceries", "Birthdays"]
    for index, i in enumerate(typeoptions):
        print(str(index +1) + ". " + i)

def createlist():
    print("You've chosen to CREATE a list.\nIf you would like to return to menu, enter 'menu' input at any time.")
    createlist.listname = str(input("Enter the name of your list.")).lower() + ".md"

    loop = 0 #set to 1 to bypass this stage for testing
    while loop < 1:

        import os
        path = os.path.relpath("lists/" + createlist.listname)   #this checks if a file in path lists already exists with the desired list name. If it does, it asks if user wants to overwrite.
        fcheck = os.path.exists(path)

        if(fcheck):
            owloop = 0
            while owloop < 1:
                overwrite = input("A file with this name already exists. Do you wish to overwrite it? (y/n)\nNote: this CANNOT be UNDONE.").lower()
                if overwrite == "y":
                    os.remove(path)
                    f = open(os.path.relpath("lists/" + createlist.listname), 'w')
                    f.write('# ' + createlist.listname[:len(createlist.listname)-3].capitalize() + '\n ')
                    f.close()
                    owloop = 1
                    loop = 1
                elif overwrite == "n":
                    createlist.listname = str(input("Enter the name of your list.")).lower() + ".md"
                    owloop = 1
                    fcheck = ""
                else: 
                    print("You have inputted your answer incorrectly. Please only use the letters 'y' or 'n' to indicate yes/no.")
        else:
            print("False")
            f = open(os.path.relpath("lists/" + createlist.listname), 'w')
            f.write('# ' + createlist.listname[:len(createlist.listname)-3].capitalize() + '\n ')
            f.close()
            loop = 1

    print("What kind of list would you like to make?")
    listmenu()
    listtype = str(input())


    createlist.lstypeloop = 0
    while createlist.lstypeloop < 1:
        if listtype == "1": #To-Do List                     print(createlist.listname[:len(createlist.listname) - 4]) for name - txt capitalize()
            createlist.lstypeloop = 1
            print("Creating To-Do List named '" + createlist.listname[:len(createlist.listname)-3].capitalize() + "'\n")
            todolist()

        ########
        elif listtype == "2": #Groceries List
            createlist.lstypeloop = 1
            print("Creating Shopping List named '" + createlist.listname[:len(createlist.listname)-3].capitalize() + "'\n")
            grocerylist()

        ########
        elif listtype == "3": #Birthdays List
            createlist.lstypeloop = 1
            print("Creating Birthdays List named '" + createlist.listname[:len(createlist.listname)-3].capitalize() + "'\n")
            birthdaylist()
        else:
            print("Please enter only numerical values (Such as 1, 2, or 3)")
            listmenu()
            listtype = str(input())

def todolist():
    import os
    f = open(os.path.relpath("lists/" + createlist.listname), 'a')
    listlen = input("How many tasks would you like to have on the list? (Numerical Value)")
    while listlen.isdigit() == 0:
        listlen = input("Please only use numerical values (such as 1, 2, 3) for the length.")
    listlen = int(listlen)
    for i in range(listlen):
        f.write("\n* " + input("What task would you like to add?") + "  ")
    lsdone = 0
    while lsdone <1:
        listlen = input("If you would like to add more items, please enter the number you would like to add.\nOtherwise, please input 'exit' to the cmd line.")
        if listlen.isdigit() == 1:
            listlen = int(listlen)
            for i in range(listlen):
                f.write("\n* " + input("What task would you like to add?") + "  ")
        elif listlen.lower() == "exit":
            createlist.lstypeloop = 1
            f.close()
            import userinterface as ui
            ui.menuopen = 0
            return
        else:
            print("You have entered an invalid input. Please use only numerica values or 'exit'.")
       
def grocerylist():
    import os
    f = open(os.path.relpath("lists/" + createlist.listname), 'a')
    listlen = input("How many items would you like to have on the list? (Numerical Value)")
    while listlen.isdigit() == 0:
        listlen = input("Please only use numerical values (such as 1, 2, 3) for the length.")
    listlen = int(listlen)
    for i in range(listlen):
        f.write("\n* " + input("What item would you like to add?") + " -- $" + input("How much does this item cost?"))
    lsdone = 0
    while lsdone <1:
        listlen = input("If you would like to add more items, please enter the number you would like to add.\nOtherwise, please input 'exit' to the cmd line.")
        if listlen.isdigit() == 1:
            listlen = int(listlen)
            for i in range(listlen):
                f.write("\n* " + input("What item would you like to add?") + " -- $" + input("How much does this item cost?"))
        elif listlen.lower() == "exit":
            createlist.lstypeloop = 1
            f.close()
            import userinterface as ui
            ui.menuopen = 0
            return
        else:
            print("You have entered an invalid input. Please use only numerica values or 'exit'.")
    
def birthdaylist():
    import os
    f = open(os.path.relpath("lists/" + createlist.listname), 'a')
    listlen = input("How many birthdays would you like to have on the list? (Numerical Value)")
    while listlen.isdigit() == 0:
        listlen = input("Please only use numerical values (such as 1, 2, 3) for the length.")
    listlen = int(listlen)
    for i in range(listlen):
        f.write("\n* " + input("Please enter the person's name") + " -- " + input("And what is their birth date?"))
    lsdone = 0
    while lsdone <1:
        listlen = input("If you would like to add more birthdays, please enter the number you would like to add.\nOtherwise, please input 'exit' to the cmd line.")
        if listlen.isdigit() == 1:
            listlen = int(listlen)
            for i in range(listlen):
                f.write("\n* " + input("Please enter the person's name") + " -- " + input("And what is their birth date?"))
        elif listlen.lower() == "exit":
            createlist.lstypeloop = 1
            f.close()
            import userinterface as ui
            ui.menuopen = 0
            return
        else:
            print("You have entered an invalid input. Please use only numerica values or 'exit'.")   