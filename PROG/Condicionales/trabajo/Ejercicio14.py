day=int(input('dia'))
year=int(input('año'))
month=int(input('mes'))

leap= year%4==0 and year%100!=0 or year%400==0 

if leap:
    print('this is a leap year')
    if month==2 and day>1 and day<=29: # es igual que poner if month==2 and 1<=day<=29
        print('the date is valid')
    elif month==2:
        print('the date is invalid')
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and day>=1 and day<=30:
    print ('The date is valid')
elif (month==4 or month==6 or month==9 or month==11) and day>=1 and day<=31: #aqui se cumple que el mes sea 4, 6, 9 o 11 Y el día sea mayor que 1 y mayor que 31, se tiene que cumplir todo para que el mes sea de 31
    print('The date is valid')
else:
    print('Invalid date')