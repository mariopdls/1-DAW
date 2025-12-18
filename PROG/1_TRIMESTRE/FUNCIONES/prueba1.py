#Lectura de los apuntes disponibles y desarrollo de dos funciones diferentes a las proporcionadas con varios tests asociados a cada una de ellas.
# parametro1= int(input("Dime un parámetro: "))
# def modulo (parametro1):
#     resultado_modulo=parametro1%2
#     return resultado_modulo

# # print (modulo(parametro1%2))

# # assert (modulo(6)==0)
# # assert (modulo(7)==1)

# parametro1= int(input("Dime un parámetro: "))
# def division (parametro1):
#     resultado_div=parametro1//2
#     return resultado_div
# print (division(parametro1))

# assert (division(5)==2) #está bien
# assert (division(5)==1) #está mal

# matriz = [
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
# ]

# matriz2 = [
#  [9,8,7],
#  [6,5,4],
#  [3,2,1]
# ]

# def suma_matrices (m1,m2):
#     listanueva=[]
#     for i in range (len(matriz)):
#         for e in range (len(matriz[0])):
#             resultado= matriz[i][e]+matriz2[i][e]
#             listanueva.append(resultado)
#     print (listanueva)
# suma_matrices (matriz,matriz2)

# matriz1=     [
#  [2,4,6],
#  [1,3,5],
#  [7,8,9]
# ]

# def sumar_columnas (matriz):
#     acum=0
#     lista=[]
#     for i in range (len(matriz)):
#         for e in range (len(matriz[0])):
#             acum+=matriz[e][i]
#         lista.append (acum)
#         acum=0
    

# # sumar_columnas (matriz1)

# def suma_filas (matriz):
#     listanue=[]
#     acum=0
#     for i in range (len(matriz)):
#         for e in range(len(matriz[0])):
#             acum+=matriz[i][e]
#         listanue.append(acum)
#         acum=0
#     print(listanue)

# suma_filas (matriz1)

def contar_subcadena(frase, palabra):
    coincide=0
    for i in range (len(frase)-(len(palabra))):
contar_subcadena ("dspfchicharosvhjuiesdpuih0chicharosoerlvfjchicharos","chicharos")