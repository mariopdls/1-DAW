
# #4


# def rotar_cadena (cadena, n):
#     return cadena[n:] + cadena[:n]           #ponemos el inicio en [n: ] y el final en [ :n], pues es [inicio:fin]

# # print (rotar_cadena ("Python", 4))


def dni_num (dni):
    letras= "TRWAEMYFPDXBIJZSQVHLCK"
    dni="00000000H"
    resto=int(dni[:-1]%23)
    letras[resto] == dni [-1]
    len(dni) ==8
    return letras  [int(dni[:-1])%23] == dni[-1]