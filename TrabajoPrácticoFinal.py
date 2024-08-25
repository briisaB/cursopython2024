#____Ejercicio 1: Números y Cadenas de Caracteres____


#A.Escribe un programa que pida al usuario dos números enteros
numero_entero1 = int(input("Ingresar el primer numero: "))
numero_entero2 = int(input("Ingresar el segundo numero: "))
print(numero_entero1)
print(numero_entero2)

print("la suma da: ", numero_entero1 + numero_entero2)
print("el producto es: ", numero_entero1 * numero_entero2)
print("la concatenacion es: ", str(numero_entero1) + str(numero_entero2))

#B.Pide al usuario una cadena de texto.
cadena = input("Ingresa una cadena de texto: ")
#_La cadena en mayúsculas.
print(cadena.upper())      
#_La longitud de la cadena.
print(len(cadena))         
#_La cadena invertida.
print(cadena[::-1])       
#_La cantidad de veces que aparece una letra específica
cadena2 = input("Ingrese un texto con la letra b: ")
print(cadena2.count("b"))  

#C.Escribe un programa que convierta un número decimal a binario y viceversa.
num1 = int(input("Ingrese el numero decimal que desee convertir: "))
binario = ''
while num1 > 0:
    if num1 %2 == 0:
        binario = '0' + binario
    else:
        binario = "1" + binario
    num1 = num1 // 2
print(binario)

num2 = input("Ingrese el numero binario que desee convertir: ")
decimal = 0
posicion = len(binario) - 1 
for i in binario:
    if i == '1':
        decimal += 2 ** posicion
    posicion = posicion - 1
print(decimal)

#D.Pide al usuario una cadena y un número entero. Muestra la cadena repetida el número de veces indicado por el número entero.
cadena_texto = input("Ingresa un texto: ")
numero_entero = int(input("Ingresa un Numero entero: "))
print(cadena_texto * numero_entero)


#____Ejercicio 2: Listas y Tuplas____


#A.Crea una lista con los nombres de tres frutas.

lista = ["anana","pera","durazno"]
print(lista)
#_Añade dos frutas más a la lista.
otras_frutas = ["melon","sandia"]  
lista.extend(otras_frutas)
print(lista)
#_Ordena la lista alfabéticamente.
lista.sort()                       
print(lista)
#_Muestra la lista completa.
print("Lista completa: ", lista)   
#_Elimina una fruta de la lista y muestra el resultado.
lista.pop()                        
print(lista)

#B.Crea una tupla con los nombres de dos ciudades.

tupla = ("Berlin","Roma")
print(tupla)
#_Muestra el primer y último elemento de la tupla.
print("Primer elemento:",tupla[0])
print("Ultimo elemento:",tupla[-1])
#_Convierte la tupla en una lista, añade una nueva ciudad y muestra la lista resultante.
list(tupla)
otra_ciudad = ["Buenos Aires",(tupla)]
print(otra_ciudad)

#C.Crea una lista de números enteros.

lista_num = [0,1,2,3,4,5,6,7,8,9,10]
print(lista_num)
#_El número mayor de la lista.
print(max(lista_num))
#_El número menor de la lista.
print(min(lista_num))
#_El promedio de los números en la lista.
suma = 0
for numero in lista_num:
    suma = + numero
promedio = suma / len(lista_num)
print(promedio)

#D.Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas.

lista_de_cadena = []
while True:
    palabra = input("Ingrese una cadena de texto: ")
    
    if palabra:
        lista_de_cadena.append(palabra.upper())
    else:
        break
for c in lista_de_cadena:
    print(c)



#____Ejercicio 3: Controladores de Flujo____


#A.Escribe un programa que pida un número al usuario. Muestra si el número es par o impar.

numero = int(input("Ingrese un numero entero: "))
if(numero % 2) == 0:
    print(numero,"Es un numero par")  
else:                             
        print(numero,"es un numero impar")  

#B.Crea un programa que simule un menú simple(saludar,despedirse y salir)
menu = input("Elige su opcion del menu: opcion1, opcion2, opcion3: ")
if menu == "opcion1":
    print("Holaa!! como estas?")
elif menu == "opcion2":
    print("Te vas? Hasta luego!!")
elif menu == "opcion3":
    print("Estas saliendo..Adios!!")
else:
    print("No reconozco esa opcion, ingresar nuevamente")

#C.Escribe un programa que pida un número al usuario y determine si es positivo, negativo o cero.
numero_ingresado = int(input("Ingresar el numero deseado: "))
if numero_ingresado > 0:
    print("El numero ingresado es positivo")
elif numero_ingresado < 0:
    print("El numero ingresado es negativo")
else:
    print("El numero es 0")

#D.Escribe un programa que muestre los números del 1 al 10 utilizando un bucle for.
numeros_1a10 = [1,2,3,4,5,6,7,8,9,10]
for valor in numeros_1a10:
    print("Soy el numero", valor)

#E.Escribe un programa que calcule la suma de los números del 1 al 100 utilizando un bucle while.
x = 1
suma = 0
while x<= 100:
    suma = suma + x
    x +=1
print("La suma de los numeros del 1 al 100 es: ", suma)


#____Ejercicio 4: Conjuntos y Diccionarios____


#A.Crea dos conjuntos con algunos números.
set1 = {1,2,3,4,5,4}
set2 = {6,7,8,2,1}
#_La unión de los dos conjuntos.
print(set1.union(set2))
#_Muestra la diferencia entre los dos conjuntos.
print(set1.difference(set2))
#_Muestra los elementos comunes en ambos conjuntos.
print(set1.intersection(set2))

#B.Crea un diccionario con tres nombres como claves y edades como valores
datos = ({"Micaela":"22", "Stephanie": "24", "Magali":"26" })
print(datos)
#_Muestra la edad del primer nombre en el diccionario.
print(datos.get("Micaela"))
#_Añade un nuevo nombre y edad al diccionario.
datos.update({"Natalia":30})
print(datos)
#_Elimina un nombre del diccionario y muestra el resultado.
datos.pop("Natalia")
print(datos)
#_Muestra todas las claves y todos los valores del diccionario.
print(datos.keys())
print(datos.values()) 

#C.Crea un diccionario con los nombres de cinco productos como claves y sus precios como valores.
productos = ({"fideos":500, "mayonesa":700, "mostaza":650, "ketchup":800, "aceite":1400})
print(productos)
#_Muestra el precio de un producto específico.
print(productos.get("aceite"))
#_Incrementa el precio de todos los productos en un 10%.
productos_actualizados = {producto: precio * 1.10 for producto, precio in productos.items()}
print(productos_actualizados)

#D.Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8.
conjunto = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}
#_La intersección de los dos conjuntos.
print(conjunto.intersection(conjunto2))
#_La diferencia simétrica entre los dos conjuntos.
print(conjunto.symmetric_difference(conjunto2))


#____Ejercicio 5: Funciones____


#A.Define una función saludar(nombre) que reciba un nombre y muestre un saludo. Luego llama a esta función con tu propio nombre.
def saludar():
    print("hola")
saludar()

def saludar(nombre):
    print("hola",nombre)
saludar("brisa")

#B_Define una función suma(a, b) que reciba dos números y retorne su suma. Luego prueba la función con dos números diferentes.
def suma(a, b):
    return a + b
print(suma(4,2))

#C_Define una función es_mayor_de_edad(edad) que reciba una edad y retorne True si la edad es mayor o igual a 18 y False en caso contrario. Prueba la función con diferentes edades.
def es_mayor_de_edad(edad):
    return edad >= 18
print(es_mayor_de_edad(17))