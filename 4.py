print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#4.- Escribir un programa que pregunte al usuario su nombre, edad, dirección y
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
#mensaje <nombre> tiene
#<edad> años, vive en <dirección> y su número de teléfono es
#<teléfono>.

# Crear un diccionario para almacenar la información del usuario
usuario = {}

# Preguntar al usuario su nombre, edad, dirección y teléfono
usuario['nombre'] = input("Introduce tu nombre: ")
usuario['edad'] = input("Introduce tu edad: ")
usuario['direccion'] = input("Introduce tu dirección: ")
usuario['telefono'] = input("Introduce tu teléfono: ")

# Mostrar la información del usuario
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")





