monto=100000
opcion=0
menu = """
-------------------------
    CAJERO AUTOMATICO
-------------------------
1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Salir
"""

while opcion!=4:
    print(menu)

    try:
        opcion=int(input("Seleccione una opcion: "))
    
        match opcion:
            case 1:
                print(f"Su saldo es de ${monto}")
                input("\nPresione Enter para continuar...")
            case 2:
                retirar=int(input("Ingrese la cantidad de dinero que desea retirar: "))
                if retirar>monto:
                    print("Saldo insuficiente")
                elif retirar%5000==0:
                    monto-=retirar
                    print(f"Usted a retirado exitosamente ${retirar}")
                else:
                    print("Solo puedes retirar con multiplos de $5000")
                input("\nPresione Enter para continuar...")
            case 3:
                depositar=int(input("Ingrese la cantidad de dinero que desea depositar: "))
                monto+=depositar
                print(f"Su deposito de ${depositar} fue realizado con exito")
                input("\nPresione Enter para continuar...")
            case 4:
                print("Gracias por usar el sistema")
                input("\nPresione Enter para continuar...")
            case _:
                print("Opcion no valida")
                input("\nPresione Enter para continuar...")

    except ValueError: 
        print("#ERROR / Solo puede ingresar numeros enteros")
        opcion=0