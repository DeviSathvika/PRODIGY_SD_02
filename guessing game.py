import random

def guess_number_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number game!")
    print("I have generated a number between 1 and 100.")
    
    # Start the guessing loop
    while not guessed_correctly:
        # Get user input
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Increment the number of attempts
        attempts += 1
        
        # Compare the guess to the number
        if guess < number_to_guess:
            print("Your guess is too low. Try again.")
        elif guess > number_to_guess:
            print("Your guess is too high. Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the correct number {number_to_guess}!")
            print(f"It took you {attempts} attempts to guess the number correctly.")

# Run the game
guess_number_game()
