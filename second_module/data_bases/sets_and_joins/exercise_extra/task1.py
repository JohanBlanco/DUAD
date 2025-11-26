from typing import Set

all:Set = {1,2,3,4,5,6,7,8,9,10}
even:Set = {2,4,6,8,10}
odd:Set = {1,3,5,7,9}

'''
1. Explicación cruzada entre conjuntos y SQL
Analice la operación de conjuntos All - Odd.
Explique cómo una operación similar se puede representar en SQL con JOINs.
¿Qué tipo de JOIN usaría?
'''

print('All - Odd')
print(all.difference(odd))

'''
Respuesta:
-> Del resultado del query, se quiere omitir una parte, por ejemplo cuando
se hace un left join para saber los registros que no tienen relacion aun con 
otra tabla, entonces al join se le agrega la condicion de que el id de la tabla
con nulos sea null

como por ejemplo

select a.id, a.name
from Authors a 
left join Books b
on b.Author = a.id
where b.id is NULL;

otro ejemplo seria el inner join, que directamente omite los registros donde
no hay un match, o sea que el registro contendra nulos en el caso de un left join

'''