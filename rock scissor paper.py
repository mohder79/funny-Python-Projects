import random

valid_opponent_choices = ['user', 'computer']


while True:
    opponent = input('your opponent is user or computer ?')
    if opponent in valid_opponent_choices:
        print("You chose:", opponent)
        break
    else:
        print('Invalid choice , please try again.')


valid_choices = ['rock', 'scissor', 'paper']


while True:
    if opponent == 'user':
        player_1 = input(
            "player one What is your choice  (rock,scissor,paper): ? ")
        player_2 = input(
            "player two What is your choice  (rock,scissor,paper): ? ")
        if player_1 and player_2 in valid_choices:
            print(
                f"player one you choice {player_1} and player two you choice {player_2}")
            break
        else:
            print('Invalid choice , please try again.')
    if opponent == 'computer':
        player_1 = input("What is your choice  (rock,scissor,paper): ?")
        player_2 = random.choice(valid_choices)
        if player_1 in valid_choices:
            print(
                f"player one you choice {player_1} and player two you choice {player_2}")
            break
        else:
            print('Invalid choice , please try again.')


def winner(player1, player2):
    if (player1 == 'rock' and player2 == 'scissor') or (player1 == 'scissor' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        return True


if player_1 == player_2:
    print(f"Its a Tie! we dont have any winer 🤨 ")
elif winner(player_1, player_2):
    print('player one you won 🥳 ')
else:
    print('player two you won 🥳 ')
