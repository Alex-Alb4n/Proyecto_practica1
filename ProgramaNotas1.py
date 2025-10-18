# Programa para calcular el promedio de estudiantes en la Universidad UNEMI
# UNIVERSIDAD UNEMI - UNIVERSIDAD ESTATAL DE MILAGRO

print("UNIVERSIDAD UNEMI - UNIVERSIDAD ESTATAL DE MILAGRO")
print("Programa para evaluar el rendimiento de estudiantes en 6 materias.")
print("Materias evaluadas:")
print("1. LENGUAJE Y COMUNICACIÓN")
print("2. FUNDAMENTOS MATEMÁTICOS PARA INGENIERÍA")
print("3. CALCULO DIFERENCIAL")
print("4. FUNDAMENTOS DE TECNOLOGÍAS DE INFORMACIÓN")
print("5. ÁLGEBRA LINEAL")
print("6. FUNDAMENTOS DE LA PROGRAMACIÓN")
print("Nota: Para aprobar una materia, la calificación debe ser mayor o igual a 70/100.\n")

# Lista de materias
materias = [
    "LENGUAJE Y COMUNICACIÓN",
    "FUNDAMENTOS MATEMÁTICOS PARA INGENIERÍA",
    "CALCULO DIFERENCIAL",
    "FUNDAMENTOS DE TECNOLOGÍAS DE INFORMACIÓN",
    "ÁLGEBRA LINEAL",
    "FUNDAMENTOS DE LA PROGRAMACIÓN"
]

# Función para obtener una nota válida
def obtener_nota(materia):
    while True:
        try:
            nota = float(input(f"Ingrese la nota para {materia} (0-100): "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Ingrese un número válido.")

# Bucle principal para evaluar estudiantes
estudiante_num = 1
while True:
    print(f"\n--- Evaluando al estudiante {estudiante_num} ---")
    
    # Datos del estudiante
    nombre = input("Nombre del estudiante: ")
    semestre = input("Semestre que cursa: ")
    carrera = input("Carrera que cursa: ")
    
    # Lista para almacenar notas
    notas = []
    aprobadas = []
    reprobadas = []
    
    # Pedir notas para cada materia
    for materia in materias:
        nota = obtener_nota(materia)
        notas.append(nota)
        if nota >= 70:
            aprobadas.append(materia)
        else:
            reprobadas.append(materia)
    
    # Mostrar resultados
    print(f"\nEstudiante: {nombre}")
    print(f"Semestre: {semestre}")
    print(f"Carrera: {carrera}")
    print("\nMaterias Aprobadas:")
    if aprobadas:
        for mat in aprobadas:
            print(f"- {mat}")
    else:
        print("Ninguna")
    
    print("\nMaterias Reprobadas:")
    if reprobadas:
        for mat in reprobadas:
            print(f"- {mat}")
    else:
        print("Ninguna")
    
    # Calcular promedio
    promedio = sum(notas) / len(notas)
    print(f"\nPromedio general: {promedio:.2f}/100")
    
    if promedio >= 70:
        print("El estudiante aprueba el semestre.")
    else:
        print("El estudiante reprueba el semestre.")
    
    # Preguntar si continuar o salir
    opcion = input("\nPresione Enter para salir o Espacio para evaluar a otro estudiante: ")
    if opcion == "":
        break  # Salir del bucle
    elif opcion == " ":
        estudiante_num += 1  # Incrementar contador y continuar
        continue
    else:
        print("Opción inválida. Evaluando a otro estudiante.")
        estudiante_num += 1
        continue

print("\nEvaluación completada. Programa finalizado.")
