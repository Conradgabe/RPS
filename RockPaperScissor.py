import random

choices = ['R', 'P', 'S']

computer = random.choice(choices)

print('**********************This is a game of Rock Paper and Scissors**************************')
print('\t\t\t********The rules are simple*********')
print('\t\t********You can Choose to Play Rock, Paper or Scissors*********\n')
print('\t*******Rule 1: If you choose to play Rock input "R" *********')
print('\t*******Rule 2: If you choose to play Paper input "P" *********')
print('\t*******Rule 3: If you choose to play Scissor input "S" *********\n')
print('Note:   To win ---------- Rock("R") beats Scissors("S")')
print('\tTo win ---------- Scissors("S") beats Paper("P")')
print('\tTo win ---------- Paper("P") beats Rock("R")')



########## Checking If the game wasa tie##########

while True:
    user_choice = input('What is you choice? ("R","P","S"): ')

    if user_choice == "R":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t**********It's a tie**********")
            print("\t**********Do you want to continue playing? **********")

            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break

    if user_choice == "S":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t**********It's a tie**********")
            print("\t**********Do you want to continue playing? **********")

            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break

    if user_choice == "P":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t**********It's a tie**********")
            print("\t**********Do you want to continue playing? ************")

            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break


#########Checking whether the game was won#########

    if user_choice == "R":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print('***************************You won!!!*****************************')

            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break

    if user_choice == "S":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print('***************************You won!!!*****************************')
            
            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break

    if user_choice == "P":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print('***************************You won!!!*****************************')
            
            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break

###########Checking to see if you lost###########

    if user_choice == "P":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print('**************************You Lost ): ****************************')

            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break

    if user_choice == "R":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print('**************************You Lost ): ****************************')

            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break
                

    if user_choice == "S":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print('**************************You Lost ): ****************************')
            
            chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)*******************')
                break
            else:
                print('********************Invalid Choice-----Choose Again**********************')
                chance = input("\t\t********Type 'Y' to continue and 'q' to quit***********:  ")
                if chance == 'Y':
                    continue
                elif chance == "q":
                    print('**********************GoodBye :)*******************')
                    break
