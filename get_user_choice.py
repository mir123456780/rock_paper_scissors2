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

#Test: to find the user choice
user_input = input("Please select your choice using (R, P or S)")
user_choice = get_user_choice(user_input)
computer_choice = get_computer_choice()
print(f"The user selected {user_choice} and the computer selected {computer_choice}")
result = select_winner(user_choice,computer_choice)
print(f"The winner is: {result}")

