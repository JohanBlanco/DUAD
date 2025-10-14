# <aside>
# 💪🏽 **Ejercicios**

# 1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def clear_result():
    return 0

def exit_program():
    exit()

def displayMenu():
    print("""
                1. Add
                2. Substract
                3. Multiply
                4. Divide
                5. Clear Result
                6. Exit
            """)
    
def calculate():
    currentValue = 0
    newValue = 0
    option = 0
    options = {
    1: add,
    2: substract,
    3: multiply,
    4: divide,
    5: clear_result,
    6: exit_program
    }

    while True:
        print(f"\nCurrent Value: {currentValue}")
        displayMenu()
        try:
            option = int(input("Choose an Option: "))
            if 0 < option < 5:
                newValue = float(input("Type a number: "))
                currentValue = options[option](currentValue, newValue)
            else:
                currentValue = options[option]()
        except ValueError:
            print("The value must be a number\n\n")
        except KeyError:
            print("The value must be in the range of [1,6], both included\n\n")
        except ZeroDivisionError:
            print("The number can not be devided by 0 ")

if __name__ == '__main__':
    calculate()