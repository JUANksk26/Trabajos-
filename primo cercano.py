m = int(input("Ingrese un número:"))
for n in range(2, m+1):
    divisores = 0
    i = 2

    while i < n:
        if n % i == 0:
            divisores += 1
        i += 1

    if divisores <= 0:         
        primo=n
print(primo)          