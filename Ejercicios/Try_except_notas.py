while True:
    try:
        nota=float(input("Ingrese su nota: "))
        if nota<1.0 or nota>7.0:
            print("Ingrese una nota valida")
        elif nota>=4.0:
            print("Aprovado")
            break
        elif nota<4.0:
            print("Reprobado")
            break
    except:
        print("Solo puede ingresar numeros decimales")