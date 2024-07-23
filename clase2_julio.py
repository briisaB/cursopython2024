
#____OPERADORES

#Operandores [operador] Operando
#     -/ + *

# Tipo logico BOOLEANO o BINARIO
#Representa el VERDADERO o FALSO
 
#NEGACION____
# No Verdadero = Falso
# No falso= Verdadero


# OPERADORES RELACIONALES 
#Los operadores relacionales son simbolos que se usan para comparar dos valores si el resultado de la comparacion es correcto la expresion va a ser considerada TRUE de lo contrario FALSE 

print( 1+1==3) #Operador de la igualdad ==

# Sirve para preguntar si ambos son operadores iguales

a = 3 

print(a == 3)


#
#DESIGUALDAD o DISTINTO____
# Sirve para preguntar si ambos son operadores distintos

print(a != 3) #Operador de desigualdad !=


#
#MENOR QUE_____
# Sirve para preguntar si el primer operando es menor que el segundo
# Nos va a devolver TRUE si el primero es menor al segundo y FALSE si el primero es mayor que el segundp

print(7<3) #Operador de menor que <

#
# MENOR IGUAL QUE_____
#Sirve para preguntarle a nuestro programa si el primer operando es menor que el segunndo o si ambos son iguales

print(7<=3)     #operandor de menor igual <=
print(10<=10)


#
#MAYOR QUE______
# #Sirve para preguntarle a nuestro programa si el primer operando es MAYOR que el saegundo

print(7>6)
print(1>2)


## MAYOR IGUAL QUE_____
#Sirve para preguntarle a nuestro programa si el primer operando es MAYOR que el segunndo o si ambos son iguales

print(7>=3)     #operandor de mayor igual >=
print(10>=10)




# Podemos hacer operaciones relacionales en string inclusive

print("hola" == "hola")

b = "hola"
print(b[1] == "o") # Aca le estoy pidiendo al programa que me diga si el indice 1 de la variable b es igual a "o"


#True es MAYOR  a falso porque tiene un valor aritmetico de 1

""" print(False == True)
print(True* == 2.5*2)  """


#_______________ OPERADORES LOGICOS
#NOT

print(not True)
