numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    mensaje = f"{i}. "
    divisibilidad = ""

    if i % 2 == 0:
        divisibilidad += "Divisible por 2"
    if i % 3 == 0:
        divisibilidad += " y " if divisibilidad else ""
        divisibilidad += "Divisible por 3"
    if i % 5 == 0:
        divisibilidad += " y " if divisibilidad else ""
        divisibilidad += "Divisible por 5"

    print(mensaje + divisibilidad)
