#CLASE 16 de Julio, analizar el código y explicar que hace cada linea, luego reemplazarlo por otra condición
#WHILE
n = 10      # se asigna un valor a la variable n entero en este caso 10
while n < 10: # indicamos que mientras n sea menor a 10 entre al bloque de codigo
    
    if (n%2) == 0:   # indica que si n es un numero divisible por 2 su resto sera igual a 0
        print(n,"Es un numero par")   # si es true se imprime la variable n es un numero par 
    else:                             # si es false se ejecuta el else
        print(n,"es un numero impar") 
    n+=1      # se suma de a uno al bucle 


grados = 0
while grados < 30:
    if grados > 20:
        print(grados,"Hace calor")
    else:
        print(grados,"Hace Frio")
    grados+=1



#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo



Estacion = input("ESCRIBI TU ESTACION DEL AÑO: ").upper()
if Estacion == "PRIMAVERA" :
    print("Los meses de primavera es del: 21 de septiembre a 20 de diciembre") 
elif Estacion == "VERANO" :
    print("Los meses de verano es del: 21 de diciembre a 20 de marzo")
elif Estacion == "OTOÑO" :
    print("Los meses de otoño es del: 21 de marzo a 20 de junio")
elif Estacion == ("INVIERNO") :
    print("Los meses de invierno es del: del 21 de junio a 20 de septiembre")
else:
    print("No reconozco la estacion del año") 
    
