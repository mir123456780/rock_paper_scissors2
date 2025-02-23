from rock_paper_scissors_game.module_all_games import get_score, play_again, write_file


#These are the rock, paper, scissor functions

def get_user_choice(value_user):
    """
    This function will return the user's action choice (rock, paper or scissors) made my the user.
    :return: str
    """

    if value_user.upper() == 'R': #this will convert lowercase to uppercase.
        return "Rock"

    elif value_user.upper() == 'P':
            return "Paper"

    elif value_user.upper() == 'S':
            return "Scissors"

    else:
        return get_user_choice(value_user)



import random
def get_computer_choice():
    """
    This function will generate a random number and convert it into a defined string value
    :return: str
    """
    random_number = random.randint(0, 2)
    if random_number == 0:
        return 'Rock'
    elif random_number == 1:
        return 'Paper'
    else:
        return 'Scissors'


winning_cases = {"Rock":"Scissors", "Paper":"Rock", "Scissors":"Paper"}

def select_winner(user_choice, computer_choice):
    """
    This function gets the choice of the user and the computer and decides who is the winner
    :param: string
    :return: str
    """
    if user_choice==computer_choice:
        return "draw"
    elif winning_cases[user_choice]==computer_choice:
        return "user"
    else:
        return "computer"


def main():
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

if __name__ == "__main__":
    main()

