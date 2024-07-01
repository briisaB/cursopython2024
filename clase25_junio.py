#Longitud de string 
# Funcion LEN

""" esto_es_un_string = "hola soy un string"

print(len(esto_es_un_string) )

string1= "     "
print(len(string1)) """

#Rebanar un string 
# Funcion SLICING [inicoi:fin:paso]
#Inicio va a ser el indice del primer caracter de la cadena que queremos rebanar
#Fin va a ser el inmdice del ultimo caracter no incluido de la cadena que queremos rebanar
#Paso: indica cada cuantos caracteres seleccionaremos entre las posiciones del inicio y fin

""" saludo = "hola, como estan?"
saludo[0:3:1]
print(saludo[0:3:1])

palabra = "pithon"
print(palabra)

print(palabra[1]) """

""" palabra[1]= "y"  """   #esto no se puede, esta mal

""" palabra = palabra[0:1] + "y" + palabra[2:]
print(palabra) """

### LISTA Y DUPLAS

""" mi_lista = [-11,20,3,41]
print(mi_lista)

otra_lista = ["hola", "como", "estas", "?"]

variable_1 = "una variable"

listita = [1, -10, 132.3, "un string", "otro string", variable_1]

print(listita)


print(listita[0])
print(listita[-2])

print(listita[-2:])

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,15,16])

numeros = [0,2,4,5,10,15,20]
numeros[3] = 8
print(numeros)

letras = ["a", "b", "c", "d","e", "f"]
letras[:3] = ["A", "B", "C"]
print(letras)

letras = ["a", "b", "c"]
letras[:3] = []
print(letras)

equipos = ["Moron", "River", "independiente", "boca"]
print(equipos)
equipos = []
print(equipos) """



#FUNCION APPEND
#Nos permite agregar un numero item al final de una lista - Se escribe mi_lista.append(item_a_agregar)

""" numeros = [1,2,3,4,5,6]
numeros.append(5+5)
print(numeros)
 """
#Tambien podemos utilixar la funcion LEN aca - LEN se escrib len(la_lista_a_consultar_su_longitud)
""" print(len(numeros)) """


#FUNCION POP
#La funcion todo lo contrario a Append, porque va a eliminar el ultimo item de una lista

""" equipos = ["Moron", "River", "independiente", "boca"]
equipos.pop()
print(equipos)

equipos = ["Moron", "River", "independiente", "boca"]
equipos.pop(2)
print(equipos) """

# FUNCION COUNT
#Muestrea la cuenta del numero de veces que el item se repite
numeros_varios = [1,2,3,4,5,6,7,77,87,1,9,1,31]
print(numeros_varios.count(1))

#INDEX
#Busca el item y nos devuelve en que indice esta 

numeros_varios = [1,2,3,4,5,6,7,77,87,1,9,1,31]
print(numeros_varios.index(2))

##_______ TUPLAS
#Las tuplas son similares a las listas, la GRAN diferencia es que las tuplas son INMUTABLES
# Se declaran con parentesis . mi_tupla(1,2,3,4)

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

tupla = (1,)
print(tupla)

otra_tupla = (1,5,-100, "cadena", "otra cadena/string", mi_tupla)

print(otra_tupla)

print(otra_tupla[-2])

print(otra_tupla[2:])

""" otra_tupla[0] = 5000 """

print(len(otra_tupla)) #cantidad de item

print(otra_tupla.index(5)) #busca la posicision del item

print(otra_tupla.count(1)) #cuantas veces se repite el numero



