
#1

# def quitar_prep(empresa):
#     excluir = ["a", "ante", "bajo", "de"]
#     palabras = empresa.split()
#     resultado = [p for p in palabras 
#         if p.lower()
#         not in excluir]
#     return resultado



# def poner_acronimo(empresa):
#     palabras = empresa.split()
#     resultado = [p[0].upper() for p in palabras if p]
#     texto=""
#     for letra in resultado:
#         texto += letra
#     return texto

# print(poner_acronimo("Empresa de Seguros"))

#2


# def convertir_camelCase (cadena):
#     cadenapalabras=cadena.split()
#     cadenapalabras[1] = cadenapalabras[1][:1].upper() + cadenapalabras[1][1:]
#     resultado= cadenapalabras[0] + cadenapalabras[1] + cadenapalabras[2]
#     print (resultado)

# convertir_camelCase("hola mundo cruel")

# # #3

# def suma_num (cadenanum):
#         acum="0"
#         acumnumero=0
#         for i in cadenanum:
#                 if i in "1234567890":
#                         acum+=i
#                 else:
#                         acumnumero+=int(acum)
#                         acum="0" #acum vuelve a cero para no empezar a acumular los numeros de nuevo, y dé las sumas bien.
#         return acumnumero+int(acum)


# print (suma_num ("23a2"))
    
#4


# def rotar_cadena (cadena, n):
#     return cadena[n:] + cadena[:n]           #ponemos el inicio en [n: ] y el final en [ :n], pues es [inicio:fin]

# print (rotar_cadena ("Python", 4))
# print (rotar_cadena ("Hola buenas tardes",-5))

#TAREACLASE DNI

# LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

# def es_dni_valido(dni):
#     valido = False

#     if 8 <= len(dni) <= 9:
#         resto = int(dni[:-1]) % 23
#         letra = LETRAS[resto]
#         valido = letra == dni[-1]

#     return valido


# def es_dni_valido_refactor(dni):
#     return 8 <= len(dni) <= 9 and LETRAS[int(dni[:-1]) % 23] == dni[-1]


# # Pruebas
# assert(not es_dni_valido("1111111L"))
# assert(not es_dni_valido("11111"))
# assert(es_dni_valido("11111111H"))

# assert(not es_dni_valido_refactor("1111111L"))
# assert(not es_dni_valido_refactor("11111"))
# assert(es_dni_valido_refactor("11111111H"))

# #5

# def charactersInString(cadena, caracter):
#     cuenta = 0
#     for i in cadena.lower():          # usa otro nombre
#         if i == caracter.lower():     # compara
#             cuenta += 1
#     return cuenta
# print (charactersInString ("buenosdias","a"))


# #  #6

# def lowcaseinstrring(cadena):
#     cuenta=0
#     for i in cadena:  #bucle para que i cuente si es minuscula o no
#         if i== i.lower():
#             cuenta+=1
#     return cuenta
# print (lowcaseinstrring("HOLABuenosDIASquetal"))

# #7

# def numberinstring(cadena):
#     cuenta=0
#     for i in cadena:
#         cadena
#         if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
#             cuenta+=1
#     return cuenta
# print (numberinstring("holabuenosdias23323"))

# #8

# def palindromo (cadena):
#     texto=""
#     espacios=" "
#     acum=""
#     acumcadena=""
#     for j in cadena:
#         if j != espacios:
#             acumcadena+=j
#     for i in range (len(cadena)-1, -1,-1): #para i en el rango de la longitud de cadena, empieza en -1, avanza hasta -1 con saltos de -1
#         texto+=(cadena[i])
#     for e in texto:
#         if e != espacios:
#             acum+=e
#     if acumcadena==acum:
#         print ("es palíndromo")
#     else:
#         print ("no es palindromo")
#     return ""
# print (palindromo ("se es o no se es"))


#CLASE

# cadena="hola"
# lista_numeros=  [1,3,5,7,9]
# print (lista_numeros[0])

