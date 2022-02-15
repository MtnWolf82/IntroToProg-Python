# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# TFarmer,2.13.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
print ("<<<Using a List of Dictionary Objects>>>")
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")  #Split then returns a list object
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
    print(lstTable) #Displays a list with dictionary objects
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current file tasks.
    2) Add a new task.
    3) Remove an existing task.
    4) Save data to the file.
    5) Exit the program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current file tasks in the table
    if (strChoice.strip() == "1"):
        objFile = open("ToDoList.txt", "r")
        for row in objFile:
            lstRow = row.split(",") #Split then returns a list object
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            print(dicRow)
        objFile.close()

    # Step 4 - Add a new task to the list/Table
    elif (strChoice.strip() == "2"):
        while(True):
            task = input("Enter your task: ")
            priority = input("What is the priority of your task? ")
            lstTable.append({"Task": task, "Priority": priority})
            strChoice = input("Exit ('y/n'): ")
            if strChoice.lower() == "y":
                break
        print(lstTable, "<-- List of Dictionary Objects>>>")

    # Step 5 - Remove a new task from the list/Table
    elif (strChoice.strip() == "3"):
        while(True):
            task = input("Task to remove: ")
            for row in lstTable:
                if row["Task"].lower() == task.lower():
                    lstTable.remove(row)
                    print("Task removed.")
                    print(lstTable, "<-- List of Dictionary Objects>>>")
                else:
                    print("Task not found.")
                    print(lstTable, "<-- List of Dictionary Objects>>>")
            strChoice = input("Exit ('y/n'): ")
            if strChoice.lower() == "y":
                break
        print(lstTable, "<-- List of Dictionary Objects>>>")

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == "4"):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("File has been updated.")

    # Step 7 - Exit program
    elif (strChoice.strip() == "5"):
        break  # and Exit the program