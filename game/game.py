import random

def choose_option():
    options = ["piedra", "papel", "tijera"]
    user = input("¿Piedra, papel o tijera?: ")
    user = user.lower()

    while not (user in options):
        print("Solo puedes escoger una de las opciones: ")
        user = input("¿Piedra, papel o tijera?: ")
        user = user.lower()

    computer = random.choice(options)

    print(f"♥ USUARIO: {user}")
    print(f"♥ COMPUTADOR: {computer}")
    return user, computer

def check_rules(user, computer, user_wins, computer_wins):
    
    if user == "tijera":

        if computer == "tijera":
            print("Tijera empata con tijera")
            print("► EMPATE")

        elif computer == "piedra":
            print("Tijera es aplastada por piedra")
            computer_wins += 1
            print("► PUNTO PARA LA COMPUTADORA")

        elif computer == "papel":
            print("Tijera corta papel")
            user_wins += 1
            print("► PUNTO PARA EL USUARIO")

    elif user == "piedra":
        if computer == "tijera":
            print("Piedra aplasta tijera")
            user_wins += 1
            print("► PUNTO PARA EL USUARIO")

        elif computer == "piedra":
            print("Piedra empata con piedra")

        elif computer == "papel":
            print("Piedra es cubierta por papel")
            computer_wins += 1
            print("► PUNTO PARA LA COMPUTADORA")

    elif  user == "papel":

        if computer == "tijera":
            print("Papel es cortado por tijera")
            computer_wins += 1
            print("► PUNTO PARA LA COMPUTADORA")

        elif computer == "piedra":
            print("Papel tapa a piedra")
            user_wins += 1
            print("► PUNTO PARA EL USUARIO")

        elif computer == "papel":
            print("Papel empata con papel")

    return user_wins, computer_wins

def run():
    user_wins = 0
    computer_wins = 0
    while user_wins != 3 and computer_wins != 3:
        user, computer = choose_option()
        user_wins, computer_wins = check_rules(user, computer, user_wins, computer_wins)

run()