numero_alumnos= int(input('Dime el número de alumnos'))

costo1=65
costo2=70
costo3=95
costo4=2500

pagobus1= numero_alumnos*costo1
pagobus2= numero_alumnos*costo2
pagobus3= numero_alumnos*costo3
pagobus4= numero_alumnos*costo4

if numero_alumnos >=100:
    print ('el costo es del bus es', pagobus1)

elif numero_alumnos >=50 or numero_alumnos<=99:
    print ('el costo es del bus es', pagobus2)

elif numero_alumnos >=30 or numero_alumnos<=49:
    print ('el costo es del bus es', pagobus3)

elif numero_alumnos <30:
    print ('el costo es del bus es', pagobus4)

costoautobus1=pagobus1/numero_alumnos
costoautobus2=pagobus2/numero_alumnos
costoautobus3=pagobus3/numero_alumnos
costoautobus4=pagobus4/numero_alumnos

if numero_alumnos >=100:
    print ('el costo es de', costoautobus1, 'por alumno')

elif numero_alumnos >=50 or numero_alumnos<=99:
    print ('el costo es de', costoautobus2, 'por alumno')

elif numero_alumnos >=30 or numero_alumnos<=49:
    print ('el costo es de', costoautobus3, 'por alumno')

elif numero_alumnos <30:
    print ('EL costo es de', costoautobus4, 'por alumno')

