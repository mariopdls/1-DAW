
partidas_ganadas_jug1=0
partidas_ganadas_jug2=0

for i in range (1,6):
    jugador1= input('Jugador 1, pares o nones: ')
    jugador1num=int(input("Jugador 1, dime un número"))
    jugador2= input('Jugador 2, pares o nones: ')
    jugador2num=int(input("Jugador 2, dime un número"))
    if  (jugador1 != 'pares' and jugador1 != 'nones') or (jugador2 != 'pares' and jugador2 != 'nones'):
        print ("Tiene que ser un término válido, pares o nones para cada jugador.")
    elif (jugador1num<0 and jugador1num>10) or (jugador2num<0 and jugador2num>10):
        print ("números no válidos")
    elif jugador1=='pares' and  (jugador1num!=2 and jugador1num !=4 and jugador1num !=6 and jugador1num !=8 and jugador1num !=10):
        print ("Jugador 1, no es un número par")
    elif jugador1=='nones' and  (jugador1num!=1 and jugador1num !=3 and jugador1num !=5 and jugador1num !=7 and jugador1num !=9):
        print ("Jugador 1, no es un número impar")
    elif jugador2=='pares' and  (jugador2num!=2 and jugador2num !=4 and jugador2num !=6 and jugador2num !=8 and jugador2num !=10):
        print ("Jugador 2, no es un número par")
    elif jugador2=='nones' and  (jugador2num!=1 and jugador2num !=3 and jugador2num !=5 and jugador2num !=7 and jugador2num !=9):
        print ("Jugador 2, no es un número impar")
    else:
        if jugador1=='pares' and jugador2=='nones':
            if jugador1num+jugador2num%2==0:
                print ("Apuesta ganada por primer jugador")
                partidas_ganadas_jug1+=1
            else:
                print ("Apuesta ganada por segundo jugador")
                partidas_ganadas_jug2+=1
        elif jugador2=='pares' and jugador1=='nones':
            if jugador1num+jugador2num%2==0:
                print ("Apuesta ganada por segundo jugador")
                partidas_ganadas_jug2+=1
            else:
                print ("Apuesta ganada por primer jugador")
                partidas_ganadas_jug1+=1
        else: 
            print ('No pueden ser la misma apuesta')

if partidas_ganadas_jug1>partidas_ganadas_jug2:
    print (f"El jugador 1 ha ganado la partida. Vanció en {partidas_ganadas_jug1} ocasiones")
elif partidas_ganadas_jug2>partidas_ganadas_jug1:
        print (f"El jugador 2 ha ganado la partida. Vanció en {partidas_ganadas_jug2} ocasiones")
else:
    print ("Empate técnico")