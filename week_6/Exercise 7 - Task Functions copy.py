# 1. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
    
#     Respuesta: Tambien pude haber usado la function sorted(words) or words.sort()
    


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
