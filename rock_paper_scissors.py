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
    print("\n   Welcome to rock, paper, scissors game! \n   First to reach 10 wins. Good Luck! ")
    print("\n          (type 'quit' to exit)          ")
    print("\n=========================================")
    time.sleep(3)

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
            print("\n             You win!\n")
            print("=======================================")
            if my_score == 10:
                print("Final Score:")
                print(f"Computer Score: {computer_score}")
                print(f"Your Score: {my_score}")
                print("#######################################")
                print("\n      Congratulations you won!\n")
                print("#######################################")
                time.sleep(2)

                play_again()
                    

        else:
            computer_score = computer_score + 1
            print("=======================================")
            print("\n         You Lose! Try again.\n")
            print("=======================================")
            if computer_score == 10:
                print("Final Score:")
                print(f"Computer Score: {computer_score}")
                print(f"Your Score: {my_score}")
                print("#######################################")
                print("\n Computer Won! Try again next time.\n")
                print("#######################################")
                time.sleep(2)

                play_again()

                
        
        print(f"Computer score: {computer_score}")
        print(f"My score: {my_score}")


def play_again():
    while True:
        response = input("\nPlay again? (yes or no): ").strip().lower()
        if response == "yes":
            lets_play()
            break
        elif response == "no":
            print("\nThanks for playing! Goodbye.\n")
            exit()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


lets_play()