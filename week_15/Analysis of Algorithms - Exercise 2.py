# 2. Analice los siguientes algoritmos usando la Big O Notation:


# print_numbers_times_2
# Respuesta: 
# Por lo tanto podemos concluir que print_numbers_times_2 tiene una complejidad de O(n)
# Ya que en el peor de los casos este algoritmo llevara a cabo n pasos, o el numero de
# elementos que contenga numbers_list
def print_numbers_times_2(numbers_list):
	for number in numbers_list: # O(n)
		print(number * 2)
		
# check_if_lists_have_an_equal
# Respuesta: 
# Por lo tanto podemos concluir que check_if_lists_have_an_equal tiene una complejidad de O(n^2)
# Ya que en el peor de los casos este algoritmo llevara a cabo n^2 pasos
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(n^2)
			if element_a == element_b:
				return True
				
	return False

# print_10_or_less_elements
# Respuesta: 
# Por lo tanto podemos concluir que print_10_or_less_elements tiene una complejidad de O(1)
# Ya que en el peor de los casos este algoritmo llevara a cabo 10 pasos
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)): # O(1)
		print(list_to_print[index])
		
# generate_list_trios
# Respuesta: 
# Por lo tanto podemos concluir que generate_list_trios tiene una complejidad de O(n^3)
# Ya que en el peor de los casos este algoritmo llevara a cabo n^3 pasos
def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(n^2)
			for element_c in list_c: # O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 
