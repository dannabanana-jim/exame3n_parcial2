print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#2.-Escribir un programa que almacene el diccionario
#con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y
#después muestre por pantalla los créditos de cada asignatura en el
#formato <asignatura>
#tiene <créditos> créditos, donde <asignatura> es
#cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe
#mostrar también el número total de créditos del curso.

# Diccionario con las asignaturas y sus créditos
asignaturas_creditos = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

# Inicializar el total de créditos
total_creditos = 0
#La "F", se utuliza para agregar las variables a la respuesta, sin complicarse tanto.
# Mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas_creditos.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total_creditos += creditos

# Mostrar el total de créditos
print("Total de créditos del curso:", total_creditos)







