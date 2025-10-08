# Contans the logic for the menu
import os
import time

def pause(seconds):
    time.sleep(seconds)

def clearScreen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux or macOS
    else:
        os.system('clear')


def displayMainMenu():
    clearScreen()
    menu = """
                        Menu
        1. Register a Student.
        2. List all students.
        3. List The Top 3 Best Avarge Students
        4. Show the avaragre of all students avarge
        5. Export Data to Csv
        6. Import Data from previous exported Csv
        7. Exit
    
    """
    try:
        option = int(input("Select an option: "))
        if 0 < option < 8:
            raise ValueError
    except ValueError as valueError:
        print("The value must be an option from [1,7] both inclusive")
