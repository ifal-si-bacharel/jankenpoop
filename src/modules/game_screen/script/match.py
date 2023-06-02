from random import randint
options = [1, 2, 3]
exit = ["play-rock.png", "play-paper.png", "play-siccsors.png"]

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
    
    if result == 1:
        result = "Você ganhou!"
    elif result == -1:
        result = "Você perdeu!"
    else:
        result = "Empate!"
        
    player_text = exit[player_choice_index]
    machine_text = exit[computer_choice_index]
    
    return [result,[player_text,machine_text]]

