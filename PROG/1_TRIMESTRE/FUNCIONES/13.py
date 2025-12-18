13
funcion que tenga como parametro tres cadenas.
la primera, una frase que debe comprobar si existe el segundo parámetro
la segunda, una palabra
la tercera, el reemplazo para la segunda palabra

ejemplo: cadena= hola buenas tardes palabra= tardes reemplazo= mañanas


def hacer_reemplazo(cadena, palabra, reemplazo):
    acum=""
    espacio=""
    cadena=cadena.split()
    if cadena[0]==palabra:
        cadena[0]=reemplazo
    elif cadena[1]==palabra:
        cadena[1]=reemplazo
    elif cadena[2]==palabra:
        cadena[2]=reemplazo
    else: print ("No hay nada que reemplazar")

    if cadena[0]==reemplazo or cadena[1]==reemplazo or cadena[2]==reemplazo:
        for i in range (len(cadena)):
            acum+=cadena[i] + " "
            i+=1
        print (acum)
        return acum

hacer_reemplazo("Hola buenas tardes", "tardes", "mañanas")