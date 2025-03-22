n = input("Ingrese un número entero positivo: ")

esv = True
indice = 0
while indice < len(n):
    if n[indice] < '0' or n[indice] > '9':
        es_valido = False
    indice += 1

if esv and n[0] != '0':
    nuevo_numero = ""
    for digito in n:
        nuevo_digito = (int(digito) + 1) % 10
        nuevo_numero += str(nuevo_digito)
    
    print(f"Número transformado: {nuevo_numero}")
else:
    print("Entrada no válida. Debe ingresar un número entero positivo.")