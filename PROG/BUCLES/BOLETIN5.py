# #EMPEZAR BOLETIN

# num=int(input("Dime un número: "))
# num2=int(input("Dime un segundo número: "))
# cont=1
# for i in range (1,num+1):
#     cadena=""
#     for e in range (i):
#         cadena+= str(cont) + " "
#         cont+=1
#     print (cadena)

#SEGUIR con binario

# #EJ3
# x=(int(input("Dime el valor de x: ")))
# terminos=(int(input("Dime el numero de terminos: ")))
# potencia=1
# suma=0
# for i in range (terminos):
#     if i % 2 == 0:
#         termino = x ** potencia
#     else:
#         termino = -(x ** potencia)---
#     potencia+=2
#     suma+=terminos
# print (suma)

#ej4
# num=int(input("Dime un número: "))
# uno="1"
# cadena= " "
# contador=0
# for i in range (num):
#     cadena+= f"{uno} +" + " "
#     contador+=int(uno)
#     uno+="1"
# print (cadena[:-2])

# print (contador)

#ej5

#necesito un programa que pida dos numeros enteros y muestre los diez primeros multiplos del primero desde el segundo.

# num1= int(input("Dime un número: "))
# num2= int(input("Dime un segundo número: "))
# contador=0
# for i in range (num2, num2*6):
#     while i%num1==0:
#         print (i)
#         i+=1

#     #ya tengo el programa que imprime 10 numeros desde el segundo numero. ahora tiene que mostrar los 10 primeros multiplos del primer numero
#     #2 y 5-> 6, 8, 10, 12, 14, 16, 18, 20 22 24

#ej6

# num= (int(input("Dime un número: ")))

# for i in range (0, num, -1):


# #num/2 es par
# #num*3+1 si es impar


def nombre_accion () :
    print ("hola")
    return

print (nombre_accion())