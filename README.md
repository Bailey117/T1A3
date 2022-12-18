# T1A3-Assignment

[Github Repository](https://github.com/Bailey117/T1A3)  
[Presentation Video](https://youtu.be/b6Z_hWe0z5w)

## Code Style
Throughout my coding, I did my best to adopt the "Zen of Python" coding style, avoiding repitition where possible and attempting to make the code as simple and explicit as possible. 

## Features
### **Create List**
The application allows users to choose a type of list - the options being 'To-Do List', 'Grocery List', and 'Birthday Dates' - and input a custom number of items to the list. 

They are able to set the list's name, which is then created as a markdown file, and can add items relevant to each list.

- To-Do List -- The to do list has a simple list, where the user inputs each task.
- Grocery List -- The user is able to input each shopping item, and an associated price. 
- Birthday Dates -- The user can input as many names as they would like, and attach a birth date to each name.

### **View Lists**
The user is able to view any created lists in the terminal.  
The program removes all markdown coding formats and prints only the key information - This being the title of the list and each relevant item points. This is all neatly displayed in the terminal.  

### **Conversion to PDF**
The program also allows its users to save their lists as a Markdown PDF. 

They can view the file through the terminal, as previously mentioned, and then if desired choose to save the document as a PDF. This will expert the list as a PDF file so they can save it, print it out and use it where they wish.
## Setup Guide
This program should be quite easy to run.

All you need to do is the following:
1. Clone the repository to a desired destination.
2. Open the folder the program is stored in in your favourite terminal app.
3. Input ```./listwrapper.sh``` into the command line. 
4. Ta-dah! The program has been begun.

## How to Use
Once the program has been set up and is running, you will be prompted with a menu that should look something like this - note that all menu interactions function the same: 
```
1. View List
2. Create List
3. Exit Program
```

Simply input the relevant numerical value (such as '1' or '2') andd press enter - and you will be taken to the relevant area.

### Writing Lists
To write a list, go to the Create List section. Once there, you simply select a list type as per the menu guide above, then enter each item in the list as relevant.



## Information Sources:
Aspose - https://pypi.org/project/aspose-words/
Zen of Python  - https://github.com/python/peps/blob/main/pep-0020.txt