# from rock_paper_scissors import get_user_choice, get_computer_choice, select_winner
#This gets the winner from another function. It receives and modifies a list.
def get_score(winner, score):
    """
    This function will return the winner and the score of the games
    :param winner: str
    :param score: str
    :return: str
    """
    user_score = score[0]
    computer_score = score[1]

#This is an if statement, adding a point to the winner of the game and returning the score
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1
    return [user_score, computer_score]

#This function will determine if they would like to play again.
def play_again(again):
    """
    This function will prompt the user to decide to play again or not and call the game again if the user chooses yes. Otherwise, it will end the game.
    :param again: str
    :return: boolean
    """
    if again == 'yes':
        return True
    else:
        return False

#This function will create a new file with the scores from the games.
def write_file(score_list):
    """This file will create a file and append the scores to it.
    :param score_list: str
    :return: str
    """
    with open('scoreboard.txt', 'a') as scoreboard:
        scoreboard.write(f"{score_list}\n")
