def chooselist():
    import os
    dirpath = './lists/'
    chooselist.listdir = []
    for path in os.listdir(dirpath):
        if os.path.isfile(os.path.join(dirpath, path)):
            chooselist.listdir.append(path[:len(path) - 3])
    print("Please choose the number corresponding to the list you would like to view.")
    chooselist.dirlength = 1
    for index, i in enumerate(chooselist.listdir):
        print(str(index +1) + ". " + i.capitalize())
        chooselist.dirlength += 1
    chooselist.chosenlist = input()
    chooseloop = 0
    while chooseloop < 1:   
        if int(chooselist.chosenlist) in range(1, chooselist.dirlength):
            chooseloop = 1
            chooselist.chosenpath = chooselist.listdir[int(chooselist.chosenlist)-1] + ".md"
            openlist()
            printloop = 0
            while printloop < 1:
                printquery = input("Would you like to convert this to a PDF? (y/n)").lower()
                if printquery =="y":
                    printlist()
                    printloop = 1
                    import userinterface as ui
                    ui.menuopen = 0
                    return
                elif printquery == "n":
                    printloop = 1
                    import userinterface as ui
                    ui.menuopen = 0
                    return
                else: 
                    input("Please only use 'y' or 'n' to indicate yes or no. Would you like to convert this list to a PDF?")
        else:
            print("\n------\nPlease only enter a numeric value (Such as 1, 2, or 3)")
            for index, i in enumerate(chooselist.listdir):
                print(str(index +1) + ". " + i.capitalize())
            chooselist.chosenlist = input()


def openlist():
    print("------\nOpening " + chooselist.listdir[int(chooselist.chosenlist)-1].capitalize() + " List\n")
    import os
    f = open(os.path.relpath("lists/" + chooselist.chosenpath), 'r')
    for line in f:
        lineprint = line.replace("#", "").replace("*", "-")
        print(lineprint)
    f.close()

def printlist():
    import aspose.words as aw
    doc = aw.Document("lists/" + chooselist.chosenpath)
    doc.save("lists/" + chooselist.chosenpath[:len(chooselist.chosenpath)-3] + ".pdf")
    print("You've saved the file as " + chooselist.chosenpath[:len(chooselist.chosenpath)-3] + ".pdf")


