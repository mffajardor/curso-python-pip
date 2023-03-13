# Juego de piedra, papel o tijera
import random

# Función para selección de opciones
def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input("piedra, papel o tijera => ")
  user_option = user_option.lower()   # Pasar a minuscula
  computer_option = random.choice(options)
  
  # Verificar que la opcion del usuario sea valida => None si no la tiene
  if not user_option in options:
    print('Esa opción no es válida!!')
    return None

  print('User option =>', user_option)
  print('Computer option =>',computer_option)
  return user_option, computer_option

# Función para verificación de reglas
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Empate !!")
  
  elif user_option == 'piedra':
    # Opcion 1 - Si gana
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('User ganó !!')
      user_wins += 1
    # Opcion 2 - Si pierde
    else:
      print('papel gana a piedra')
      print('Computer ganó !!')
      computer_wins += 1
  
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('User ganó !!')
      user_wins += 1
      
    else:
      print('tijera gana a papel')
      print('Computer ganó !!')
      computer_wins += 1
      
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('User ganó !!')
      user_wins += 1
      
    else:
      print('piedra gana a tijera')
      print('Computer ganó !!')
      computer_wins += 1
  # Retorno de la puntuación que lleva el user y computer en el momento 
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    print('=' * 20)
    # Colocar break para cuando tenga la mayor cantidad de victorias
    if computer_wins == 2:
      print('El ganador es Computer ====> Felicidades !!!')
      
    if user_wins == 2:
      print('El ganador es User ====> Felicidades !!!')
    print('=' * 20)

# Función maestra del juego
def run_game():
  # Contador para victorias computer y user
  computer_wins = 0
  user_wins = 0
  rounds = 1
 
  while True: # Se repite hasta que alguno de los 2 gane
  
    print('=' * 14)
    print(f'ROUND {rounds}, los puntos que llevan son:')
    print(f' ===> Computer lleva {computer_wins}')
    print(f' ===> User lleva {user_wins}')
    print('=' * 14)
  
    # Guardar Opciones del user y computer => Desde la función
    user_option, computer_option = choose_options()

    # Guardar wins del user y computer => Desde la función
    #Necesario colocarlas nuevamente por estar como argumentos de la función y por estar en el ciclo
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    # Verificar si se llega a las victorias
    if user_wins >= 2 or computer_wins >=2:
      check_winner(user_wins, computer_wins)
      break

    rounds += 1

# Arrancar juego    
run_game()