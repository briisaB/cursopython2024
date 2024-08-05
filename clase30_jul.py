#________________CONJUNTOS / SET _______________
""" conjunto = {1,2,3,4,5}
otro_conjunto = {"hola", "como", "estas"}
conjunto_vacio = set() """

#son heterogeneos
""" variable1 = "esto es una variable"
datos = {1, -3, 123,"una cadena","otro string", variable1 }
print(datos)"""

#Puede incluir numeros, variables, strings o tuplas.
#Pero NO puede incluir objetos mutables ccomo listas, diccionarios e incluso otros conjuntos


""" lista = ({1,2,3,4,5})
print(lista)
print(set([1,1,2,3,4,4,5])) """


# FUNCIONES INTEGRADAS EN SET/CONJUNTOS
# ADD
""" numeros = {1,2,3,4}
numeros.add(5)
print(numeros)
 """

# UPDATE
""" numeros = {1,2,3,4}
numeros.update([5,6,7,8])
print(numeros) """

#LEN
""" print(len(numeros)) """

#DISCARD
""" numeros.discard(2)
print(numeros) """

#REMOVE
#Remove y discard funciona de igual manera, a diferencia que en Discard si el elemento pasado como argumento no existe, lo ignora. en cambio con Remove nos devolvera error.


#IN
""" print(2 in numeros) """


#CLEAR 
""" numeros.clear() """


#POP
""" numeros1 = {1,2,3,4,5,6}
while numeros1:
    print("Se esta borrando: ", numeros1.pop()) """
    
#___________DICCIONARIO/ DICT________________


""" colores = {"amarillo": "yellow", "azul": "blue", "violeta": "violet" }
print(colores["amarillo"])

colores ["amarillo"] = "white"
print(colores)

edades = {"juan": 26, "esteban": 35, "maria": 23}
edades["juan"] +=5
edades["maria"] *=2
print(edades) """


#ADD
""" numeros3 = {"uno": 1, "dos": 2, "tres": 3}
numeros3["cinco"] = 5
print(numeros3) """


#UPDATE
""" numeros3.update({"seis":6})
print(numeros3)
 """

#LEN
""" print(len(numeros3)) """

#DEL
""" del numeros3["dos"]
print(numeros3) """

#IN
""" print("tres" in numeros3)
 """
#CLEAR
""" numeros3.clear() """

#POP
""" print(numeros3.pop("uno")) """


#____________ UPPER_______________

cadena = "hola chicos"
print(cadena.upper())

print("Hola como estan".upper())


#LOWER
string = "HOLA cHICOS"
print(string.lower())
 
 
#CAPITALIZE
cadena1 = "hola amigoS"
print(cadena1.capitalize())


#TITLE
cadena2 = "HOLa mUNDO"
print(cadena2.title())


#CoUNT
cadena3 = "HOLa mUNDO esta cadena tiene muchas a"
print(cadena3.count("a"))


#FIND
cadena4 = "HOLa mUNDO esta cadena tiene muchas a"
print(cadena4.find("esta"))


#RFIND 
cadena5 = "Hola amigo como estas amigo"
print(cadena5.rfind("amigo"))


#SPLIT
cadena6 = "hola MunDo"
print(cadena6.split())


#JOIN 
cadena7 = "Hola mundo"
print("-".join(cadena7))

#STRIP
cadena8  = "----------hola mundo-------"
print(cadena8.strip("-"))


#REPLACE
cadena9= "moron"
print(cadena9.replace("o", "0"))


#_________METODO PARA LISTAS________________

#CLEAR
letras = ["a", "b", "c", "d", "e", "f"]
print(letras)
letras.clear ()
print(letras)


#EXTEND 
numeros = [1,2,3,4,5]
numeros + [6,7,8,9,10]

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

lista1.extend(lista2)
print(lista1)


#INSER 
lista3 = [1,2,3,4,5,6]
lista3.insert(0,0)
print(lista3)


#REVERSE
lista4 = [1,2,3,4,5,6]
lista4.reverse()
print(lista4)

#SORT
lista5 = [5, -10, 35, 0, -75,150]
lista5.sort()
print(lista5)



#______________________CONJUNTOS_____________________________

#COPY
""" set1 = [1,2,3,4]
set2 = set1.copy()
print(set2) """


#ISDISJOINT
""" set3 = {1,2,3}
set4 = {3,4,5}
print(set3.isdisjoint(set4))  """


#ISSUBSET
set5 = {-1,99}
set6 = {1,2,3,4,5}
print(set5.issubset(set6))


#ISSUPERSET
set7 = {1,2,3}
set8 = {1,2}
print(set7.issuperset(set8))


#UNION
set9 = {1,2,3}
set10 = {3,4,5}
print(set9.union(set10))


#DIFFERENCE
""" set1 = {1,2,3}
set2 = {3,4,5}
print(set1.difference(set2)) """


#DIFFERENCE_UPDATE
""" set1 = {1,2,3}
set2 = {3,4,5}
set1.difference_update(set2)
print(set1)
 """

#INTERSECTION
set1 = {1,2,3}
set2 = {3,4,5}
set1.intersection(set2)
print(set1.intersection(set2))


#INTERSECTION_UPDATE
set1 = {1,2,3}
set2 = {3,4,5}
set1.intersection_update(set2)
print(set1)


#________________DICCIONARIOS_______________
 
#GET
""" colores = {"amarillo": "yellow", "azul": "blue", "violeta": "violet" }
print(colores.get("verde", "no hay clave verde"))
 """

#KEY
""" colores = {"amarillo": "yellow", "azul": "blue", "violeta": "violet" }
print(colores.keys()) """


#VALUES
colores = {"amarillo": "yellow", "azul": "blue", "violeta": "violet" }
print(colores.values())


#ITEMS
colores = {"amarillo": "yellow", "azul": "blue", "violeta": "violet" }
print(colores.items())

for clave, valor in colores.items():
    print(clave,valor)

