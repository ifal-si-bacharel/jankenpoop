from random import randint
player_lifes = 3
enemy_lifes = 3
current_round = 0
options = [1, 2, 3]
exit = ["pedra", "papel", "tesoura"]
rules = [
  [0, -1, 1],
  [1, 0, -1],
  [-1, 1, 0]
]

def machine_choice():
    return randint(1, 3)

def player_choice(option: str):
    global current_round,player_lifes,enemy_lifes
    if current_round == 0:
      player_lifes = 3
      enemy_lifes = 3
    current_round += 1
    
    player_choice_index = options.index(option)
    computer_choice_index = options.index(machine_choice())
    result = rules[player_choice_index][computer_choice_index]
    if result == 1:
        enemy_lifes -=1
    elif result == -1:
        player_lifes -= 1
    
    if enemy_lifes == 0 or player_lifes == 0:
        current_round = 0
    
    print(f"{current_round}|jogador: {player_lifes} X Inimigo: {enemy_lifes}")
    return [result,f"Você jogou {exit[player_choice_index]}...",f"O inimigo jogou {exit[computer_choice_index]}...",player_lifes,enemy_lifes,current_round]