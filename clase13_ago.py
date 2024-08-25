""" def saludar():
    print("HOla")
saludar()
 """
""" try:
 n = float(input("introduce un numero: "))
 m = 4
 print(n, "/", m, "=", n/m )
except:
    print("algo salio mal")
 """

while(True):
    try:
        n = float(input("introduce un numero: "))
        m = 4 
        print(n, "/", m, "=", n/m)
        break
    except:
     print("ocurrio un error, introduci un nro")
    else:
     print("todo sucedio correctamente")
     break