N = int(input("Introduce un número entero: "))
base = int(input("Introduce la base (2, 4, 6, 8 o 10): "))

if base not in [2, 4, 6, 8, 10]:
    print("Base no soportada. Elige entre 2, 4, 6, 8 o 10.")
else:
    if base == 10:
        print(f"El número {N} en base {base} es: {N}")
    else:
        resultado = ""
        numero = N 
        while numero > 0:
            resultado = str(numero % base) + resultado
            numero //= base
        print(f"El número {N} en base {base} es: {resultado if resultado else '0'}")


 