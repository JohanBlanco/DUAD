
# 1. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.
# </aside>



average = 0
average_passed = 0
average_failed = 0
count_passed = 0
count_failed = 0

grades = [70, 85, 90, 100, 60, 50]

for grade in grades:
    if grade >= 70:
        count_passed += 1
        average_passed += grade
    else:
        count_failed += 1
        average_failed += grade
    average += grade

if(count_passed):
    average_passed = average_passed / count_passed
    print(f"Passed Grades Average:  {average_passed}")
else:
    print("It is not possible to calculate the average of passed grades, because its ammount is 0")

if(count_failed):
    average_failed = average_failed / count_failed
    print(f"Failed Grades Average:  {average_failed}")
else:
    print("It is not possible to calculate the average of failed grades, , because its ammount is 0")

if(len(grades)):
    average = average / len(grades)
    print(f"Average:  {average}")
else:
    print("It is not possible to calculate the average, because the ammount of grades provided is 0")
