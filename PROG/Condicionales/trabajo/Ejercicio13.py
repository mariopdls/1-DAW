monedas1cent=int(input('Dime cuantas monedas tienes de 1 céntimo:'))
monedas2cent=int(input('Dime cuantas monedas tienes de 2 céntimos:'))
monedas5cent=int(input('Dime cuantas monedas tienes de 5 céntimos:'))
monedas10cent=int(input('Dime cuantas monedas tienes de 10 céntimos:'))
monedas20cent=int(input('Dime cuantas monedas tienes de 20 céntimos:'))
monedas50cent=int(input('Dime cuantas monedas tienes de 50 céntimos:'))
monedas1euro=int(input('Dime cuantas monedas tienes de 1 euro:'))
monedas2euro=int(input('Dime cuantas monedas tienes de 2 euros:'))

uncent=0.01
doscent=0.02
cincocent=0.05
diezcent=0.10
veintecent=0.20
cincuentacent=0.50
euro= 1     
doseuro=2                  #MULTIPLICAR RESULTADO DEL INPUT POR EL VALOR DE LA MONEDA


monedas1cent= (uncent*monedas1cent)
print('tienes', monedas1cent, 'monedas de 1 céntimo')

monedas2cent=(doscent*monedas2cent)
print('tienes', monedas2cent, 'monedas de 2 céntimos')

monedas5cent=(cincocent*monedas5cent)
print('tienes', monedas5cent, 'monedas de 5 céntimos')

monedas10cent=(diezcent*monedas10cent)
print('tienes', monedas10cent, 'monedas de 10 céntimos')

monedas20cent=(veintecent*monedas20cent)
print('tienes', monedas20cent, 'monedas de 20 céntimos')

monedas50cent=(cincuentacent*monedas50cent)
print ('Tienes', monedas50cent, 'monedas de 50 céntimos')

monedas1euro=(euro*monedas1euro)
print('tienes', monedas1euro, 'euro o euros')

monedas2euro= (monedas2euro*1)
print('tienes', monedas2euro, 'euros')

dinerototal= (monedas1cent+monedas2cent+monedas5cent+monedas10cent+monedas20cent+monedas50cent+monedas1euro+monedas2euro)
print ('En total tienes', dinerototal, 'euros')