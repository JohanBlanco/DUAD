# Contans the logic for the actions, except the import and export
import menu
import data
import os
from Student import Student

def register_student(student_list):
    new_student = menu.register_student()
    student_list.append(new_student)

def list_all_students(student_list):
    if len(student_list) > 0:
        menu.display_all_students(student_list)
    else:
        menu.display_message('WARNING', 'There are 0 students in the system yet', do_pause=True)

def list_top_3_students(student_list):
    if len(student_list) > 0:
        sorted_list = student_list.copy()
        sorted_list.sort(key=lambda student: student.get_average(), reverse=True)
        top_3 = sorted_list[:3]
        menu.display_top_3_students(top_3)
    else:
        menu.display_message('WARNING', 'There are 0 students in the system yet', do_pause=True)

def show_average_from_all_students(student_list):
    if len(student_list) > 0:
        all_average_list = [student.get_average() for student in student_list]
        average = sum(all_average_list) / len(student_list)
        menu.display_average_of_all_average(average)
    else:
        menu.display_message('WARNING', 'There are 0 students in the system yet', do_pause=True)

def convert_students_to_dictionaries(student_list):
    dictionary_list = []

    for student in student_list:
        dictionary = student.to_dict()
        dictionary_list.append(dictionary)

    return dictionary_list

def convert_dictionaries_to_students(dictionary_list):
    student_list = []

    for dictionary in dictionary_list:
        student = Student.from_dict(dictionary)
        student_list.append(student)

    return student_list

def store_data_in_csv(student_list, csv_file_path, headers):
    dictionary_list = convert_students_to_dictionaries(student_list)

    if len(student_list) > 0:
        data.write_csv_file(file_path=csv_file_path, data=dictionary_list, headers=headers)
        menu.display_message('INFO', 'Data exported successfully to students.csv file', do_pause=True)
    else:
        menu.display_message('WARNING', 'There are 0 students in the system yet', do_pause=True)

def load_data_from_csv(csv_file_path):
    if not os.path.exists(csv_file_path):
        menu.display_message('WARNING', 'There is no previously exported data', do_pause=True)
        return []

    dictionary_list = data.read_csv_file(csv_file_path)
    student_list = convert_dictionaries_to_students(dictionary_list)

    for student in student_list:
        student.grade_in_spanish = float(student.grade_in_spanish)
        student.grade_in_english = float(student.grade_in_english)
        student.grade_in_science = float(student.grade_in_science)
        student.grade_in_social_studies = float(student.grade_in_social_studies)

    if len(student_list) > 0:
        menu.display_message('INFO', 'Data successfully loaded from students.csv file', do_pause=True)
    else:
        menu.display_message('WARNING', 'There is no previously exported data', do_pause=True)

    return student_list

def execute():
    file_path = 'Week 11/Exercise 3/students.csv'
    headers = ['full_name', 'section', 'grade_in_spanish', 'grade_in_english', 'grade_in_science', 'grade_in_social_studies']
    student_list = []

    try:
        while True:
            try:
                option = menu.display_main_menu()

                if option == 1:
                    register_student(student_list)
                elif option == 2:
                    list_all_students(student_list)
                elif option == 3:
                    list_top_3_students(student_list)
                elif option == 4:
                    show_average_from_all_students(student_list)
                elif option == 5:
                    store_data_in_csv(student_list, file_path, headers)
                elif option == 6:
                    student_list = load_data_from_csv(file_path)
                elif option == 7:
                    break
            except KeyboardInterrupt:
                menu.display_message('INFO', 'Type 7 to exit', do_pause=True)
    except Exception as e:
        print("An error occurred:", e)
