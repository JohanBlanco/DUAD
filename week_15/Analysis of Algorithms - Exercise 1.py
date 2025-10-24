# Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort(list_to_sort):
    for _ in range(0, len(list_to_sort) - 1): # O(n)
        changed = False
        for index in range(0, len(list_to_sort) - 1 - _): # O(n^2)
            current = list_to_sort[index]
            next = list_to_sort[index+1]

            if current > next:
                list_to_sort[index] = next
                list_to_sort[index+1] = current
                changed = True
        if not changed:
            break

# Por lo tanto podemos concluir que bubble sort tiene una complejidad de O(n^2)
# Ya que en el peor de los casos este algoritmo llevara a cabo n^2 pasos