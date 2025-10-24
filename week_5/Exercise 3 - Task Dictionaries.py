# 1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#     1. Ejemplos:
#     2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#     `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#     → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`


person = {}

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

for index in range(len(list_a)):
    key = list_a[index]
    value = list_b[index]
    person[key] = value

print(person)