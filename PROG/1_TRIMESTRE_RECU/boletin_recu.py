# #ejercicio1

# def obtener_ganancia (cantidad, anios, interes):
#     interes_formula=interes/100
#     resultado_ganancia=0
#     acum=0
#     for i in range (anios):
#         resultado_ganancia=cantidad+(interes_formula*cantidad)
#         cantidad=resultado_ganancia

#     acum+=resultado_ganancia
#     return acum

# assert (obtener_ganancia(100,3,10))==133.1

#ejercicio3
# lista1=[1,1,2,3,5,8,1,1,9,15,9]

# def contar_numeros (lista):
#     nueva_lista=[]
#     nueva_lista_def=[]
#     acum=0
#     numero=1

#     for i in range (len(lista)):
#         while numero in lista:
#             lista1.remove(numero)
#             acum+=1
#             if numero not in lista:
#                 nueva_lista.append(numero)
#                 nueva_lista.append(acum)
#                 nueva_lista_def.append(nueva_lista)
#                 nueva_lista=[]
#                 numero+=1
#                 acum=0
#         if numero not in lista:
#             numero+=1
#     return nueva_lista_def

# assert (contar_numeros(lista1))==[[1, 4], [2, 1], [3, 1], [5, 1], [8, 1], [9, 2], [15, 1]]


#ejercicio4

# numero_nick=100
# lista_users=[]
# lista_con_contra=[]
# def alta_user (nombre, apellido1):
#         global numero_nick

#         nick=nombre[0:3]+apellido1[0:3]+str(numero_nick)
#         lista_users.append(nick)
#         numero_nick+=1
#         print(f"tu usuario es {nick}")
#         again=str(input("¿Quieres hacer otro usuario?: "))

#         while again != "Si" and again != "No":
#             print ("Dime algo válido")
#             again=str(input("¿Quieres hacer otro usuario?: "))

#         else:
#             if again=="si" or again== "Si":
#                 nick=""
#                 nombre_user=input("Dime tu nombre: ")
#                 apellido1_user=input("Dime tu primer apellido: ")
#                 apellido2=input("Dime tu segundo apellido: ")
#                 alta_user(nombre=nombre_user, apellido1=apellido1_user)

#             elif again=="no" or "No":
#                 menu_inicio()
#         return nick

# def definir_contra (nombrereg):
#     print ("Vamos a definir tu contraseña")
#     if nombrereg in lista_users:
#         password= input("Define una contraseña: ")
#         lista_con_contra.append([nombrereg,password])
#     else:
#         print ("Tu usuario no está registrado.")
#     return password, lista_con_contra


# def logueo ():
#     e=2
#     user= input("Dime tu usuario: ")
#     passw= input("Dime tu contraseña: ")
#     for i in range (len(lista_con_contra)):
#         if lista_con_contra[i][0]==user and lista_con_contra[i][1]==passw:
#             print ("Correcto")
#             menu_inicio()
#         else:
#             while e>=0:
#                 passw=input(f"Di la contraseña correcta. Te quedan {e} intentos")
#                 e-=1
#             else:
#                 print ("Cuenta bloqueada")
#     return lista_con_contra
# def menu_users ():
#     for i in range(len(lista_con_contra)): 
#         lista_con_contra[i][1] = "*" * len(lista_con_contra[i][1])
#     print (lista_con_contra[i], "\n" )
#     menu_inicio()
#     return lista_con_contra
        

# def menu_inicio():
#     print("Bienvenido de nuevo.")
#     print ("=======MENÚ=======\n")
#     print ("- Pulsa A para el alta de usuario")
#     print ("- Si ya te diste de alta, pulsa L para definir contraseña y loguearte.")
#     print ("- Pulsa I para mostrar la Información de Usuarios. \n")

#     option=input("Elige una opción: ")

    
#     while option != "I" and option != "L" and option!="A":
#         option=input("Di una opción correcta: ")


#     if option == "A":
#         nombre_user = input("Dime tu nombre: ")
#         apellido1_user = input("Dime tu primer apellido: ")
#         apellido2 = input("Dime tu segundo apellido: ")
#         alta_user(nombre=nombre_user, apellido1=apellido1_user) 
        
#     elif option == "L":
#         nombre_registrado = input("Dime tu usuario: ")

#         if nombre_registrado not in lista_users:
#                 print ("No está en la lista de usuarios")
#         else:
#                 definir_contra(nombrereg=nombre_registrado)
#         pregunta=input("¿Quieres pasar al logueo?")
        
#         if pregunta=="Si" or pregunta== "si":
#             logueo()

#         elif pregunta=="No" or pregunta== "no":
#             nombre_registrado = input("Dime tu usuario: ")
#             if nombre_registrado not in lista_users:
#                 print ("No está en la lista de usuarios")
#             else:
#                 definir_contra(nombrereg=nombre_registrado)
            
#     elif option== "I":
#         menu_users()

# menu_inicio()


#EJERCICIO5

# función que reciba un número e indique si es
# primo o no. Diseña otra que reciba dos valores (límite inferior, límite superior) y devuelva
# todos los números primos contenidos en ese rango

# numero primo: mayores que 1 que solo tienen dos divisores exactos: el 1 y el propio número.

# def es_primo (numero):
#     acum=0
#     num=1
#     for i in range (numero):
#         if numero%num==0:
#             acum+=1
#         num+=1
#     if acum==2:
#         print ("Es primo")
#     else:
#         print ("No es primo")

# es_primo (3)

# lista1 = [2, 3, 15, 7, 8, 9, 54, 2, 9, 6, 4, 2, 90, 7]
# listaprimos = []

# def es_primo(lista):
#     for i in range(len(lista)):
#         acum = 0
#         num = 1
#         for e in range(lista[i]):
#             if lista[i] % num == 0:
#                 acum += 1
#             num += 1
        
#         if acum == 2:
#             listaprimos.append(lista[i])

#     return listaprimos

# es_primo(lista1)


#Ejercicio6

# matriz=[[1,2,3],[4,5,6],[7,8,9]]

# def determinante_3x3(m):
#     det = (
#         m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
#         - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
#         + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
#     )
#     print (det)
#     return det

# determinante_3x3(matriz)

#De 4x4 lo he intentado pero no he dado con la tecla.