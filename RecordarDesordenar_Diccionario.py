
diccionarioPreguntas = {}

##                         enunciado , respCorrecta, opciones
diccionarioPreguntas[0] = ["Numero 1", 1, [1, 2, 3, 4]]
diccionarioPreguntas[1] = ["Numero 2", 2, [1, 2, 3, 5]]
diccionarioPreguntas[2] = ["Numero 3", 3, [5, 2, 3, 4]]
diccionarioPreguntas[3] = ["Numero 4", 4, [1, 5, 3, 4]]
diccionarioPreguntas[4] = ["Numero 5", 5, [1, 4, 3, 5]]

print()
#diccionario de preguntas con orden normal
print("Diccionario Original")
print(diccionarioPreguntas)

##opcion 0
#copiaDesordenada = diccionarioPreguntas   #no es buena idea, debido a que las referencias se copian

#opcion 1
#copiaDesordenada = {}
#for i in diccionarioPreguntas:
#    #print(diccionarioPreguntas[i])
#    copiaDesordenada[i] = diccionarioPreguntas[i]
###########################################################

#opcion 2
copiaDesordenada = diccionarioPreguntas.copy()
#####################################################

print("Copia Sin Cambios")
print(copiaDesordenada)

import  random as rnd
rnd.shuffle(copiaDesordenada)
print("Desordenado")
print(copiaDesordenada)

print("Original:")
print(diccionarioPreguntas)

#Tarea. ¿Cómo se puede desordenar un diccionario en Python?


