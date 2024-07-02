#CLASE 25/6: TENIENDO DOS LISTA LA CUAL LLAMAREMOS lista_1 y lista_2 hay que hacer los siguientes ejercicios

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"

#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789

#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último

#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último

#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4


#                              AHORA CON TUPLAS
#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:

# El ultimo item de la tupla creada, el numero de items de la misma, 
# la posicion donde se encuentra algun item que haya dentro, 
# una lista con los ultimos cuatro items de la tupla,
# un item que haya en la posicion 8, 
# el numero de veces que se repite algún item dentro de la misma.
""" numero = [4567] 
nombre = "UNAHUR"
lista_1 = [numero, nombre]
print(lista_1)

variable = ["EDUCACION"]
entero  = [789]
lista_2 = [variable, entero]
print(lista_2)

lista_3 = lista_1[-2]
print(lista_3)

lista_4 = lista_2[1:-1]
print(lista_4)

lista_5 = [lista_3, lista_4]
print(lista_5)
 """


tupla = [1, -2, 40, 33, 0.5, 60, 777, 88, 900, 110, -11, 122, 3.33, 40, -1.5, 116]
print(tupla)

ultimo_item = tupla[-1]
print(ultimo_item)

numeros_de_items = tupla
print(len(numeros_de_items))

posicion_de_item = tupla
print(posicion_de_item.index(60))

ultimos_cuatro_items = tupla[-4:]
print(ultimos_cuatro_items)

posicion_8 = tupla[8]
print(posicion_8)

repeticion_items = tupla
print(repeticion_items.count(40))