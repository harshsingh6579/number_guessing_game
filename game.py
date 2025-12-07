import time
import random

print("Welcome to the Number guessing game! You will have seven chances to guess the number correctly")

time.sleep(4) # creates a 4 second gap for the following print statement

print("But First! Lets set up the range that you will be guessing from")

time.sleep(3)

low = int(input("Select a lower range: ")) # captures user input

high = int(input("Select an upper range: ")) # captures user input

random_number = random.randint(low, high)

chances = 7
guess_counter = 0
 
time.sleep(0.5)

print(f"Great! time to guess a number between {low} and {high}")

while guess_counter < chances: 
    guess_counter += 1
    guess = int(input(f"Guess a Number between {low} and {high}"))

    if guess == random_number:
        print(f"That's Correct! {guess} is the right Number. You've got it in the {guess_counter} attempt")
        break

    elif guess_counter >= chances and guess != random_number:
        print(f"Sorry! The Number was {random_number}, you have ran out of all the chances")

    elif guess > random_number:
        print(f"Hint: choose a Lower number")
    
    elif guess < random_number:
        print(f"Hint: choose a Higher number")