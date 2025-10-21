caracter1=input('Dime un carácter: ')
num1=int(input('Dime un número'))
num2=int(input('Dime otro número'))

if caracter1=='/':
    if num2==0:
        print('No se puede dividir entre cero')
    else:
        print (num1/num2)
elif caracter1=='*':
    print (num1*2 or num2*1)
elif caracter1=='+':
    print (num1+num2 or num2+num1)
elif caracter1=='-':
    print (num1-num2 or num2-num1 )
else:
    print (num1, caracter1, num2)