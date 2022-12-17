# Contains functions to create a list 

def createlist():
    print("You've chosen to CREATE a list.\nIf you would like to return to menu, enter 'menu' and input at any time.")
    listname = str(input("Enter the name of your list.")).lower() + ".txt"

    loop = 0
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
                    print("You have inputted your answer incorrectly. Please only use the letters y or n to indicate yes/no.")

        else:
            print("False")
            f = open(os.path.relpath("lists/" + listname), 'w')
            loop = 1


createlist()
