#Scrip que juega priedra papael o tijera 
import random 

#Leer elecciondel usuario 
user = input("Elige: Piedra, Papel o Tijera \n")

#Generar eleccion de la maquina
aleatorio = random.randint(1, 3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine ="papel"
else:
    aleatorio = "tijera"

#Comparara para determinar quien gana
print(f"El usuario eligio {user} y la maquina eligio {machine}")

if user=="piedra" and machine=="piedra":
    print("Es un empate")
elif user=="piedra" and machine=="papel":
    print("Gana la maquina")
elif user=="piedra" and machine=="tijera":
    print("Gana el usuario")
elif user=="papel" and machine=="piedra":
    print("Gana el usuario")
elif user=="papel" and machine=="papel":
    print("Es un empate")
elif user=="papel" and machine=="tijera":
    print("Gana la maquina")
elif user=="tijera" and machine=="piedra":
    print("Gana la maquina")
elif user=="tijera" and machine=="papel":
    print("Gana el usuario")
else:
    print("Es un empate")