# Contans the logic for the menu
import os
import time

def wait(seconds):
    time.sleep(seconds)

def pause():
    input("\nPress any key to continue...")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux or macOS
    else:
        os.system('clear')

def loading_data():
    print("Loading the data from previous exported")

def request_grade(message):
    grade = 0
    while True:
        try:
            grade = float(input(message))
            if not (0 <= grade <= 100):
                raise ValueError
            return grade
        except ValueError:
            print("""
                
                WARNING
                The grade must be a value from [0,100] both inclusive
                
            """)


def display_main_menu():
    try_again = True
    while try_again:
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
        clear_screen()
        print(menu)
        try:
            option = int(input("Select an option: "))
            if not (0 < option < 8):
                raise ValueError
            try_again = False
        except ValueError as valueError:
            print("""
                
                WARNING
                The value must be an option from [1,7] both inclusive
                
            """)
            wait(3)
    return option

def register_student():
    menu = """
                New Student Registration
    """
    clear_screen()
    print(menu)

    full_name = input("Full Name: ")
    section = input("Section: ")
    grade_in_spanish = request_grade("Grade in Spanish: ")
    grade_in_english = request_grade("Grade in English: ")
    grade_in_social_studies= request_grade("Grade in Social Studies: ")
    grade_in_science = request_grade("Grade in Science: ")

    student_info = {
        "Full Name": full_name,
        "Section": section,
        "Grade in Spanish": grade_in_spanish,
        "Grade in English": grade_in_english,
        "Grade in Science": grade_in_science,
        "Grade in Social Studies": grade_in_social_studies
    }

    return student_info

def display_all_students(student_list):
    menu = """
                List of Students
    """
    clear_screen()
    print(menu)

    print(f"{'Full Name':<20} {'Section':<8} {'Spanish':<8} {'English':<8} {'Science':<8} {'Social Studies':<15}")
    print("-" * 90)

    for student_info in student_list:
        print(f"{student_info['Full Name']:<20} {student_info['Section']:<8} {student_info['Grade in Spanish']:<8} {student_info['Grade in English']:<8} {student_info['Grade in Science']:<8} {student_info['Grade in Social Studies']:<15}")

    pause()


def display_top_3_students(student_list):
    menu = """
            TOP 3 BEST STUDENTS AVARGE
    """
    clear_screen()
    print(menu)

    print(f"{'Full Name':<20} {'Section':<8} {'Avarage':<8}")
    print("-" * 40)

    for student_info in student_list:
        print(f"{student_info['Full Name']:<20} {student_info['Section']:<8} {student_info['Avarage']:<8}")

    pause()

def display_avarage_of_all_avarage(avarage):
    menu = """
            AVARGE FROM ALL STUDENTS AVARAGE
    """
    clear_screen()
    print(menu)

    print(f"{'Avarage':<8}")
    print("-" * 20)
    print(avarage)

    pause()