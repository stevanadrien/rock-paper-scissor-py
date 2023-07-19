import random

userPick = input("What do you pick? Rock, Paper, Scissor: ")
list = ["Rock", "Paper", "Scissor"]
randomPick = random.choice(list)
print(f"Your pick: {userPick}, Bot pick: {randomPick}")


def brain():
    if userPick == "Rock" and randomPick == "Rock":
        return "Draw"
    elif userPick == "Rock" and randomPick == "Paper":
        return "Lose"
    elif userPick == "Rock" and randomPick == "Scissor":
        return "Win"
    elif userPick == "Paper" and randomPick == "Rock":
        return "Win"
    elif userPick == "Paper" and randomPick == "Paper":
        return "Draw"
    elif userPick == "Paper" and randomPick == "Scissor":
        return "Lose"
    elif userPick == "Scissor" and randomPick == "Rock":
        return "Lose"
    elif userPick == "Scissor" and randomPick == "Paper":
        return "Win"
    elif userPick == "Scissor" and randomPick == "Scissor":
        return "Draw"
    else:
        return "Your pick is not valid"


brain()
print(f"You {brain()}")
