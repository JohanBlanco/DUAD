

# 1. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#     1. Ejemplos:
#     2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.


largest = 0

for _ in range(10):
    number = int(input("Type an integer number: "))
    if(number > largest):
        largest = number

print(f"The largest number is: {largest}")