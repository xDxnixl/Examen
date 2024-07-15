import random
import csv

# Lista de empleados
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez",
                "Pedro Rodríguez","Laura Hernández","Miguel Sánchez",
                "Isabel Gómez","Francisco Díaz","Elena Fernández"]

# Función para asignar sueldos aleatorios
def asignar_sueldos():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    menor_800k = []
    entre_800k_2m = []
    mayor_2m = []

    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menor_800k.append((trabajadores[i], sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre_800k_2m.append((trabajadores[i], sueldo))
        else:
            mayor_2m.append((trabajadores[i], sueldo))

    # Imprimir clasificación
    print("\nSueldos menores a $800.000")
    print(f"TOTAL: {len(menor_800k)}\n")
    for empleado, sueldo in menor_800k:
        print(f"{empleado}\t${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre_800k_2m)}\n")
    for empleado, sueldo in entre_800k_2m:
        print(f"{empleado}\t${sueldo}")

    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(mayor_2m)}\n")
    for empleado, sueldo in mayor_2m:
        print(f"{empleado}\t${sueldo}")

# Función para ver estadísticas
def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)

    # Media geométrica (para simplificar, calculada como promedio de logaritmos)
    media_geom = sum([log(sueldo) for sueldo in sueldos]) / len(sueldos)

    print("\nEstadísticas de Sueldos:")
    print(f"Sueldo más alto:\t${sueldo_max}")
    print(f"Sueldo más bajo:\t${sueldo_min}")
    print(f"Promedio de sueldos:\t${promedio:.2f}")
    print(f"Media geométrica:\t${exp(media_geom):.2f}")

# Función para generar reporte de sueldos
def reporte_sueldos(sueldos):
    # Abrir archivo CSV para escribir
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])

        for i, sueldo in enumerate(sueldos):
            salud = sueldo * 0.07
            afp = sueldo * 0.12
            sueldo_liquido = sueldo - salud - afp
            writer.writerow([trabajadores[i], sueldo, salud, afp, sueldo_liquido])

    print("\nReporte de sueldos generado en 'reporte_sueldos.csv'")

# Función para mostrar el menú
def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

# Función principal
def main():
    sueldos = []

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == '1':
            sueldos = asignar_sueldos()
            print("\nSueldos asignados aleatoriamente.")

        elif opcion == '2':
            if not sueldos:
                print("\nDebe asignar sueldos primero (opción 1).")
            else:
                clasificar_sueldos(sueldos)

        elif opcion == '3':
            if not sueldos:
                print("\nDebe asignar sueldos primero (opción 1).")
            else:
                ver_estadisticas(sueldos)

        elif opcion == '4':
            if not sueldos:
                print("\nDebe asignar sueldos primero (opción 1).")
            else:
                reporte_sueldos(sueldos)

        elif opcion == '5':
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()