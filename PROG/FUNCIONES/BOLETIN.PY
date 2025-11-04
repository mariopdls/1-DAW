
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

# #3

# numeros="1234567890"
# cadena= "ew32q133asa"

# numerosfuera=""

# for i in cadena:
#     if i in numeros:
#         numerosfuera+=i

# int (numerosfuera)
    
#4


# def rotar_cadena (cadena, n):
#     return cadena[n:] + cadena[:n]           #ponemos el inicio en [n: ] y el final en [ :n], pues es [inicio:fin]

# print (rotar_cadena ("Python", 4))
# print (rotar_cadena ("Hola buenas tardes",-5))

#TAREACLASE DNI

# def dni_num (dni): #define numero de dni
#     letras= "TRWAEMYFPDXBIJZSQVHLCK" #todas las letras posibles de dni
#     dni="00000000H" #string, cadena de texto
#     resto=int(dni[:-1]%23) #calculo de resto, que yo lo hice con la formula de dividendo(cociente*divisor) pero sevillano usó mod23
#     letras[resto] == dni [-1] #cualquiera de las letras que está, junto con el resultado del restro, es igual que el dni menos la letra
#     len(dni)==8
#     return letras  [int(dni[:-1])%23] == dni[-1]


# #5

# def charactersInString(cadena, caracter):
#     cuenta = 0
#     for i in cadena:          # usa otro nombre
#         if i == caracter:     # compara
#             cuenta += 1
#     return cuenta
# print (charactersInString ("buenosdias","a"))
