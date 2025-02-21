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

#Test: to find the user choice
#a = input("Please select your choice using (R, P or S)")
#b = get_user_choice(a)
#print(b)

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

#a = get_computer_choice()
#print(a)

