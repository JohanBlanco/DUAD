# 1. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”


def revert_string(string):
    reverted = ""
    for index in range(len(string) -1, -1, -1):
        char  = string[index]
        reverted += str(char)
    return reverted

print(revert_string("Hola mundo"))
