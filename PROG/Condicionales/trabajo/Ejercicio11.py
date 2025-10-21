#EJERICIO11  

amount=(int(input('Type the amount: ')))
discount=(str(input('You are student or regular?: ')))

# stu= (discount =='student') #STU ES UNA NUEVA VARIABLE QUE ES RESULTADO DE QUE EL DESCUENTO SEA COMPARADO CON EL STRING ESTUDIANTE. LO MISMO CON REG AL SER COMPARADO CON REGULAR
# reg= (discount=='regular')

# if stu:
#     if amount >= 100:
#         print("15% discount")
#     else:
#         print("10% discount")
# if reg:
#     if amount >= 200:
#         print("12% discount")
#     else:
#         print("5% discount")
# else:
#     print("Write 'student' or 'regular'.")

print(discount*amount/100)

