total_a_pagar=0
cant_cafe=0
cant_sandwich=0
menu= """

--- CAFETERÍA VIRTUAL ---
1. Comprar Café ($2.500)
2. Comprar Sandwich ($3.500)
3. Ver total actual
4. Salir y Pagar
"""
while True:
    print(menu)
    try:
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                print("Usted a seleccionado Cafe")
                total_a_pagar+=2500
                cant_cafe+=1

            case 2:
                print("Usted a seleccionado Sandwich")
                total_a_pagar+=3500
                cant_sandwich+=1

            case 3:
                print(f"El total a pagar es de ${total_a_pagar}.")

            case 4:
                print(f"Usted ha comprado:\nCafes:{cant_cafe} \nSandwich:{cant_sandwich} \nUsted debe pagar: ${total_a_pagar}")
                break
            case _:
                print("Ingrese una opcion valida")
    except:
        print("## Ingrese caracteres validos ##")