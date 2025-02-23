# from rock_paper_scissors import get_user_choice, get_computer_choice, select_winner

def get_score(winner, score):
    user_score = score[0]
    computer_score = score[1]

    if winner == 'user':
        user_score += 1
        return [user_score, computer_score]
    elif winner == 'computer':
        computer_score += 1
        return [user_score, computer_score]
    else:
        return [user_score, computer_score]


def play_again(again):
    if again == 'yes':
        return True
    else:
        return False


def write_file(score_list):
    with open('scoreboard.txt', 'a') as scoreboard:
        scoreboard.write(f"{score_list}\n")
