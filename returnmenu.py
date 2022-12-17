def returntomenu():
    print("Returning you to the menu..\n----\n")
    loop = 1
    import userinterface as ui
    ui.menuopen = 0
    ui.choice = str(input())
    return