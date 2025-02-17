import random

print("Hello, welcome to your game of High-Low!")
playerName = input("What is your name: ")

# Difficulty selection
while True:
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        maxNumber = 50
        break
    elif difficulty == "medium":
        maxNumber = 100
        break
    elif difficulty == "hard":
        maxNumber = 200
        break
    else:
        print("Invalid choice, please enter 'easy', 'medium', or 'hard'.")

# Gets the amount of attempts the user wants, can only accept valid numbers above 0
while True:
    try:
        attempts = int(input("How many tries would you like to have: "))
        if attempts < 1:
            print("Please enter a number bigger than 0")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

print(
    f"Nice to meet you, {playerName}! You will have {attempts} attempts. Let's start the game."
)

secretNumber = random.randint(
    1, maxNumber
)  # Generate a random number based on difficulty
previousGuesses = []  # Keeps track of previous guesses
hintUsed = False  # Tracks if the player used a hint

print(f"I have chosen a number between 1 and {maxNumber}. Try to guess it!")

# Main game logic
while attempts > 0:
    print(f"Previous guesses: {previousGuesses}")  # Show previous guesses

    # Accept input, allowing the player to request a hint once
    guess_input = input(
        f"You have {attempts} attempts left. Enter your guess (1-{maxNumber}) or type 'hint': "
    )

    if guess_input.lower() == "hint":
        if not hintUsed:
            hintRange = max(10, maxNumber // 10)  # The hint narrows the range
            lowerBound = max(1, secretNumber - hintRange)
            upperBound = min(maxNumber, secretNumber + hintRange)
            print(f"Hint: The number is between {lowerBound} and {upperBound}.")
            hintUsed = True
        else:
            print("You have already used your hint!")
        continue

    # Reject bad input
    try:
        guess = int(guess_input)
        if guess < 1 or guess > maxNumber:
            print(f"Please enter a number between 1 and {maxNumber}.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    previousGuesses.append(guess)

    if guess < secretNumber:
        print("Higher!")
    elif guess > secretNumber:
        print("Lower!")
    else:
        score = attempts * 10  # Score system
        print(
            f"Congratulations, {playerName}! You guessed the number {secretNumber} correctly!"
        )
        print(f"Your final score is: {score}")
        break

    attempts -= 1  # Adds to the amount of commits

if attempts == 0:
    print(f"Game over! The correct number was {secretNumber}.")

print(f"Thanks for playing, {playerName}!")
