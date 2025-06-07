
numero_cierto = -2  
adivinado = False
cantidad_intentos = 0
cantidad_maxima_intentos = 2

print("El ejercicio consiste en adivinar el valor de x que cumple la ecuación: x - 14 + 4x + 24 = 0")

while not adivinado and cantidad_intentos < cantidad_maxima_intentos:
    try:
        entrada = int(input("Debes ingresar el valor de X que consideras que resuelve la ecuación: ")) 
        cantidad_intentos += 1

        if entrada == numero_cierto:
            print("¡Has adivinado el valor de X!")
            adivinado = True
        elif entrada < numero_cierto:
            print("Pista: el valor de x es mayor al seleccionado.")
        else:
            print("Pista: el valor de x es menor al seleccionado.")
    except ValueError:
        print("¡Debes ingresar un número!")

if not adivinado:
    print("No lograste adivinar el valor de X. La respuesta correcta era -2.")
