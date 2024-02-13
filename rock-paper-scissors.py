import random, time

choice_player = 0

while choice_player != 4:
    welcome = """Welcome to the rock paper scissors game. Choose:
    1 - stone
    2 - paper
    3 - scissor
    4 - exit
    """

    print(welcome)

    choice_player = int(input("Your choise: "))

    choice_computer = random.choice((1, 2, 3))
    print(choice_computer)

    if choice_player == choice_computer:
        print("Tie!")
        time.sleep(5)
    elif (choice_player == 1 and choice_computer == 3) or (choice_player == 2 and choice_computer == 1) or (choice_player == 3 and choice_computer == 2):
        print("You're winner!")
        time.sleep(5)
    elif (choice_player == 1 and choice_computer == 2) or (choice_player == 2 and choice_computer == 3) or (choice_player == 3 and choice_computer == 1):
        print("You lost.")
        time.sleep(5)
    elif choice_player == 4:
        print("Game over!")
        time.sleep(5)
    else:
        print("Something wrong. Try one more time!")
        time.sleep(5)