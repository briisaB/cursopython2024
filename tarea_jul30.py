# SETS
# Es una variable grupo:
#Añadir a las siguientes personas: Jose, Maria, Gerardo, Fabian


grupo = {"Fernando", "Federico", "Francisco", "Ricardo"}
grupo.update(["jose", "Maria", "gerardo", "fabian"])
print(grupo)

#Eliminar a las personas: Fernando, Federico, Francisco

grupo.remove("Fernando")
print(grupo) 

grupo.remove("Federico")
print(grupo) 

grupo.remove("Francisco")
print(grupo) 

# DICCIONARIOS
animalitos = {"elefante": ""}
animalitos["elefante"] = "pupi"
print(animalitos)

# Añadir al diccionario las claves perro, gato y tucan con sus valores "Tobi", "Michi" y "Diego"
animalitos.update({"perro":"tobi", "gato": "michi", "tucan":"Diego" })
print(animalitos)

# Modificar la clave elefante por delfin

animalitos.pop("elefante")
print(animalitos)

animalitos["delfin"] = "pupi"
print(animalitos)