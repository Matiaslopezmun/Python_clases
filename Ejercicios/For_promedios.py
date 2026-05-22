## Pida la cantida de alumnos
## Pida cada cantidad de notas x alumno
## Saque el promedio y muestre si aprueba o no


# alumnos=int(input("Ingrese la cantidad de alumnos: "))

# for i in range(alumnos):
#     suma_notas=0

#     print(f"\n--- Datos del aluumno {i+1} ---")
#     n=int(input("Ingrese cantidad de notas del alumno: "))

#     for j in range(n):
#         nota=float(input(f" Ingrese la nota {i+1}: "))
#         suma_notas=suma_notas+nota

#     promedio=suma_notas/n
#     print(f"Su promedio es de: {promedio:.2f}")


alumnos=int(input("Ingrese la cantidad de alumnos: "))

for i in range(alumnos):
    suma=0

    print("--- Datos del alumno", i+1, "---")
    n=int(input("Ingrese cantidad de notas del alumno: "))

    for j in range(n):
        nota=float(input("Ingrese la nota: "))
        suma=suma+nota

    promedio=suma/n

    if promedio>=4.0:
        print("Su promedio es de:", promedio, "y usted ha APROBADO")

    else:
        print("Su promedio es de:", promedio, "y usted ha REPROBADO")