<aside>
💪🏽 **Ejercicios**

**Para estos ejercicios debe utilizar solo lo visto en clase. No es valido utilizar funciones como `zip` o `reversed`.**

1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util

```python
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(len(first_list)):
    print(first_list[index])
    print(second_list[index])
```

1. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    1. Pista: investigue de que otras maneras se puede usar el `range`.
    2. Ejemplos:
    3. `my_string = ‘Pizza con piña’` → 
    a
    ñ
    i
    p
    
    n
    o
    c
    
    a
    z
    z
    i
    p

```python
my_string = 'Pizza con piña'

for index in range(len(my_string)-1, -1, -1):
    print(my_string[index])
```

1. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`

```python
my_list = [4, 3, 6, 1, 7]
print(my_list)

my_list = [my_list[-1]] + my_list[1:-1] + [my_list[0]]

print(my_list)
```

1. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [number for number in my_list if number % 2 == 0]

print(my_list)
```

1. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

```python
largest = 0

for _ in range(10):
    number = int(input("Type an integer number: "))
    if(number > largest):
        largest = number

print(f"The largest number is: {largest}")
```

</aside>