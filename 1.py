print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#1.-Escribir un programa que almacene las
#asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
#Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura y elimine de la lista las asignaturas aprobadas. Al final el
#programa debe mostrar por pantalla las asignaturas que el usuario tiene que
#repetir.

# Lista de asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para almacenar las asignaturas que el usuario debe repetir
repetir = []

#cada asignatura en la lista
for asignatura in asignaturas:
    # Solicitar al usuario que introduzca la calificación para la asignatura actual
    nota = float(input(f"Calificación de {asignatura}: "))
    
    # Verificar si la nota es menor o igual a 5
    if nota < 5:
        # Si la nota es insuficiente, añadir la asignatura a la lista de repetir
        repetir.append(asignatura)

# Mostrar al usuario las asignaturas que debe repetir
print("Asignaturas que debes repetir:", repetir)






