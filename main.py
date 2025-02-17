import random

print("Hello, welcome to your game of high-low")
playerName = input("What is your name: ")
attempts = input("How many tries would you like to have: ")
print(f"Nice to meet you, {playerName}! You will have {attempts}, let's start the game.")

# Generate a random number
secretNumber = random.randint(1, 100)
previousGuesses = []

print("I have chosen a number between 1 and 100. Try to guess it!")

while attempts > 0:
    print(f"Previous guesses: {previousGuesses}")  # Show previous guesses
    try:
        guess = int(input(f"You have {attempts} attempts left. Enter your guess (1-100): "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
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
        print(f"Congratulations, {playerName}! You guessed the number {secretNumber} correctly!")
        break
    
    attempts -= 1

if attempts == 0:
    print(f"Game over! The correct number was {secretNumber}.")

print(f"Thanks for playing, {playerName}!")
