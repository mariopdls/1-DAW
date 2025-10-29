#Ej2
numganador= int(input("Dime el número ganador: "))
i=int(input("¿Cuántas apuestas quieres hacer?: "))
numapuesta=0
valor=0
banca=0
dinerojugador=int(input("¿Cuánto dinero tienes para apostar?"))


for i in range (1,i+1):
    numapuesta=int(input(f"Dime un numero para la apuesta. Es tu {i}º apuesta: "))
    while numapuesta<0 or numapuesta>=37:
        numapuesta=int(input(f"Dime un numero válido para la apuesta."))
    if numapuesta==numganador:
        tripleapuesta=numapuesta*3
        dinerojugador+=tripleapuesta
        print (f"El ganador triplica el valor de su apuesta. Su valor ahora es de {tripleapuesta}")

    elif numapuesta in range (numganador-10,numganador+11):
        tercioapuesta=dinerojugador/3
        dinerojugador+=tercioapuesta
        print (f"El ganador pierde un tercio del valor de su apuesta. Su valor ahora es de {tercioapuesta}")
    elif numapuesta in range (numganador-20,numganador+21):
        mitadapuesta=dinerojugador/2
        dinerojugador+=mitadapuesta
        print (f"El ganador pierde la mitad del valor de su apuesta. Su valor ahora es de {mitadapuesta}")
    else:
        banca+=dinerojugador
        dinerojugador=0
        print (f"El jugador pierde toda la apuesta")


print (f"Se han realizado {i} apuestas, y el importe total ganado por el jugador es de {dinerojugador}. La banca por su lado ha obtenido {banca}")