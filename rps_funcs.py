import random

# check the game logic
def main(user_choice, computer_choice):
    if user_choice == "R" and computer_choice == "R" or user_choice == "S" and computer_choice == "S" or user_choice == "P" and computer_choice == "P":
        result = "\nIt's a tie"

    elif user_choice == "S" and computer_choice =="P" or user_choice == "R" and computer_choice == "S" or user_choice == "P" and computer_choice == "R":
        result = "\nUser win's - Computer lose's"
    
    else:
        result = "\nComputer win's - User lose's"

    return f"{result} - computer: {computer_choice} vs user: {user_choice}"


# get the computer choice
def computer_choices():
    choices_options = ["R", "P", "S"]
    computer_choice = random.choice(choices_options)

    return computer_choice 


# get the user choice
def user_choices():
    user = input("What is you choice: 'R', 'P' or 'S': ")
    user_choice = user.upper()

    # check user choices
    if user_choice != "R" and user_choice != "P" and user_choice != "S":
        n_result = "...Please input 'R', 'P' or 'S'..."
        print(n_result)
        user_choices()

    return user_choice


# game loop play
def play():
    chance = input("\nWanna play again ('enter 'y' to play or 'q' to quit'): ")
    user_chance = chance.upper()#

    # check user choice chance
    if user_chance == "Y":
        u_choice = user_choices()
        c_choice = computer_choices()
        winner = main(u_choice, c_choice)
        return winner

    elif user_chance == "Q":
        quit_n = "\n***********Goodbye**********\n"
        return quit_n
    
    n_error = "Please input 'Y' to continue or 'Q' to quit"
    return n_error
    
# loop the game

c_choice = computer_choices()
u_choice = user_choices()

winner = main(u_choice, c_choice)
print(winner)

f_result = play()
print(f_result)

while True:
    o_error = play()
    print(o_error)
    if o_error == "\n***********Goodbye**********\n":
        break
    continue