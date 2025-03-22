n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))

if n1 > n2:
    for i in range(n1 * n2, n1 - 1, -1):
        if i % n1 == 0 and i % n2 == 0:
            mcm = i
else:
    if n1 < n2:
        for i in range(n1 * n2, n2 - 1, -1):
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
    else:
        mcm = n2

suma = n1+n2 

if suma % 2 == 0:

 print(f'{int(mcm)} es el minimo comun multiplo de {n1} y {n2}')
else:
 
  MCD = int(n1*n2/mcm)
 
  print(f'{MCD} es el maximo comun divisor de {n1} y {n2}')