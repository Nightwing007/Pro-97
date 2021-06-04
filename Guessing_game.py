import random

print("Number guessing game")

number = random.randint(1, 9)

chance = 0

print("Guess a number (between 1 and 9):")

while chance < 5:

    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chance += 1

if not chance < 5:
    print("YOU LOST!!! The number is", number)