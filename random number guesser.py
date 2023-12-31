# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I1LJ-XTnDQpMIrKrtrrybN4R09oO3Ps7
"""

import random

def guess_number(secret_number, guess):
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "Congratulations! You guessed the number."

def main():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        result = guess_number(secret_number, guess)
        print(result)

        if result == "Congratulations! You guessed the number.":
            print(f"You guessed the number in {attempts} attempts!")
            break
        else:
            remaining_attempts = max_attempts - attempts
            print(f"You have {remaining_attempts} attempts left.\n")

    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    main()