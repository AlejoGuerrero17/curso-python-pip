def choose_options():
  import random
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Elija , piedra papel o tijera -> ').lower()
  if user_option not in options:
    print('Esa opción no es valida')
    return None, '0'
    #continue
  computer_option = random.choice(options)
  print('User_option --> ', user_option)
  print('Computer option --> ', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, users_wins, computer_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user ganó!')
      users_wins += 1
    else:
      print('papel gana a piedra')
      print('computer ganó!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user ganó!')
      users_wins += 1
    else:
      print('tijera gana a papel')
      print('computer ganó')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user ganó')
      users_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer ganó!')
      computer_wins += 1
  return users_wins, computer_wins


def check_winner(users_wins, computer_wins):
  if computer_wins == 2:
    print('El ganador es la computadora')
    return True
  if users_wins == 2:
    print('El ganador es el usuario')
    return True


def run_game():
  rounds = 1
  computer_wins = 0
  users_wins = 0
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('computer_wins', computer_wins)
    print('users_wins', users_wins)
    rounds += 1
    user_option, computer_option = choose_options()
    users_wins, computer_wins = check_rules(user_option, computer_option,
                                            users_wins, computer_wins)
    if check_winner(users_wins, computer_wins):
      break


run_game()
