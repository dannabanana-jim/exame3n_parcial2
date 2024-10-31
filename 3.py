print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")


#3.-Escribir un programa que almacene las
#asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
#Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las correspondientes

# Lista de asignaturas
asignaturas = ["Matematicas", "Física", "Quimica", "Historia", "Lengua"]

# Preguntar y mostrar las notas
for asignatura in asignaturas:
    nota = float(input(f"Nota de {asignatura}: "))
    print(f"En {asignatura} has sacado {nota}")



