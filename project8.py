import logo
import os
print(logo.text)

playerScore = {
    "Virat Kohli": 82,
    "Babar Azam": 65,
    "Joe Root": 74,
    "Steve Smith": 91,
     "Kane Williamson": 58,
    "Rohit Sharma": 47,
    "David Warner": 33,
    "Ben Stokes": 27,
    "Shubman Gill": 76,
    "Marnus Labuschagne": 50
}
userScore = 0
#firstPlayer means current player and lastPlayer means the previous player
def upperlower(firstPlayer,lastPlayer):
    global userScore
    global userInput
    userInput = ""
    print(f"The score of {lastPlayer} is higher or lower than {firstPlayer}")
    
    def userSelection():
        userInput = input("Enter higher or lower : \n").lower()
        if userInput != "higher" or userInput != "lower":
            print(f"{firstPlayer} : {playerScore[firstPlayer]}  {lastPlayer} score :  {playerScore[lastPlayer]}")
            
    userSelection()
    
    score2 = playerScore[firstPlayer]
    score1 = playerScore[lastPlayer]
    
    if userInput == "higher" and score1 > score2:
        print("Correct ✔")
        userScore += 1
    elif userInput == "lower" and score1 < score2:
        print("Correct ✔")
        userScore += 1    
    else:
        print("Wrong 😌")
    os.system("cls")    
playersNames = []
for name in playerScore.keys():
    playersNames.append(name)
length = len(playersNames)    
for playerNo in range(0,length):
    if playerNo < (length - 1):
        preveiousPlayer = playersNames[playerNo]
        currentPlayer = playersNames[playerNo + 1]
        upperlower(firstPlayer=currentPlayer,lastPlayer=preveiousPlayer)
    else:
        break    
print(f"Your final score is {userScore}")    