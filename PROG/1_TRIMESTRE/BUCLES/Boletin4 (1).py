# programa que reciba 2 numeros por teclado y que muestre los numeros que hay entre ellos. ej: 5 y 3: 3,4,5.

# num1=int(input('Dime un numero'))
# num2=int(input('Dime otro numero'))
# acum=0

# if num1<num2:
#     for i in range (num1, num2+1):
#         print (i) 
# if num2<num1:
#     for i in range (num2, num1+1):
#         print (i)
# else:
#     print ('Los numeros son iguales')

# num1=int(input('Dime un numero'))
# num2=int(input('Dime otro numero'))



# if num1<num2:
#     contador=num1
#     while contador <=5:
#         print (contador)
#         contador+=1
# if num2<num1:
#     contador=num1
#     while contador >=5:
#         print (contador)
#         contador-=1
# else:
#     print ('Son numeros iguales')

# # ejercicio2: programa que reciba un numero y muestre la tabla de multiplicar de ese numero

# num=int(input('Dime un número'))
# tabla=0
# while tabla <11:
#     print(f"{num}x{tabla}= {num*tabla}")
#     tabla+=1

#Ejercicio3
# num=int(input('Dime un número'))
# num2=int(input('Dime un segundo número'))
# acum=0

# if num<num2:
#     while num<num2:
#         num+=1
#         if num%11==0:
#             acum+=1
#     print (f"hay {acum} multiplos de 11")
# elif num2<num:
#     while num2<num:
#         num2+=1
#         if num2%11==0:
#             acum+=1
#     print (f"hay {acum} multiplos de 11")
# else:
# #     print ("Son iguales")

# num=int(input('Dime un número'))
# num2=int(input('Dime un segundo número'))
# acum=0
# for i in range (num, num2):
#     if i%11==0:
#         acum+=1
#         print (f"hay {acum} numeros multiplos de 11")

#Ejercicio4
# num=int(input("Dame un número: "))
# acum=0
# max=-1
# suma=0

# while num>=1 and num<=10000:
#     acum+=1
#     suma+=num
#     num=int(input("Dame un número: "))
# else:                                       #TRAS EL ELSE, METER UN IF. ¿POR QUÉ? NO HACE FALTA OTRO WHILE, TERMINA EL BUCLE. METER OTRO BUCLE NO TIENE SENTIDO.
#     if num <=0 or num>10000:
#         acum+=1
#         suma+=num
#         print(f"Fin del bucle, se ha introducido {acum} numeros ")

# if num > max:
#     max=num                         #Si num > maximo, entonces el mayor “hasta ahora” pasa a ser num, por eso  maximo = num.
#     print (f"El máximo es {max}")

# # media=suma/acum                     #La suma de los numeros la tenemos en el while y en el else if.  la suma entre el acumulador (que acumula los numeros que se guardaron)
# # # print (f"La media es de {media}")   #da la media.

# # #ejercicio5


# num=int(input('Dime un número entero positivo: '))
# i=1
# suma=0

# # while num <0:
# #     num=int(input('Debe solicitar un número entero positivo: '))

# # while i<=num:
# #     suma+=i
#     i+=1
# print (f"la suma de los numeros en el rango entre 1 y {num} es {suma}")

# num=int(input("Dame un número: "))
# suma=0
# if num<0:
#     for i in range (-1,-5,-1):
#         num=int(input("Dame un número correcto (Tienes 5 intentos): "))
# else:
#     for i in range (1,num+1):
#         suma+=i
#     print (suma)

# if num<=0:
#     print ("Numero invalido")
#     num=int(input("dime otro número"))
#     if num<=0:
#         print ("no válido")
# if num>0:
#     suma=num*(num+1)/2                            #GAUSS
#     print(f"la suma de 1 a {num} es {suma}")

# # EJ6    
# # num=int(input("Dame un número: "))
# m=int(input("Dame un segundo número: "))
# acum=0

# while num<0 or m<0:
#     print("Ambos números deben ser positivos.")
#     num=int(input("Dame un número: "))
# #     m=int(input("Dame un segundo número: "))
# # if num<m:
# #     while num<=m:
# #         acum+=num
# #         num+=1
# #     print (f"la suma entre n y m es {acum}")
# # elif m<num:
# #     while m<=num:
# #         acum+=m
# #         m+=1
# #     print (f"la suma entre n y m es {acum}")

# # #EJ7    

# # num=int(input("Dame un número: "))
# # max_num=0
# # acum=0

# # while num>100:
# #     if num>max_num:
# #         max_num=num
# #     num=int(input("Dame un número: "))
# # if num<=100:
# # #     max_num=num
# # #     print (f"el mayor numero introducido es {max_num}.")

# #ej8

# num = int(input("Dame el primer número: "))
# num2 = int(input("Dame el segundo número: "))

# acum = 0 
# i = 0
# if num>0 and num2>0:
#     if num<num2:
#         while i < num2:
#              acum += num  # Sumamos num al total
#              i += 1        # Incrementamos el contador
#              print(f"El producto de {num} x {num2} es {acum}")
#     elif num2<num:
#             while i < num2:
#                  acum += num  
#                  i += 1       
#                  print(f"El producto de {num2} x {num} es {acum}")
# elif num>0 and num2<0:

# #hacer en negativo

# #ej9

# num = int(input("Dame el primer número: "))
# num2 = int(input("Dame el segundo número: "))
# i=0
# total=num
# while total>=num2:
#     i+=1
#     total=num-(num2*i)
# print (f"el módulo de {num} y {num2} es {total}") 

# # #ej10

# cant_num = int(input("¿Cuántos números quieres introducir?: "))
# while cant_num <= 0:
#     cant_num = int(input("Debe ser un entero positivo. ¿Cuántos números?: "))

# suma = 0

# for i in range(1, cant_num + 1):
#     n = int(input("Dime un número: "))
#     suma += n

#     if i == 1: 
#         cant_maxima = n
#         cant_minima = n
#     else:
#         if n > cant_maxima:
#             cant_maxima = n
#         if n < cant_minima:
#             cant_minima = n

# media = suma / cant_num
# print(f"La media de los {cant_num} números es {media}")
# print(f"El número mayor es {cant_maxima}")
# print(f"El número menor es {cant_minima}")

# #ej11
#Centrado: espacios delante = num − f.

# for f in range (1,num+1):
#     espacio=num-f
#     print (' '* espacio +'*'*(2*f-1))

# #ej12

# num=int(input("Dame un número: "))
# acum=0
# while num<=0:
#     num=int(input("Dame un número positivo: "))
# else:
#     for i in range (1,num):
#         if num%i==0:
#             acum+=i

# if acum==num:
#     print ("El número es perfecto")
# else:
# #     print ("es imperfecto")

# num=int(input('Introduce el número de términos: '))
# suma=0
# simbolo='+'

# for i in range (1,num+1):
#     suma+=1/i
#     print (f"1/{i}"), print (simbolo)
# print (f"la suma de todos es {(suma)}")

# #ej15

# num=int(input('Introduce el número: '))
# factorial=1
# acum=0
# if num==0:
#     print ("Su factorial es 1")
# else:
#     for i in range (1,num+1):
#         factorial*=i
#         print (factorial)

#FIN