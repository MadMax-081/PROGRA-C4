#Darle la bienvenida al usuario
print("Bienvenido al programa")

#Dar instrucciones
print("Ingrese 3 numeros ")

#Pedir numeros
num1 = int(input("Ingrese el Numero 1: "))
num2 = int(input("Ingrese el Numero 2: "))
num3 = int(input("Ingrese el Numero 3: "))

#Denotar numeros negativos
if num1<0 or num2<0 or num3<0:
        print("Uno o mas numeros proporcionados son negativos")
else:
    #Denotar numeros iguales
    if num1 == num2 and num1 == num3:
            print("Todos los numeros son iguales")
    else:
        if num1 == num2 or num3 == num2 or num3 == num1:
                print("Dos numeros son iguales numeros son iguales")

        #Escribir numeros diferentes
        else:
            print("Los numeros {}, {}, {} son los proporcionados".format(num1, num2, num3))

