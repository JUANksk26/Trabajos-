palabra = input("Introduce una palabra: ")

if palabra[0] in "aeiouAEIOU":
    pig_latin = palabra + "ción" # añadir "cion" al final de la palabra si empieza con vocal
else:
    pig_latin = palabra[1:]  + palabra[0] + "mente" # añadir "mente" al final de la palabra
# palabra 1 significa que se toma la palabra desde la segunda letra en adelante
print("Palabra en Pig Latin:", pig_latin)
