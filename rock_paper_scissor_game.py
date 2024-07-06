import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = ""
    while user_choice not in choices:
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

def play_again():
    while True:
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again in ["y", "n"]:
            return again == "y"
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        print(f"\nRound {rounds}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nScores:\nYou: {user_score}\nComputer: {computer_score}")

        if not play_again():
            break

    print("\nThank you for playing! Final scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

if __name__ == "__main__":
    main()
