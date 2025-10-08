<aside>
💪🏽 **Ejercicios**

1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

```python
def sum_two_numbers(a,b):
    return a + b

def printSum(result):
    print(result)

printSum(sum_two_numbers(1,2))
```

1. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
        
        Respuesta: No es posible
        
        ```python
        def new_function():
            local_var = 10
        
        print(local_var)
        ```
        
    
    Traceback (most recent call last):
    File "c:\Users\blajo\OneDrive\Documentos\Python\[test.py](http://test.py/)", line 4, in <module>
    print(local_var)
    ^^^^^^^^^
    
    1. Intente accesar a una variable global desde una función y cambiar su valor.
        
        Respuesta: 
        
        Es necesario el uso de la palabra reservada global seguida del nombre de la variable global
        
        ```python
        global_var = 10
        
        def new_function():
            global global_var
            global_var = 50
        
        new_function()
        print(global_var)
        ```
        
2. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41

```python
def sum_list_numbers(my_list):
    sum = 0
    for num in my_list:
        sum += num
    return sum

my_list = [4, 6, 2, 29]
print(sum_list_numbers(my_list))
```

1. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”

```python
def revert_string(string):
    reverted = ""
    for index in range(len(string) -1, -1, -1):
        char  = string[index]
        reverted += str(char)
    return reverted

print(revert_string("Hola mundo"))
```

1. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

```python
def number_of_cases(string):
    upper_case_list =  [char for char in string if char.isupper() and len(char.strip()) != 0]
    lower_case_list =  [char for char in string if char.islower() and len(char.strip()) != 0]
    print(f'There’s {len(upper_case_list)} upper cases and {len(lower_case_list)} lower cases')

number_of_cases("I love Nación Sushi")
```

1. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
    
    Respuesta: Tambien pude haber usado la function sorted(words) or words.sort()
    

```python
def sort_alphabetically(string):
    words = string.split('-')
    sorted_words = []
    
    while len(words):
        first_word_position = get_first_word_position_alphabetically(words)
        word = words[first_word_position]
        sorted_words.append(word)
        words.pop(first_word_position)

    return "-".join(sorted_words)

def get_first_word_position_alphabetically(words):
    first = 0
    first_word = "zzzzzzzzzzzzzz"
    for index, word in enumerate(words):
        if word.lower() <= first_word.lower():
            first = index
            first_word = word
    return first
```

1. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

```python
def is_prime(number):
    returnValue = True

    if number == 2 or number == 3:
        pass

    elif number < 2 or number % 2 == 0:
        returnValue =  False
    
    else:
        for n in range(2,(number//2)+1):
            if number % n == 0:
                returnValue = False
                break

    return returnValue

def get_prime_numbers(numbers):
    only_prime = []
    for number in numbers:
        if(is_prime(number)):
            only_prime.append(number)
    return only_prime

print(get_prime_numbers([1, 4, 6, 7, 13, 9, 67]))
```

</aside>