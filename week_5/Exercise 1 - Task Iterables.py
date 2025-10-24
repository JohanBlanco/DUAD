# <aside>
# 💪🏽 **Ejercicios**

# **Para estos ejercicios debe utilizar solo lo visto en clase. No es valido utilizar funciones como `zip` o `reversed`.**

# 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#     1. Ejemplos:
#     2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
#     `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
#     Hay casos
#     en los
#     que la
#     iteracion por
#     indice es
#     muy util


first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(len(first_list)):
    print(first_list[index])
    print(second_list[index])