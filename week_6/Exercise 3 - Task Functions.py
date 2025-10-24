
    
# 1. Intente accesar a una variable global desde una función y cambiar su valor.
    
#     Respuesta: 
    
#     Es necesario el uso de la palabra reservada global seguida del nombre de la variable global
    

global_var = 10

def new_function():
    global global_var
    global_var = 50

new_function()
print(global_var)
