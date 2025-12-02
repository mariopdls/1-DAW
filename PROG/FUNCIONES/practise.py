# import re
# def validacionDNI (dni):
#     patron='^[0-9]{8}[A-Z]{1}'
#     if re.match (patron, dni):
#         print ("Dni correcto")
#     else:
#         print ("Dni incorreto")

# validacionDNI ("28986934B")
# validacionDNI("boregsa")

# def calcularletra(dni):
#     letras="TRWAGMYFPDXBNJZSQVHLCKE"
#     numero=int(dni)
#     acum=""
#     resultado=numero%23
#     for i in range (len(letras)):
#         if letras[i]==letras[resultado]:
#             acum+=letras[i]
#     print (f"la letra que le corresponde es {acum}")

# calcularletra("28986934")

# def dnicompleto (dni):

#     if len(dni) != 8:
#         print ("Ponga los 8 numeros del dni para calcular su letra")
#     else:
#         letras="TRWAGMYFPDXBNJZSQVHLCKE"
#         dni=int(dni)
#         resultado=dni%23
#         acum=""
#         for i in range (len(letras)):
#             if letras[i]==letras[resultado]:
#                 acum+=letras[i]
#                 print (f"La letra que le corresponde es {acum}")

#         dnicompleto=str(dni)+acum
#         import re
#         regular= '^[0-9]{8}[A-Z]{1}'

#         if re.match(regular, dnicompleto):
#             print (f"Todo Correcto, su dni completo es {dnicompleto}")
#         else:
#             print ("Lo siento, es incorrecto")

# dnicompleto("28986934")



#menu

# def buscarletra (dni):

#     print ("Quiere usted generar una letra.")
#     letras="TRWAGMYFPDXBNJZSQVHLCKE"
#     dninumero= int(dni)
#     resultado= dninumero%23
#     for i in range (len(letras)):
#         if letras[i]==letras[resultado]:
#             print (f"La letra que le corresponde es {letras[i]}")

# def dnicompleto(totaldni):
#     letras="TRWAGMYFPDXBNJZSQVHLCKE"
#     acum=""
#     import re
#     patron='^[0-9]{8}[A-Z]{1}$'
#     if re.match(patron,totaldni):
#         print ("Dni correcto en longitud")
#     else:
#         print ("Es incorrecto en longitud.")

#     print ("Ahora veremos si su letra es correcta.")
#     dnisinletra=totaldni[:8]
#     posicionletra= int(dnisinletra)%23
#     for i in range (len(letras)):
#         if letras[i]==letras[posicionletra]:
#             acum+=letras[i]
#     if acum==totaldni[8]:
#         print ("DNI correcto.")
#     else:
#         print ("Incorrecto bro")
    
# def menuopciones ():
#     menu= input("Bienvenido al menú de opciones. Seleccione una de ellas para continuar \n 1. Generar la letra de un número de dni \n 2. Validar un dni por completo \n 3. Salir del programa \n Seleccione una opción: "  )
    
#     if menu=="1":
#         dni=input("Introduzca el DNI sin número: ")
#         buscarletra(dni)
    
#     elif menu== "2":
#         print ("Usted ha seleccionado la opción de validar un DNI al completo: ")
#         totaldni=input("Digame su dni al completo")
#         dnicompleto(totaldni)
#     elif menu=="3":
#         print ("Gracias por visitarnos.")

#     return
    

# menuopciones()

# cifrado

# def cifrado (cadena, desplazamiento):
       
#     abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     acum=""
#     for i in range (len(cadena)):
#         posicion=cadena[i]
#         for e in range (len(abecedario)):
#             if abecedario[e]==posicion:
#                 acum+=abecedario[(e+int(desplazamiento))%26]
#     print (acum)
        


# cifrado ("HOLA", "3")
# cifrado ("ZIMBABUE", "5")


# def descifrado (cadena2, desplazamientoinverso):
#     abecedarioinverso= "ZYXWVUTSRQPONMLKJIHGFEDCBA"
#     acum=""
#     for i in range (len(cadena2)):
#         posicion=cadena2[i]
#         for e in range (len(abecedarioinverso)):
#             if abecedarioinverso[e]==posicion:
#                 acum+=abecedarioinverso[(e+int(desplazamientoinverso))%26] 
#     print (acum)

# descifrado ("KROD", "3")
# descifrado ("ZIGA", "3")

# def contarPalabra (cadena, palabra):
#     contador=0
#     for i in range (len(cadena) - len(palabra)+1):
#         coincidencias=0
#         for e in range (len(palabra)):
#             if cadena[i+e] == palabra[e]:
#                 coincidencias += 1
#         if coincidencias == len(palabra):
#             contador += 1
#     print (contador)

# contarPalabra("ATCGTTCTCGTTGATCTCGTTATCTCG", "CGTT")


#leerpalabra

# def contarsubcadenas (cadena1, palabrabuscar):
#     acum=0
#     for i in range (len(cadena1)- len(palabrabuscar)+1):
#         palabra_completa=""
#         for e in range (len(palabrabuscar)):

#             if cadena1[i+e] == palabrabuscar[e]:
#                 palabra_completa+=palabrabuscar[e]

#             if palabra_completa==palabrabuscar:
#                 acum+=1
#     print (f"Coincide {acum} veces")

# contarsubcadenas ("holararoholararohola", "hola")

#palabraescondida

def palabraescondida (cadena, palabraescondida):
    count=0
    for i in range (len(cadena)-len(palabraescondida)+1):
        acum=""
        for e in range (len(palabraescondida)):
            if cadena[i+e] == palabraescondida[e]:
                acum+=palabraescondida[e]
            if acum==palabraescondida:
                count+=1
    print (f"Aparece {count} veces")

palabraescondida("tupachamburguesatupachamburguesatuntupachamburguesa", "hamburguesa")
palabraescondida ("patataeofvuefopatataspdfivjhsdppatata", "patata")