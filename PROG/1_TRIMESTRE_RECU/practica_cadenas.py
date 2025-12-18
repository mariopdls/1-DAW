# #ej 2

# def camelcase (cadena):
#     acum=""
#     lista=[]
#     acum3=""
#     for i in range (len(cadena)):
#         if cadena[i] != " ":
#             acum+=cadena[i]

#         else:
#             lista.append(acum)
#             acum=""
#     lista.append (acum)

#     for e in range (len(lista)):
#         for j in range (len(lista[e])):
#             if lista[e][j]==lista[0][0]:
#                 acum3+=lista[e][j]
#             elif lista[e][j]==lista[e][0]:
#                 acum3+=lista[e][j].upper()
#             else:
#                 acum3+=lista[e][j]

# camelcase ("hola mundo cruel")

#ej3

def sumanumeros (cadena):
    numeros="1234567890"
    acum="0"
    lista=[]
    for i in range (len(cadena)):
        
        if cadena[i].isdigit():
            acum+=cadena[i]

        elif cadena[i].isalpha():
            if acum!="0":
                lista.append(int(acum))
                acum="0"
    lista.append(int(acum))

    print (sum(lista))

sumanumeros("abc12x3y45")