N = int(input("ingrese un numero entero: "))
if N**1/3 % 1 == 0:
    resultado = (N**1/3)
    print(f'{N} tiene raiz cuadrada entera  y es {resultado} ')
else:
    print(f'{N} No tiene raiz cuadrada entera')