#Condicionales if, elif else 
#Nos permiten evaluar expresiones boleanas que de cumplirse realizan una accion y en caso de no, realizan otra 

#Evaluar si una persona es mayor de edad 

genero = int(input('Ingresa tu genero 1)Mujer  2)Hombre'))
age = int(input('Ingresa tu edad:'))

if age <= 2:
    if genero == 1:
        print("You are a baby girl!!!")
    else:
        print("You are a baby boy!!!")
elif age < 12:
    if genero == 1:
        print("You are a girl!!!")
    else:
        print("You are a boy!!!")
elif age < 18:
    if genero == 1:
        print("You are a young girl!!!")
    else:
        print("You are a young boy!!!")
elif age < 50:
    if genero == 1:
        print("You are a woman!!!")
    else:
        print("You are a man!!!")
else:
    
    print("Eres muy mayor")
