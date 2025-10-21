base= int(input('Dime la base:'))
exponente= (int(input('Dime el exponente')))
potencia=base**exponente

if exponente==0:
    print ('resultado es 1')

elif exponente<0:
    print((1/base)**(exponente*-1))
elif exponente>=0:
    print('el resultado es %s' %(potencia))

