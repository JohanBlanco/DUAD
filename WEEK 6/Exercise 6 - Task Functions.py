
# 1. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def number_of_cases(string):
    upper_case_list =  [char for char in string if char.isupper() and len(char.strip()) != 0]
    lower_case_list =  [char for char in string if char.islower() and len(char.strip()) != 0]
    print(f'There’s {len(upper_case_list)} upper cases and {len(lower_case_list)} lower cases')

number_of_cases("I love Nación Sushi")
