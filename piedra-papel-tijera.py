nombre1 = input("Cual es tu nombre jugador1?: ")
nombre2 = input("Cual es tu nombre jugador2?: ")

jugador1 = input("Hola jugador1! Que eliges, piedra, papel o tijera?: ")
jugador2 = input("Hola jugador2! Que eliges, piedra, papel o tijera?: ")

condicion1 = (jugador1 == "piedra" and jugador2 == "tijera")
condicion2 = (jugador1 == "papel" and jugador2 == "piedra")
condicion3 = (jugador1 == "tijera" and jugador2 == "papel")

if jugador1 == jugador2:
    print("Hay un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado el jugador1!", nombre1)
else:
    print("Ha ganado el jugador2!", nombre2)