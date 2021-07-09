# game.py

print("Rock, Paper, Scissors, Shoot!")


# ASK FOR A USER INPUT
# source https://docs.python.org/3/library/functions.html#input
# s = input('--> ')  

X= input("Please choose one of 'rock, 'paper', 'scissors': ")
print(x)

# VALIDATE THE USER INPUT

if (x == "rock") or (x == "paper") or (x == "scissors"): # "paper"  "scissors"
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

print("LATER MESSAGES")


# GENERATE A COMPUTER COICE
# source 

# import random

# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))

valid_options - ["rock", "paper", "scissors"] # list

c = random.choice(valid_options)

print("COMPTUER CHOSE"))



# DETERMINE THE WINNER

# DISPLAY THE FINAL CHOICE  