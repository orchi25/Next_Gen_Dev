import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScores: You - {user_score}, Computer - {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    play_game()
