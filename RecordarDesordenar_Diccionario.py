
diccionarioPreguntas = {}

##                         enunciado , respCorrecta, opciones
diccionarioPreguntas[0] = ["Numero 1", 1, [1, 2, 3, 4]]
diccionarioPreguntas[1] = ["Numero 2", 2, [1, 2, 3, 5]]
diccionarioPreguntas[2] = ["Numero 3", 3, [5, 2, 3, 4]]
diccionarioPreguntas[3] = ["Numero 4", 4, [1, 5, 3, 4]]
diccionarioPreguntas[4] = ["Numero 5", 5, [1, 4, 3, 5]]

#diccionario de preguntas con orden normal
print(diccionarioPreguntas)


import  random as rnd
rnd.shuffle(diccionarioPreguntas)
print(diccionarioPreguntas)

#Tarea. ¿Cómo se puede desordenar un diccionario en Python?


