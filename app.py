import random  # Import the random module for generating random choices.

def game():  # Define the main function for the game
    player_score = 0  # Initialize player's score
    computer_score = 0  # Initialize computer's score
    choices = ['rock', 'paper', 'scissors']  # Define the possible choices

    for _ in range(3):  # Loop for three rounds of the game
        computer_choice = random.choice(choices)  # Computer makes a random choice

        # Ask the player for their choice
        # Ask the player for their choice
        player_choice = input("Type your choice (rock, paper, scissors) or quit: ").lower()
        if player_choice == 'quit':  # Allow the player to quit
            break
        elif player_choice not in choices:  # Check if the player's choice is valid
            print("Invalid choice. Please type rock, paper, scissors, or quit.")
            continue

        print(f"Computer chose {computer_choice}")  # Display the computer's choice

        # Determine the winner of the round
        if player_choice == computer_choice:  # If both choices are the same, it's a tie
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'scissors' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'rock'):  # Player wins the round
            player_score += 1
            print("You win this round!")
        else:  # Computer wins the round
            computer_score += 1
            print("Computer wins this round!")

        # Display the current scores
        print(f"Scores: Player - {player_score}, Computer - {computer_score}")

    # Determine and display the final winner
    if player_score > computer_score:
        print("You win the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("The game is a tie!")

game()  # Start the game