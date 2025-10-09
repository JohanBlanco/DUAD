<aside>
💪🏽 **Ejercicios**

1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`

```python
hotel = {
    "name": "Riu",
    "number_of_stars": 5,
    "rooms": 1000,
}
```

- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`

```python
hotel = {
    "name": "Riu",
    "number_of_stars": 5,
    "rooms": [
        {
            "number": "A1",
            "floor": 1,
            "price_per_night": 200
        },
        {
            "number": "A2",
            "floor": 1,
            "price_per_night": 200
        },
    ],
}
```

1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`

```python
person = {}

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

for index in range(len(list_a)):
    key = list_a[index]
    value = list_b[index]
    person[key] = value

print(person)
```

1. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

```python
list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for key in list_of_keys:
    employee.pop(key)

print(employee)
```

</aside>