#Ejercicio4

edad=int(input("Teclee la edad: "))

if edad>50:
    print("Edad superior a la permitida")
elif edad>16:
    print("Le corresponde: Enseñanza post-obligatoria.")
elif 16>=edad>=12:
    print("Le corresponde: Educación segundaria obligatoria.")
elif 11>=edad>=7:
    print("Le corresponde: Educación primaria.")
elif 7>=edad>=0:
    print("Le corresponde: Educación infantil.")
else:
    print("Edad menor a la soportada")
