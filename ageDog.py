#lee la edad de alguien 
age = int(input("Ingresa tu edad:"))
#resta dos a esa edad y se llamara last_years
last_years = age - 2
#first_year sera igual a los 2 por 10.5
first_year = 2*10.5
#multiplica los años restantes por 4 y suma los first_years
agDog = 4*last_years + first_year

print(f"Tienes {age} año que equivalen a {agDog}")
