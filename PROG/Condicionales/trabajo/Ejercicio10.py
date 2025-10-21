hora=int(input('Dime la hora de un reloj:'))
minutos=int(input('Dime los minutos de un reloj:'))
segundos=int(input('Dime los segundos de un reloj: '))

hora2=int(input('Dime las horas de un segundo reloj: '))
minutos2=int(input('Dime las horas de un segundo reloj: '))
segundos2=int(input('Dime los segundos de segundo un reloj: '))

horatotal1=hora, minutos, segundos,
horatotal2= hora2, minutos2, segundos2

if hora<0 or hora>23:
    print ('Hora inválida')
elif minutos <0 or minutos>60:
    print ('Hora inválida')
elif segundos <0 or segundos>60:
    print ('Hora inválida')
if hora2<0 or hora2>23:
    print ('Hora inválida')
elif minutos2 <0 or minutos2>60:
    print ('Hora inválida')
elif segundos2 <0 or segundos2>60:
    print ('Hora inválida')

else:   #EN CASO DE QUE NO SEA INVALIDA:
    if hora>hora2:
        print(horatotal1, 'es mayor')
    elif hora2>hora:                    #ELIF PORQUE O SE CUMPLE IF O ELSEIF
        print (horatotal2, 'es mayor')
    else:
        if hora==hora2: #SI HORA ES IGUAL A HORA2 PUES RECURRIMOS A LOS MINUTOS
            if minutos>minutos2:
                print (horatotal1, 'es mayor')
            elif minutos2>minutos:
                print (horatotal2, 'es mayor')
            else:
                if minutos==minutos2: #SI LOS MINUTOS SON IGUALES, VAMONOS A LOS SEGUNDOS
                    if segundos>segundos2:
                        print (horatotal1, 'es mayor')
                    elif segundos2>segundos:
                        print (horatotal2, 'es mayor')
                    else:
                        print(horatotal1, "es igual que", horatotal2) #SI TODAS LAS CONDICIONES SON IGUALES, PUES ES PORQUE LAS HORAS SON IGUALES.
                        
