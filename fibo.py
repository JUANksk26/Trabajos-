n = int(input("Ingrese un numero entero:"))
pn = 0
ul = 1
i = 2

while i < n :
    suma = pn+ul
    pn = ul
    if ul > n:
        print (pn)
        i=n
    ul = suma
    i += 1
    
