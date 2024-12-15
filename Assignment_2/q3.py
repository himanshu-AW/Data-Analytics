# 3. Write a Python program to guess a number between 1 to 9.   
# Note : User is prompted to enter a guess. If the user guesses wrong then the  
# prompt appears again until the guess is correct, on successful guess, user will  
# get a "Well guessed!" message, and the program will exit.  

from random import randint

def guess_number():
    number = randint(1, 9)
    while True:
        user_guess = int(input("Guess a number: "))
        if user_guess == number:
            print("Well guessed!")
            break
        else:
            print("Incorrect guess. Try again.")

guess_number()