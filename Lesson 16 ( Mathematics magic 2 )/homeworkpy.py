import random

correct_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == correct_number:
    print("You guessed correctly.")
else:
    print(f"Wrong guess. The correct number was {correct_number}.")
