# filas=3 #numero de filas
# columnas=3 #numero de columnas
# matriz=[] #lista principal de la matriz, donde dentro van las columnas
# contador=1 #empieza en uno
# for i in range (filas): #recorre cada fila
#     fila=[] #fila dentro de las matrices
#     for j in range (columnas): #recorre cada columna
#         fila.append(contador)
#         contador+=1 #se añade un numero a la  fila e incrementa
#     matriz.append(fila) #añadir fila completa a la matriz

# for fila in matriz:
#     print (fila)

# filas=3
# columnas=3
# lista=[]
# for i in range (filas):
#     fila=[]
#     for e in range (columnas):
#         fila.append(0)
#     lista.append(fila)

# for fila in lista:
#     print (fila)


# #matriz con numeros consecutivos

# filas=3  #tamaño de las filas horizontales
# columnas=3 #tamaño de las columnas verticales
# lista=[] #lista principal
# acum=1 #acumulador
# for i in range (filas): #recorremos las filas horizontales
#     fila=[] #sire para guardarlo dentro de la lista principal
#     for e in range (columnas): #recorremos las columnas verticales. terminará antes que el horizontal
#         fila.append(acum) #el acumulador que empieza en 1 se guarda en fila
#         acum+=1 #se incrementa el acumulador en la siguiente iteracion
#     lista.append(fila) #la fila horizontal se guarda en la matriz (lista) y pasamos a la siguiente fila

# for fila in lista:  #bucle para imprimir la matriz
#     print (fila)


#suma de matrices

# matriz1= [
#     [2, 4, 5],
#     [3, 5, 6],
#     [2, 1, 5]
# ]

# matriz2= [
#     [2, 5, 6],
#     [3, 1, 3],
#     [2, 2, 2]
# ]

# resultado=[]
# for i in range (len(matriz1)):
#     fila=[]
#     for e in range (len(matriz1[0])):
#         suma=matriz1[i][e]+matriz2[i][e]
#         fila.append(suma)
#     resultado.append(fila)

# for fila in resultado:
#     print (fila)


# A = [
#     [1, 3, 5, 7],
#     [2, 4, 6, 8],
#     [9, 8, 7, 6]
# ]

# B = [
#     [5, 5, 5, 5],
#     [2, 2, 2, 2],
#     [1, 1, 1, 1]
# ]

# matriznueva=[]
# acum=0
# for i in range (len(A)):
#     for e in range (len(A[0])):
#         resultado= A[i][e] + B[i][e]
#         matriznueva.append(resultado)
# print (matriznueva)

# A = [
#     [1, 2],
#     [3, 4]
# ]

# B = [
#     [5, 6],
#     [7, 8]
# ]

# resultado=[]
# acum=0
# for i in range (len(A)):
#     filanueva=[]
#     for e in range (len(A[0])):
#         suma=A[i][e] + B [i][e]
#         filanueva.append(suma)
#     resultado.append(filanueva)

# for fila in resultado:
#     print (fila)


# A = [
#     [3, 1, 2],
#     [0, 5, 4],
#     [7, 8, 9]
# ]

# B = [
#     [1, 1, 1],
#     [1, 1, 1],
#     [2, 2, 2]
# ]

# resultado=[]

# for i in range (len(A)):
#     filanueva=[]
#     for e in range (len(A[0])):
#         suma= A[i][e] + B[i][e]
#         filanueva.append(suma)
#     resultado.append(filanueva)

# for fila in resultado:
#     print (fila)


# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [1, 1, 1]
# ]

# B = [
#     [9, 9, 9],
#     [3, 3, 3],
#     [2, 2, 2],
#     [5, 5, 5]
# ]

# resultado= []

# for i in range (len(A)): #Longitud de las filas
#     filanueva=[]
#     for e in range (len(A[0])): #longitud de las columnas
#         suma= A[i][e]+B[i][e]
#         filanueva.append(suma)
#     resultado.append(filanueva)

# for fila in resultado:
#     print (fila)


#sumar solo la segunda fila

# A = [
#     [1, 1, 1],
#     [2, 2, 2],
#     [3, 3, 3]
# ]

# B = [
#     [5, 5, 5],
#     [6, 6, 6],
#     [7, 7, 7]
# ]

# fila=[]
# for i in range (len(A[2])):
#     suma=A[2][i] + B[2][i]
#     fila.append(suma)
# print (fila)

# columna=[]
# for i in range(len(A)):
#     suma= A[i][2] + B[i][2]
#     columna.append(suma)
# print (columna)

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8]         # esta fila está mal
]

for i in range (len(A)):
    if len(A[i])== len(A[0]):
        print ("Es correcto")
    else:
        print ("Es incorrecto")