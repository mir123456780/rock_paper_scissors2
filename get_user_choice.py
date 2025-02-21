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

