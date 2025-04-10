import random
import os

computerChoice = random.randrange(1,51)

def gameLevel():
    global attempts
    Level = input("Select the game level (easy/hard): \n").lower()
    if Level == "hard":
        attempts = 5
    elif Level == "easy":
        attempts = 10
    else:
        print("Wrong entry please select the your game level")
        gameLevel()

gameLevel()        
def guessingGame(chosenNumber, userChoice):
    global attempts
    
    if chosenNumber == userChoice:
        print("You guessed correct")
        print(f"The correct number is {chosenNumber}")
        attempts = 0
    else:
        print("You guessed wrong number")
        print("Please try again")    
        if guessedNumber > 50 or guessedNumber < 0 :
            attempts -= 2
        else:    
            attempts -= 1 
        print(f"You have remaining attempts {attempts}")

print("Welcome to the number guessing game")
print("Guess the number in the given range,otherwise, you will lose two attempts")
print("\nYou can guess a number from 1 to 50")

while attempts != 0:
    guessedNumber = int(input("Guess the number : \n"))
    guessingGame(computerChoice , guessedNumber)
    