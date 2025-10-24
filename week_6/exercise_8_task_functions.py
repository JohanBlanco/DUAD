

# 1. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*


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
