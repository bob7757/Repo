import random
def outcome(player_move_number, player_choice_str):
    computer_choice = random.randint(0,2)
    if computer_choice - player_move_number == 0:
        print(f"You tied! Your opponent also chose {player_choice_str}!")
    elif computer_choice - player_move_number == 1 or computer_choice - player_move_number == -2:
        print(f"You lose, you chose {player_choice_str} and your opponent chose {rpy[computer_choice]}!")
    else:
        print(f"You win! You chose {player_choice_str} and your opponent chose {rpy[computer_choice]}!")


rpy = ["rock", "paper", "scissors"]
quit = False
while not quit:
    player_choice_str = input("Choose rock, paper, or scissors!").lower()
    if player_choice_str == "quit":
        quit = True
    elif player_choice_str == "rock":
        player_move_number = 0
        outcome(player_move_number, player_choice_str)
    elif player_choice_str == "paper":
        player_move_number = 1
        outcome(player_move_number, player_choice_str)
    elif player_choice_str == "scissors":
        player_move_number = 2
        outcome(player_move_number, player_choice_str)
    else:
        print("Please enter rock, paper, or scissors. To quit, enter quit. \n")