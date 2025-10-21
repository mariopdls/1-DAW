d='D'
c='C'
v='V'
s='S'

estadocivil=str(input('Teclee su estado civil (S/C/D/V): '))

if estadocivil==s:
    print ('Es usted soltero')
elif estadocivil==c:
    print ('es usted casado')
elif estadocivil==v:
    print('es usted viudo')
elif estadocivil==d:
    print ('es usted divorciado')
else:
    print('no válido')

edad=int(input('Teclee su edad: '))
print ('tiene usted', edad ,'años')

if edad>50:
    print ('se aplica un 8%')
else:
    if edad<35:
        if s or d:
            print ('le corresponde un 12%')
        elif c or v:
            print('le corresponde un 11.3')
    else:
     print('le corresponde un 10.5%')