N = int(input("Introduce un número entero: "))
base = int(input("Introduce la base (2, 4, 8 o 16): "))
B = "ABCDEF"

resultado = ""
numero = N 

if base == 16:
    while numero > 0:
        residuo = numero % 16
        if residuo > 9:
            resultado = B[residuo - 10] + resultado  
        else:
            resultado = str(residuo) + resultado
        numero //= 16

elif base in [2, 4, 8]:
    while numero > 0:
        resultado = str(numero % base) + resultado
        numero //= base

else:
    print("Base no válida. Usa 2, 4, 8 o 16.")
    exit()


resultado = resultado if resultado else "0"

print(f"El número {N} en base {base} es: {resultado}")