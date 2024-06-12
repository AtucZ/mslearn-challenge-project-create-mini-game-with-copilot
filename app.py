# Un juego de piedra papel o tijera que permita ingresar entre esas opciones en consola
# Tras cada partida el juego pregunte si desea seguir jugando o culminar el juego
# Cuando el juego termine muestre la puntuación del jugador con el número de victorias y rondas
# El juego debe ejecutarse en la consola de python

import random

def jugar():
    
    opciones = ['piedra', 'papel', 'tijera']
    rounds = 0
    wins = 0
    
    while True:
        opcion = input('Ingresa tu opción: ')
        opcion = opcion.lower()
        
        if opcion not in opciones:
            print('Opción no válida')
            continue

        rounds += 1
        pc = random.choice(opciones)
        print(f'PC: {pc}')
        
        if opcion == pc:
            print('Empate')
        elif opcion == 'piedra' and pc == 'tijera':
            print('Ganaste')
            wins += 1
        elif opcion == 'tijera' and pc == 'papel':
            print('Ganaste')
            wins += 1
        elif opcion == 'papel' and pc == 'piedra':
            print('Ganaste')
            wins += 1
        else:
            print('Perdiste')

        print(f'Rounds: {rounds}, Wins: {wins}')

        seguir = input('Deseas seguir jugando? (s/n): ')

        if seguir.lower() == 'n':
            break

    print(f'Fin del juego. Rounds: {rounds}, Wins: {wins}')


# Iniciar juego
jugar()