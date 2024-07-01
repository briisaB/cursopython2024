#Clase Martes 18 de junio
#____________NUMEROS___________
##NUMEROS ENTEROS = INT O LONG
##LONG 123312331345547L ENTEROS


## NUMERO FLOAT = NUMEROS CON DECIMALES 
## EJ; 0,5 O NUMERO NEGATIVO EJ; -33,544


# COMPLEX 
## 33,8j

# SUMA + 
# RESTA - 
# MULTIPLICACION *
# POTENCIA **
# DIVISION (cociente) /
# DIVISION (parte entera) //
# PROMEDIO %

""" print(15.5+8)

print(3/2)

print(50*6) """

#________________STRING = STR (CADENA DE TEXTO)___________

print("hola como estan")

print("un string \t con tabulacion")

print("otro strin pero con \n saltos de linea")


#_______________________VARIABLES__________________________
# LAS VARIABLES EN PYTHON SON COMO ETIQUETAS QUE NOS PERMITEB HACER REFERENCIA A LOS DATOS.
# POR CADA DATO QUE APARECE EN UNA PROGRAMA, PYTHONM VA A CREAR UN OBJETO QUE LO CONTIENE.
# CADA OBJETO VA A TENER:
#1- UN IDENTIFICADOR UNICO (id)
#2- UN TIPO DE DATO (entero, decimal sting, etc)
#3- UN VALOR (el propio dato dentro)
# LAS VARIABLES EN PYTHON NO GUARDAN LOS DATOS.

dni = 42595811 

a = 2

print(dni)
print(a)

#### EL NOMBRE DE UNA VARIABLE SIEMPRE DEBE EMPEZAR POR UNA LETRA O POR UN GUION BAJO (_) snake_case
#LOS NOMBRES EN LAS VARIABLES NO PUEDEN INCLUIR ESPACIOS EN  BLANCOS
mi_fecha_de_nacimiento = "4 de noviembre"

print(mi_fecha_de_nacimiento)


#METODO DE SALIDA = PRINT()

#METODO DE SALIDA = IMPUT()

""" nombre = input("hola! Escribi tu nombre:")

print(nombre) """

print(30+9)


# LA FUNCION INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADA EN UN STRIN (ES UNA CADENA)AUNQUE ESTUVIERAMOS ESCRIBIENDO UN NUMERO

a=20
b=30

resultado=a+b

print(resultado)

c=100
d=200

print(c+d)

#LOS DATOS DE ENTRADAS SE PODRIAN CONVERTIR DE STR (STRING)

e=30
""" f= input("cual es tu edad")  """ # ESTE ES UN ej DE UN DATO DE ENTRADA QUE LO TOMA COMO CADENA DE TEXTO 
""" f=int(input("cual es tu edad")) """ #CONVERSION DE TIPO: De esta forma logramos que python convierta el STR de entrada en un numero



""" print(e+f) """


cadena_de_texto="Python"
anio_del_curso="2024"

print(cadena_de_texto + anio_del_curso)

# A LAS SUMA DE LOS STRINGS LO VAMOS A LLAMAR CONCATENACION

print(cadena_de_texto[2])