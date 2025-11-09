# <aside>
# 💪🏽 **Ejercicios**

# 1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


with open('unordered playlist.txt') as unordered_playlist:
    lines = unordered_playlist.readlines()
    lines.sort()
    for line in lines:
        with open('ordered playlis.txt', 'a') as ordered_playlist:
            ordered_playlist.write(line)