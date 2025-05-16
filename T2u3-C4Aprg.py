#Mensajes introductorios
print("**********Bienvenido al Programa**********")
print("Seleccione un numero segun la opcion seleccionada")
print("\n")
#Presentando opciones
print("1. Contador de centenas, decenas y unidades")
print("2. Ingrese un numero y calculare sus primeros 9 multiplos")
print("3. Salir")
print("\n")
#Pedirle al usuario que escoja una de las opciones anteriormente presentadas
op = int(input("Ingrese un numero segun opcion: "))
#Seleccion 1
if op == 1:
    #Declarando variables necesarias para el desarrollo del programa
    repeticiones = 0
    centena = 0
    decena = 0
    unidad = 0
    #Mensaje Introductorio al Programa 1
    print("Bienvenido a el Programa 1!!!")
    #Ciclo que hace que dicho programa se repitar 10 veces
    for repeticiones in range(0,10):
        #Pide numero que cumpla los criterios
        calcular_numero = int(input("Ingrese un numero positivo: "))
        #Si el numero no cumple con los criterios no le deja avanzar
        while calcular_numero >= 1000 or calcular_numero <= 0:
            print("Ingrese un numero valido")
            calcular_numero = int(input("Ingrese un numero positivo: "))
        #Verifica si es centena
        if calcular_numero >= 100 and calcular_numero < 1000:
            centena += 1
        #Verifica si es decena
        elif calcular_numero >= 10 and calcular_numero <100:
            decena += 1
        #Verifica si es unidad
        else:
            unidad += 1
    #Imprime resultados
    print("Numero de centenas: {}, Numero de decenas {}, Numero de unidades {} (Segun numeros proporcionados)".format(centena, decena, unidad))
#Seleccion 2
elif op == 2:
    #Declarar variables necesarias
    multiplos = 1
    #Mensaje introductorio al Programa 2
    print("Bienvenido a el Programa 2!!!")
    #Pide numero que cumpla con los criterios
    numero = int(input("ingrese un numero entero y positivo: "))
    #Descarta errores de numeros negativos
    if numero <= 0:
        print("Ingrese un numero valido")
    #SiNo hay negativos continua con el proceso
    else:
        #Aclaracion de el numero seleccionado
        print("Segun {}, el numero proporcionado, la tabla seria la siguiente:")
        #Ciclo While para ascender de 1 en 1 los multiplos del 1 al 9 
        while multiplos < 10:
            #Estableciendo l formula y que se repita las veces que establece el Bucle While
            print("{} * {} = {}".format(numero, multiplos, numero * multiplos))
            multiplos += 1
#Seleccion 3
elif op == 3:
    #Dar por finalizado el programa
    print("Ten un gran dia!!!")
#De no ser asi    
else:
    #Establecer que el numero seleccionado no tiene una opcion designada en el menu
    print("Ingresa una opcion valida.")
