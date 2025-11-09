
        
# 2. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41


def sum_list_numbers(my_list):
    sum = 0
    for num in my_list:
        sum += num
    return sum

my_list = [4, 6, 2, 29]
print(sum_list_numbers(my_list))
