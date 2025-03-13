"""Crear un programa el cual pida 3 numeros y
muestre en pantalla cual es el mayor de los tres"""

#Darle la bienvenida al usuario
print("Bienvenido al programa")

#SOlicitar numeros
num1 = int(input("Proporcioname un numero: "))
num2 = int(input("Proporcioname otro numero: "))
num3 = int(input("Proporcioname un ultimo numero: "))

#Denotar errores de numeros iguales
if num1 == num2 and num1 == num3:
        print("Todos los numeros son iguales")
if num1 == num2 or num3 == num2 or num3 == num1:
        print("Dos numeros son iguales numeros son iguales")
        
#Denotar numeros negativos
if num1<0 or num2<0 or num3<0:
        print("Uno o mas numeros proporcionados son negativos")
        
#Definir numero 1 mayor
else:
    if num1>num2 and num1>num3:
        print("El primer numero: {} proporcionado es mayor que el numero 2: {} y numero 3: {}".format(num1, num2, num3))
        
#Definir numero 2 mayor        
    else:
        if num2>num1 and num2>num3:
            print("El segundo numero: {} proporcionado es mayor al numero 1: {} y numero 3: {}".format(num2, num1, num3))
            
#Definir numero 3 mayor            
        else:
            if num3>num1 and num3>num2:
                print("El tercer numero: {} proporcionado es mayor al numero 1: {} y numero 2: {}".format(num3, num1, num2))

        
            

    
      
      
