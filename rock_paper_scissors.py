from random import randint

choice = ["rock", "paper", "scissors"]

def main():
    computer = choice[randint(0, 2)]

    print("Welcome to the Rock, Paper, Scissors Game!\n")

    while True:
        # Convert the user input to lowercase to ensure case-insensitive comparison
        player = input("Your Choice (rock, paper, scissors): ").lower()

        if player not in choice:
            print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.")
            continue

        print("Computer Chose: " + computer)

        if player == computer:
            print("Draw")
        elif player == "rock" and computer == "paper":
            print("Computer Wins")
        elif player == "rock" and computer == "scissors":
            print("Player Wins")
        elif player == "paper" and computer == "scissors":
            print("Computer Wins")
        elif player == "paper" and computer == "rock":
            print("Player Wins")
        elif player == "scissors" and computer == "rock":
            print("Computer Wins")
        elif player == "scissors" and computer == "paper":
            print("Player Wins")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

main()
