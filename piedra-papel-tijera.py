import random

print(" Bienvenido al juego de  Piedra, Papel o Tijera")
print("Opciones: piedra, papel, tijera")

opciones = ["piedra", "papel", "tijera"]

# Elección del jugador
jugador = input("Elige una opción: ").lower()

# Elección de la computadora
computadora = random.choice(opciones)

print(f"La computadora eligió: {computadora}")

# Determinar ganador
if jugador == computadora:
    print("🤝 ¡Empate!")
elif (
    (jugador == "piedra" and computadora == "tijera") or
    (jugador == "papel" and computadora == "piedra") or
    (jugador == "tijera" and computadora == "papel")
):
    print("🎉 ¡Ganaste!")
elif jugador in opciones:
    print(" ¡La computadora gana!")
else:
    print(" Opción inválida")
