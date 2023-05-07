from random import randint

options = [1, 2, 3]
choice_exit = ["pedra", "papel", "tesoura"]
rules = [
  [0, -1, 1],
  [1, 0, -1],
  [-1, 1, 0]
]

def machine_choice():
  return randint(1, 3)

def player_choice(option: str):
  player_choice_index = options.index(option)
  computer_choice_index = options.index(machine_choice())

  result = rules[player_choice_index][computer_choice_index]

  return [result,
          f"Você jogou {choice_exit[player_choice_index]}...",
          f"O inimigo jogou {choice_exit[computer_choice_index]}..."]
