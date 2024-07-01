# NOTA FINAL EN BASE A 5 EXAMENES, ESTOS EXAMENES EQUIVALEN A UN PORCENTAJE DE LA NOTA FINAL.

# LA NOTA NUMERO 1 CORRESPONDE AL 20% DE LA NOTA FINAL.
# LA NOTA NUMERO 2 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 3 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 4 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 5 CORRESPONDE AL 50% DE LA NOTA FINAL.

#NOTA DEL ESTUDIANTE 
Examen1 = float(input(" ingresar nota del examen 1 (20%): "))
Examen2 = float(input(" ingresar nota del examen 1 (10%): "))
Examen3 = float(input(" ingresar nota del examen 1 (10%): "))
Examen4 = float(input(" ingresar nota del examen 1 (10%): "))
Examen5 = float(input(" ingresar nota del examen 1 (50%): "))

#PORCENTAJE DE LOS EXAMENES

porcentaje1 = 0.20 
porcentaje2 = 0.10 
porcentaje3 = 0.10 
porcentaje4 = 0.10
porcentaje5 = 0.50

#CALCULO DE LA NOTA FINAL

Nota_Final = (Examen1 * porcentaje1) + (Examen2 * porcentaje2) + (Examen3 * porcentaje3) + (Examen4 * porcentaje4) + (Examen5 * porcentaje5)

print("Tu nota final es: " + str(Nota_Final))