# # #crear lista 50 numeros pares

# lista=[]
# num=0
# for i in range (num,101):
#     if i%2==0:
#         lista.append (i)

# print (lista)

#10

# número que es igual a la suma de sus propios dígitos elevados cada uno a la potencia del número total de dígitos que tiene.

# def es_armstrong (num):
#     num=str(num)
#     if len(num[0])**3 == num[0] and  len(num[1])**3 == num[1] and len(num[1])**3 == num[1]:
#         print ("Es armstrong")
#     else:
#         print ("No es armstrong")
#     return ""

# print (es_armstrong (153))

# def numAmstrong(num):
#     num=str(num)
#     suma=0
#     for i in num:
#         digito=int(i)**(len(num))
#         suma+=digito
#     if suma==int(num):
#         print(num, "Es un numero de Amstrong")
#     else:
#         print(num, "No es un numero de Amstrong")
#     return suma


# print(numAmstrong(num=(int(input("Dime un numero: "))))) #sus propios dígitos, elevados cada uno a la po sus propios dígitos, elevados cada uno a la po

#13
#funcion que tenga como parametro tres cadenas.
# la primera, una frase que debe comprobar si existe el segundo parámetro
#la segunda, una palabra
#la tercera, el reemplazo para la segunda palabra

#ejemplo: cadena= hola buenas tardes palabra= tardes reemplazo= mañanas


# def hacer_reemplazo(cadena, palabra, reemplazo):
#     acum=""
#     espacio=""
#     cadena=cadena.split()
#     if cadena[0]==palabra:
#         cadena[0]=reemplazo
#     elif cadena[1]==palabra:
#         cadena[1]=reemplazo
#     elif cadena[2]==palabra:
#         cadena[2]=reemplazo
#     else: print ("No hay nada que reemplazar")

#     if cadena[0]==reemplazo or cadena[1]==reemplazo or cadena[2]==reemplazo:
#         for i in range (len(cadena)):
#             acum+=cadena[i] + " "
#             i+=1
#         print (acum)
#         return acum

# hacer_reemplazo("Hola buenas tardes", "tardes", "mañanas")

#14

# #15

# def contar_vocales (palabra):
#     lista=["a","e","i","o","u"]
#     acum=0
#     if lista[0] in palabra:
#             acum+=1
#     if lista [1] in palabra:
#             acum+=1
#     if lista [2] in palabra:
#             acum+=1
#     if lista [3] in palabra:
#             acum+=1
#     if lista [4] in palabra:
#             acum+=1
#     print (acum)
#     return acum
# contar_vocales("abaco")

#16

# def contar_letras (palabra):
#     acum=0
#     i="asdfghjklñwertyuiopqzxcvbnm"
#     for i in palabra: 
#         acum+=1
#     print (acum)
#     return acum
# contar_letras("abaco")
# contar_letras("hamburguesa")

# #17

# #poner vocales en un acumulador y consonantes en otro

# def es_ordenado (cadena):
#     acum=""
#     acumcons=""
#     for i in cadena:
#         if i== " ":
#             i=""
#         elif i=="a":
#             acum+=i
#         elif i=="e":
#             acum+=i
#         elif i=="i":
#             acum+=i
#         elif i=="o":
#             acum+=i
#         elif i=="u":
#             acum+=i
#         else:
#             acumcons+=i
#     print (f"{acumcons} {acum}")

# es_ordenado ("curso de programacion")

# #18

# def num_palabras (cadena):
#     cadena=cadena.split()
#     print (len(cadena))
# num_palabras ("hola me llamo antonio")

#clase

def palabra_escondida(palabra,palabraescondida):
    acum=""
    for i in palabra:
        for e in palabraescondida:
            if e==i:
                acum+=e
    if palabraescondida in acum:
        print ("Hola")

palabra_escondida("supercalifragilisticoespialidoso","rapido")
