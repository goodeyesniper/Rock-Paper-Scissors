import random
import time

def lets_play():
    choices = ["rock", "paper", "scissors"]
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    computer_score = 0
    my_score = 0

    print("\n\n=========================================")
    print("\n  Welcome to rock, paper, scissors game!")
    print("\n  First to reach 10 wins. Good Luck!")
    print("\n=========================================")
    time.sleep(5)

    while True:
        
        computer_hand = random.choice(choices)
        print(f"Computer chose: {computer_hand}")
        my_hand = input("rock, paper, or scissors? ").strip().lower()
        
        if my_hand == "quit":
            break
        elif my_hand not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        if my_hand == computer_hand:
            print("=======================================")
            print("\n           It's a draw!\n")
            print("=======================================")
            
        elif win_conditions[my_hand] == computer_hand:
            my_score = my_score + 1
            print("=======================================")
            print("\n             YOU WIN!\n")
            print("=======================================")
            if my_score == 10:
                print("#######################################")
                print("\n      CONGRATULATIONS YOU WON!\n")
                print("#######################################")
                break
        else:
            computer_score = computer_score + 1
            print("=======================================")
            print("\n         YOU LOSE! Try again.\n")
            print("=======================================")
            if computer_score == 10:
                print("#######################################")
                print("\n COMPUTER WON! TRY AGAIN NEXT TIME.\n")
                print("#######################################")
                break
        
        print(f"Computer score: {computer_score}")
        print(f"My score: {my_score}")


lets_play()