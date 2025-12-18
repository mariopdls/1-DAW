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

# ej5

# necesito un programa que pida dos numeros enteros y muestre los diez primeros multiplos del primero desde el segundo.

num1= int(input("Dime un número: "))
num2= int(input("Dime un segundo número: "))
contador=0
for i in range (num2, num2*6):
    while i%num1==0:
        print (i)
        i+=1

#ej6

# n= (int(input("Dime un número: ")))

# while n != 1:
#     print(n)  # imprime cada número en su propia línea
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1
# print (1)


#     #13 es impar, 13 (num) hace else
#  https://github.com/mariopdls/1-DAW.git   #siguiente vuelta num=40
#     # ¿como guardo el 40?

# #ej7

# day=int (int(input("Dime el día: ")))
# month= (int(input("Dime el mes: ")))
# year= (int(input("Dime el año: ")))


# if month==4 or month==6 or month==9 or month==11:
#     while day<1 or day>30:
#         day=int (int(input("Dime un día válido para este mes: ")))
# elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     while day<1 or day>30:
#          day=int (int(input("Dime el un día válido para este mes: ")))
# elif month==2:
#     if year%400==0 or (year%4==0 and year%100!=0):
#         while day <1 or day>29:
#          day=int (int(input("Dime el un día válido para este mes. El año es bisiesto: ")))
#     else:
#         while day<1 or day>28:
#          day=int (int(input("Dime el un día válido de febrero: ")))


# if month==4 or month==6 or month==9 or month==11:
#     while day<1 or day>30:
#         day=int (int(input("Dime un día válido para este mes: ")))
# elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     while day<1 or day>31:
#          day=int (int(input("Dime el un día válido para este mes: ")))
# elif month==2:
#     if year%400==0 or (year%4==0 and year%100!=0):
#         while day <1 or day>29:
#          day=int (int(input("Dime el un día válido para este mes. El año es bisiesto: ")))
#     else:
#         while day<1 or day>28:
#          day=int(input("Dime el un día válido de febrero: "))

# print (f"La fecha es {day}/{month}/{year}.")
#     #ya tengo el programa que imprime 10 numeros desde el segundo numero. ahora tiene que mostrar los 10 primeros multiplos del primer numero
#     #2 y 5-> 6, 8, 10, 12, 14, 16, 18, 20 22 24
# #ahora añadir un dia mas

# day+=1
# if month == 4 or month == 6 or month == 9 or month == 11:
#     if day > 30:
#         day = 1
#         month += 1
# elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
#     if day > 31:
#         day = 1
#         month += 1
# elif month == 12: #diciembre aparte por el cambio del año
#     if day > 31:
#         day = 1
#         month = 1
#         year += 1
# elif month == 2:
#     if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#         limite = 29
#     else:
#         limite = 28
#     if day > limite:
#         day = 1
#         month += 1

# print(f"Día siguiente: {day}/{month}/{year}.")

# #ej8

# num=int(input("dime un número positivo mayor que 0: "))
# i=1
# termino1=0
# termino2=1
# acum=0
# acum+=0
# cadena= ""
# while num <=0:
#     num=int(input("dime un número positivo mayor que 0"))
# else:
#     for i in range (1,num+1):
        
#         cadena+= print(termino1)
#         resultado=termino1+termino2
#         termino1=termino2
#         termino2=resultado

#cada termino es igual a la suma de los dos anteriores

#ej9: XD

# # ej10
# edad=int(input("Di la edad: "))

# dinero1=20
# dinero2=0
# dinerototal=0
# acum=0

# puzzle1=1
# puzzle2=0
# puzzlestotal=0
# acum2=0

# while edad<=0 or edad>100:
#     edad=int(input("Di una edad válida: "))
# else:
#     if edad%2==0:
#         for i in range(2, edad + 1, 2):   # solo años pares
#             dinerototal= dinero1+dinero2
#             acum+=dinerototal
#             print (f"acumula {acum} y recibe {dinerototal}")
#             dinero2+=15
#     if edad%2 != 0:
#         for i in range(1, edad + 1, 2):   # solo años impares
#             puzzlestotal= puzzle1+puzzle2
#             acum2+=puzzlestotal
#             print (f"acumula {acum2} y recibe {puzzlestotal}")
#             acum2+=puzzlestotal
#             puzzle2 *= 2 
