import time

stock=50
opcion=0
menu = """

-------------------------
    INVENTARIO TIENDA
-------------------------
1. Ver stock
2. Vender productos
3. Reponer stock
4. Salir
"""

while opcion!=4:
    print(menu)

    try:
        opcion=int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print(f"El stock disponible es {stock}")
            case 2:
                    productos=int(input("Ingrese la cantidad de productos a vender: "))
                    if productos>stock:
                        print("Stock no disponible")
                    elif productos<stock:
                        stock-=productos
                        print(f"Usted a vendido una cantidad de {productos} productos.")
            case 3:
                  reponer=int(input("Ingrese la cantidad de productos a reponer: "))
                  stock+=reponer
                  print(f"A reponido con exito {reponer}")
            case 4:
                  print("Cargando...")
                  time.sleep(2)
                  print("Gracias por utilizar el sistema.")              
    except ValueError:
        print("#ERROR / Solo puede ingresar numeros enteros")
        opcion=0