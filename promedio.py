N= int(input("ingrese el ultimo numero de la serie:"))
i = 0
ul = 0
prom = 0
while i <= N:
    if i % 2 == 0 :
       prom+=1
       ul= i + ul
    i += 1     
print(ul/prom)    