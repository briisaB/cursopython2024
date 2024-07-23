#if elif y else
# IF : SI
# ELIF: SINO, SI
# ELSE : SINO

# IF

""" edad= int(input("Que edad tenes?"))
if edad >= 18:
    print("Sos adulto")
    
if False:
    print("IMPRIMIME LA CONDICION VERDADERA") """
    

a = 2
b = 10
""" if a == 2:
    print("a vale", a)
    if b == 10:
        print("y b vale:", b) """
        
        
#ELSE

""" numero = 24
if numero >=36:
    print("El numero es mayor o igual a 36")
else:
    print("el numero es menor a 36")
     """

# ELIF

""" numero = 18
if numero >=18: 
    print("Es un adulto")
elif numero == 17:
    print("Casi es mayor")
else:
    print("Es menor") """
    
    
""" dato_entrada = input("ESCRIBI ENTRAR, SALUDO O SALIR: ").upper()
if dato_entrada == "ENTRAR" :
    print("Bienvenido") 
elif dato_entrada == "SALUDO" :
    print("Hola, como estas?")
elif dato_entrada == "SALIR" :
    print("Te estas yendo")
else:
    print("No reconozco la interaccion")
     """
    
""" nota = int(input("Escribi tu nota:"))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 6:
    print("Bien")
elif nota >= 4:
    print("Regular")
else:
    print("Desaprobaste") """
    


# SENTENCIAS ITERACTIVAS
# WHILE 
# FOR

# EL flujo de ejecucion de una sentencia WHILE:
#1. Evalua la condiccion devolviendo FALSE O TRUE 
#2. Si la condiccion es FALSE, se sale sentencia WHILE y continua la ejecuccion con la sigueinte SENTENCIA
#3. Si la condiccion es TRUE, ejecuta cada una de las sentenciasd que hay en el bloque del codigo y regresa el paso 1.

""" numero = 20
while numero >0:
    print(numero)
    numero-= 1
print("Termino el conteo") 

n = 0 
while n <=5:
    n+=1
    print("N vale", n) """
    
#while condicion: 
#  intrucciones de while
#else
#  intrucciones de while-else
#si no se termino con break
#  intrucciones de while-else


""" chance = 1
while chance <= 3:
    txt =input("Escribe SI: ")
    if txt == "SI":
        print("ok, lo conaeguiste en el intento", chance)
        break
    chance +=1
else:
    print("Has agotado tus tres intentos") """
    
# BREAK - CONTINUE - PASS

#  BREAK CIERRA EL BUCLE CON UNA CONDICION EXTERNA
""" n = 5 
while n < 10:
    n-=1
    if n == 2:
        print("ahora n vale 2 y salimos del bucle")
        break
    print("n vale", n) """
    
# CONTINUE SIRVE PARA OMITIR UNA PARTE DEL BUCLE EN LA CUAL SE ACTIVA UNA CONDICION EXTERNA

""" m = 0
while m < 10:
    m+=1
    if m==2:
        print("Continuamos con la siguiente interacion")
        continue
    print("m vale", m) """


#PASS sirve para manejar la condicion sin que el bucle se vea afectado de ninguna manera.
""" 
l = 0
while l < 10:
    l+=1
    if l ==2:
        pass
    print("l vale", l) """


# FOR

""" lista = [1,2,3,4,5,6]

for valor in lista:
    print("Soy un item de la lista y valgo", valor) """


#FOR = PARA
#Valor es simplemente una variable creada del objeto que se esta iterando 
# IN = en 
# lista es la lista, tupla, etc.. que va ser iterada..


""" lista_1 = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista_1:
    print("soy el valor de la lista_1 y ahora valgo", num)
    num *=5
    print("soy un valor de la lista_1 y ahora valgo", num)
 """


texto = "Hola mundo, como estan?"
for letra in texto:
    print(letra)

texto2 = ""
for letra in texto:
    texto2= letra *2
print(texto2)