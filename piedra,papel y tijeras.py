 #piedra, papel y tijeras 
import random
opciones=("piedra", "papel", "tijeras")
usuario = input("introduce tu valor").lower()
maquina = random.choice(opciones) 

print("maquina selecciono",maquina)
if usuario not in opciones:
    print("intente nuevamente")


if maquina == usuario:
    print("empate")
elif (usuario== "tijeras" and maquina=="papel") or \
    (usuario=="piedra"and maquina=="tijeras") or \
    (usuario=="papel" and maquina=="piedra"):
    print("ganaste")
else:
    print("perdiste")
