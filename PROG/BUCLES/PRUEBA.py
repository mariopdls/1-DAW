# AL RECIBIR EL NUMERO HAGA LA TABLA DE MUTLPIPLCIAR DEL NUMERO QUE HA DADO

# numero= int(input('Dime un número: '))
# for i in range (0, 11):
#      print (numero, 'x', i, '=', i*numero)

# AL RECIBIR EL NUMERO HAGA LA TABLA DE MUTLPIPLCIAR pero de otra forma


# for i in range (0, 11):
#      print (numero, 'x', i, '=', acumulador)
#      acumulador+=numero #+= lo que hace es incrementar el valor del acumulador

# HACER TABLA DE MULTIPLICAR SOLO USANDO UNA VEZ LA MULTIPLICACION Y OTRA OPERACION (SUMA, RESTA...)

num1=int(input('Introduzca un numero'))
for i in range(1,num1*11):
    if i%num1==0:
        print(i,'x', i//num1,'=',num1)

        f"{} x {} = {}"