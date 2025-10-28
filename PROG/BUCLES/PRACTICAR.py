
# num=int(input("Dime un número entero"))
# acumpositivos=0
# acumnegativos=0
# acumpares=0
# acumimpares=0

# while num!=0:
#     if num%2==0:
#         acumpares+=1
#     else:
#         acumimpares+=1
#     if num>0:
#         acumpositivos+=1
#     elif num<0:
#         acumnegativos+=1
#     num=int(input("Dime un número entero: "))
# else:
#     print (f" Fin del programa. Hay {acumpares} números pares, {acumimpares} números impares, {acumpositivos} números positivos y {acumnegativos} números negativos")

#2
# num=int(input("Dime un número entero"))
# limite= int(input("Dime un limite para la tabla"))

# for i in range (0,limite+1):
#     print (f" {num} x {i} = {num*i}")

# #3

# num=int(input("Dime un número entero"))
# impares=0
# acumimpar=0

# # while num<0:
# #     print ("Tiene que ser entero positivo")
# # else:
# #     for i in range (0, num+1):
# #         if i%2!=0:
# #             impares+=1
# #             acumimpar+=i

# # print (f"Hay {impares} números impares y su suma es de {acumimpar}")

# #4

# notas=int(input("Dime una nota. Tienes 3 intentos: "))
# intentos=10
# notasvalidas=0
# notasinvalidas=0
# media=0
# aprobado=0
# suspenso=0
# intentos=0
# intentos_maximos=10
# sumanotas=0

# while intentos<intentos_maximos:
#     notas=int(input("Dime una nota"))
#     intentos+=1

#     while notas <0 or notas >10:
#         notas=int(input("Dime una nota válida"))
#         notasinvalidas+=1
#     else:
#         notasvalidas+=1
#         sumanotas+=notas
#         if notas>=5 and notas <=10:
#             aprobado+=1
#         elif notas >=0 and notas<=4:
#             suspenso+=1
# media=notasvalidas/10


# print (f"Hay {notasinvalidas} notas inválidas. Hay {notasvalidas} notas válidas. La nota media de las notas válidas es {sumanotas}. Hay {aprobado} aprobados y {suspenso} suspensos")


# num=int(input("Dime un numero. "))
# num2=int(input("Dime un numero 2. "))
# num3=int(input("Dime un numero 3. "))

# if num>num2 and num>num3:
#     print (f"{num} es el mayor")
# elif num2>num and num2>num3:
#     print (f"{num2} es el mayor")
# elif num3>num and num3>num2:
#     print (f"{num3} es el mayor")
# else:
#     print ("son iguales")

# if num<num2 and num<num3:
#     print (f"{num} es el menor")
# elif num2<num and num2<num3:
#     print (f"{num2} es el menor")
# elif num3<num and num3<num2:
#     print (f"{num3} es el menor")

# if num2-1==num and num2+1==num3:
#     print ("son consecutivos")
# else:
#     print ("no son consecutivos")

#8 fibonasi
limite=int(input("dime un número: "))
num1=0
num2=1
suma=0
acum=0

for i in range (0, limite):
    suma=num1+num2
    print (suma)
    acum+=suma
    num1=num2
    num2=suma
print (f"La suma de los términos es {acum}")