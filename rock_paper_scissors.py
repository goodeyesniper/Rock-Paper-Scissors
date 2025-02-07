import random

def lets_play():
    choices = ["rock", "paper", "scissors"]
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    while True:
        computer_hand = random.choice(choices)
        my_hand = input("rock, paper, or scissors? ").strip().lower()

        if my_hand not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        print(f"Computer chose: {computer_hand}")

        if my_hand == computer_hand:
            print("It's a draw!")
        elif win_conditions[my_hand] == computer_hand:
            print("You win!")
            break
        else:
            print("You lose! Try again.")

lets_play()