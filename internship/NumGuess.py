import random
import math
name = input("Enter your name :")
lower = int(input("Enter the lower limit :"))
higher = int(input("Enter the higher limit :"))
randomNumber = random.randint(lower, higher)
no_of_guesses = 0
user_guess = None
print(f"Hello {name},play the game by using the guessing number between {lower} and {higher} in range")
print(f"You have {round(math.log(higher-lower+1,2))} no_of_guesses")
while(no_of_guesses < (math.log(higher-lower+1, 2))):
    user_guess = int(input(f"{name},enter your guess :"))
    no_of_guesses += 1
    if(user_guess == randomNumber):
        print(f"congratulations{name}!,you guessed the  exact number!\nYou win!")
        print(f"You guessed it in {no_of_guesses} guesses!")
        break
    else:
        if(user_guess > randomNumber):
            print(f"Sorry,{name},you guessed wrong! Enter a lower number")
            print(f"{name},You lose!")
            print(f"You have used {no_of_guesses} guesses. You have {round(math.log(higher-lower+1,2))-no_of_guesses} left.")
        else:
            print(f"Sorry,{name},you guessed wrong! Enter a higher number")
            print(f"{name},You lose!")
            print(f"You have used {no_of_guesses} guesses. You have {round(math.log(higher-lower+1,2))-no_of_guesses} left.")
        if no_of_guesses == round(math.log(higher-lower+1, 2)) and user_guess != randomNumber:
           print(f"{name},You couldn't guess the number correctly in {no_of_guesses} guesses.\n Unfortunately {name} you lose!,Better luck next time.")
           break

