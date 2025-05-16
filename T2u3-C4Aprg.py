print("**********Bienvenido al Programa**********")
print("Seleccione un numero segun la opcion seleccionada")
print("\n")
print("1. Contador de centenas, decenas y unidades")
print("2. Ingrese un numero y calculare sus primeros 9 multiplos")
print("3. Salir")
print("\n")
op = int(input("Ingrese un numero segun opcion: "))
centena = 0
decena = 0
unidad = 0
if op == 1:
    repeticiones = 0
    centena = 0
    decena = 0
    unidad = 0
    print("Bienvenido a el Programa 1!!!")
    for repeticiones in range(0,10):
        calcular_numero = int(input("Ingrese un numero positivo: "))
        while calcular_numero >= 1000 or calcular_numero <= 0:
            print("Ingrese un numero valido")
            calcular_numero = int(input("Ingrese un numero positivo: "))
        if calcular_numero >= 100 and calcular_numero < 1000:
            centena += 1
        elif calcular_numero >= 10 and calcular_numero <100:
            decena += 1
        else:
            unidad += 1
    print("Numero de centenas: {}, Numero de decenas {}, Numero de unidades {} (Segun numeros proporcionados)".format(centena, decena, unidad))
elif op == 2:
    multiplos = 1
    print("Bienvenido a el Programa 2!!!")
    numero = int(input("ingrese un numero entero y positivo: "))
    if numero <= 0:
        print("Ingrese un numero valido")
    else:
        print("Segun {}, el numero proporcionado, la tabla seria la siguiente:")
        while multiplos < 10:
            print("{} * {} = {}".format(numero, multiplos, numero * multiplos))
            multiplos += 1
elif op == 3:
    print("Ten un gran dia!!!")
else:
    print("Ingresa una opcion valida.")
        
        
