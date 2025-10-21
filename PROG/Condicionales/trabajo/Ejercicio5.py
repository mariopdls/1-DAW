#Ejercicio5

valor=2
valor=valor+2
valor+=2

#saludo='hola'
#saludo=saludo + ' qué tal?' #quedaría como 'hola + que tal'
#saludo= ' que haces'  #quedaría como 'hola + que tal que haces'

num1=int(input('Dime un número: '))
num2=int(input('Dime otro número: '))
num3=int(input('Dime otro número: '))
num4=int(input('Dime otro número: '))

media=(num1+num2+num3+num4)/4
print ('la media de los números es ', media)

cantidad_superiores=0
valores_superiores= ''

if num1>media:
    cantidad_superiores +=1
    valores_superiores+= '' + str(num1)

if num2>media:
    cantidad_superiores +=1
    valores_superiores+= '' + str(num2)
   
if num3>media:
    cantidad_superiores +=1 #cuenta los números
    valores_superiores+= '' + str(num3) #almace na numero

if num4>media:
    cantidad_superiores +=1
    valores_superiores+= '' + str(num4)


print ('la media es de: ', media, 'y hay', cantidad_superiores, 'numeros superiores a la media')

#VER EN CASA PASO A PASO