n = int(input("Ingrese un numero entero:"))
pn = 0
ul = 1
i = 2
print(pn)
print(ul)

while i < n :
    suma = pn+ul
    pn = ul
    ul = suma
    print(suma)
    i += 1