n = True

while n  == True:
    print("\nCalculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "5":
        print("Saliendo de la calculadora...")
        n = False
    
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida, intenta de nuevo.")
        continue
    
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    if opcion == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1 * num2}")
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            print(f"Resultado: {num1 / num2}")
