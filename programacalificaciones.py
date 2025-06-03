def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            calificaciones = list(map(float, input("Ingresa las calificaciones separadas por comas: ").split(",")))
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Error: Ingresa solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, calificaciones in estudiantes.items():
        promedios[nombre] = sum(calificaciones) / len(calificaciones)
    return promedios

def obtener_mejor_estudiante(promedios):
    return max(promedios, key=promedios.get)

def guardar_resultados(estudiantes, promedios, mejor):
    with open("resultados.txt", "w") as archivo:
        for nombre, calificaciones in estudiantes.items():
            archivo.write(f"{nombre}: {calificaciones}, Promedio: {promedios[nombre]:.2f}\n")
        archivo.write(f"\nMejor estudiante: {mejor} con promedio de {promedios[mejor]:.2f}\n")

def main():
    estudiantes = ingresar_datos()
    promedios = calcular_promedios(estudiantes)
    mejor = obtener_mejor_estudiante(promedios)
    guardar_resultados(estudiantes, promedios, mejor)
    print("Resultados guardados en resultados.txt")

if __name__ == "__main__":
    main()
