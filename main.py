import random

while True:  # Outer loop to play multiple games
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

    # Gets the amount of attempts the user wants
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

    secretNumber = random.randint(1, maxNumber)
    previousGuesses = []
    hintUsed = False

    print(f"I have chosen a number between 1 and {maxNumber}. Try to guess it!")

    # Main game logic
    while attempts > 0:
        print(f"Previous guesses: {previousGuesses}")

        gameInput = input(
            f"You have {attempts} attempts left. Enter your guess (1-{maxNumber}) or type 'hint': "
        )

        if gameInput.lower() == "hint":
            if not hintUsed:
                hintRange = max(10, maxNumber // 10)
                lowerBound = max(1, secretNumber - hintRange)
                upperBound = min(maxNumber, secretNumber + hintRange)
                print(f"Hint: The number is between {lowerBound} and {upperBound}.")
                hintUsed = True
            else:
                print("You have already used your hint!")
            continue

        try:
            guess = int(gameInput)
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
            score = attempts * 10
            print(
                f"Congratulations, {playerName}! You guessed the number {secretNumber} correctly!"
            )
            print(f"Your final score is: {score}")
            break

        attempts -= 1

    if attempts == 0:
        print(f"Game over! The correct number was {secretNumber}.")

    print(f"Thanks for playing, {playerName}!")

    playAgain = input("Do you want to play again? (yes/no): ").lower()
    if playAgain == "no":
        break  # Exit the outer loop to stop playing
    elif playAgain != "yes":
        print("Invalid input. Assuming you want to play again.") #Handles invalid input

print("Goodbye!")