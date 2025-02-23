#This will play the game externally.

from rock_paper_scissors_game.rock_paper_scissors import get_computer_choice, get_user_choice, get_score, select_winner, play_again, write_file

score = [0, 0]
count = 0
while True:
    count += 1
    user_input = input("Please select your choice using (R, P or S)")
    choice_user = get_user_choice(user_input)
    choice_computer = get_computer_choice()
    print(f"The user selected {choice_user} and the computer selected {choice_computer}")
    result = select_winner(choice_user, choice_computer)
    print(f"The winner is: {result}")
    score = get_score(result, score)
    print(f"The user score {score[0]} and the computer score {score[1]}")
    again = input("Would you like to play again (yes/no)")
    if not play_again(again):
        write_file(f"You have played {count} games. The user score {score[0]} and the computer score {score[1]}")
        exit()