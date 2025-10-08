
# 💪🏽 Ejercicios

## 1. Experimente haciendo sumas entre distintos tipos de datos

1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.  
   *Los errores son oportunidades de aprendizaje.*
2. Por ejemplo:
    - `string + string → ?`  
      **Respuesta:** Todo bien
    - `string + int → ?`  
      **Respuesta:** No se puede, solo se pueden concatenar 2 strings o sumar 2 enteros, por lo que hay que castear el int a un string con la función `str()`.
    - `int + string → ?`  
      **Respuesta:** No se puede, solo se pueden concatenar 2 strings o sumar 2 enteros, por lo que hay que castear el int a un string con la función `str()`.
    - `list + list → ?`  
      **Respuesta:** Concatena las listas en 1 sola
    - `string + list → ?`  
      **Respuesta:** No se puede, solo se pueden concatenar 2 strings o 2 listas.
    - `float + int → ?`  
      **Respuesta:** Todo bien
    - `bool + bool → ?`  
      **Respuesta:** Toma los True como 1 y los False como 0, y los suma

## 2. Programa que pide nombre, apellido y edad

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Determine category based on age
if age < 3:
    category = "baby"
elif age < 8:
    category = "child"
elif age < 12:
    category = "preteen"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
elif age < 65:
    category = "adult"
else:
    category = "senior"

print(category)
```

## 3. Programa con número secreto del 1 al 10

```python
import random

secret = random.randint(1, 10)
user_answer = 0

while secret != user_answer:
    user_answer = int(input("Guess the number from 1 to 10: "))
```

## 4. Programa que pide tres números y muestra el mayor

```python
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

largest = n3

if n1 >= n2 and n2 >= n3:
    largest = n1
elif n2 >= n1 and n1 >= n3:
    largest = n2

print(largest)
```

## 5. Calcular estadísticas de notas

```python
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
```

### Resolución en pseudocódigo

> Calcular notas
>
> 1. Inicio
> 2. Definir `total_de_notas`
> 3. Definir `contador_de_nota`
> 4. Definir `nota_actual`
> 5. Definir `cantidad_de_notas_aprobadas`
> 6. Definir `cantidad_de_notas_desaprobadas`
> 7. Definir `promedio_de_notas_aprobadas`
> 8. Definir `promedio_de_notas_desaprobadas`
> 9. Definir `promedio_de_notas_total`
> 10. `contador_de_nota` = 1
> 11. `cantidad_de_notas_aprobadas` = 0
> 12. `cantidad_de_notas_desaprobadas` = 0
> 13. `promedio_de_notas_aprobadas` = 0
> 14. `promedio_de_notas_desaprobadas` = 0
> 15. `promedio_de_notas_total` = 0
> 16. Mostrar “Ingrese la cantidad de notas”
> 17. Pedir `total_de_notas`
> 18. Mientras que (`contador_de_nota` ≤ `total_de_notas`) repetir:
>     1. Mostrar “Ingrese la nota numero"
>     2. Mostrar `contador_de_nota`
>     3. Pedir `nota_actual`
>     4. Si (`nota_actual`  < 70) entonces:
>         1. `cantidad_de_notas_desaprobadas` =  `cantidad_de_notas_desaprobadas` + 1
>         2. `promedio_de_notas_desaprobadas` = `promedio_de_notas_desaprobadas` + `nota_actual`
>     5. Sino:
>         1. `cantidad_de_notas_aprobadas` = `cantidad_de_notas_aprobadas` + 1
>         2. `promedio_de_notas_aprobadas` = `promedio_de_notas_aprobadas` + `nota_actual`
>     6. `promedio_de_notas_total` = `promedio_de_notas_total` + (`nota_actual` / `total_de_notas`)
> 19. FinMientras
> 20. `promedio_de_notas_desaprobadas` = `promedio_de_notas_desaprobadas` / `cantidad_de_notas_desaprobadas`
> 21. `promedio_de_notas_aprobadas` = `promedio_de_notas_aprobadas` / `cantidad_de_notas_aprobadas`
> 22. Mostrar “El estudiante tiene esta cantidad de notas aprobadas”
> 23. Mostrar `cantidad_de_notas_aprobadas`
> 24. Mostrar “Este es el promedio de notas aprobadas”
> 25. Mostrar `promedio_de_notas_aprobadas`
> 26. Mostrar “El estudiante tiene esta cantidad de notas desaprobadas”
> 27. Mostrar `cantidad_de_notas_desaprobadas`
> 28. Mostrar “Este es el promedio de notas desaprobadas”
> 29. Mostrar promedio`_de_notas_desaprobadas`
> 30. Mostrar “Este es el promedio total de notas”
> 31. Mostrar `promedio_de_notas_total`
> 32. Fin
