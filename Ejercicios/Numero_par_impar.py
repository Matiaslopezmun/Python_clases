numero=int(input("Ingrese un numero entero positivo: "))
npar=0
nimpar=0

for i in range(1, numero):
    if i%2==0:
        npar+=1
        print(f"El {i} es PAR")

    else:
        nimpar+=1
        print(f"El {i} es IMPAR")

print(f"El numero total de numeros pares es de {npar}")
print(f"El numero total de numeros impares es de {nimpar}")