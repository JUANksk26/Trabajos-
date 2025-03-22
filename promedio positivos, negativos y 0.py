positivos = 0
negativos = 0
suma_positivos = 0
suma_negativos = 0

while True:
    numero = int(input("Ingrese un número entero (0 para salir): "))
    
    if numero == 0:
        break
    elif numero > 0:
        print("El número es positivo.")
        positivos += 1
        suma_positivos += numero
    else:
        print("El número es negativo.")
        negativos += 1
        suma_negativos += numero

if positivos > 0:
    promedio_positivos = suma_positivos / positivos
else:
    promedio_positivos = 0

if negativos > 0:
    promedio_negativos = suma_negativos / negativos
else:
    promedio_negativos = 0

print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Promedio de positivos: {promedio_positivos}")
print(f"Promedio de negativos: {promedio_negativos}")
