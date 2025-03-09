texto = input("Introduce una frase: ")

palabra = ""
for caracter in texto:
    if caracter == " ":
        if palabra:
            print(palabra)
            palabra = ""
    else:
        palabra += caracter

if palabra:
    print(palabra)
