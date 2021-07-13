# game.py

import random
import os
#from dotenv import load_dotenv

#load_dotenv() #> loads contents of the .env file into the script's env

user_name = os.getenv("USER_NAME")

print(user_name) # reads the variable from the environment #> "Hello World"




exit()
print("Rock, Paper, Scissors, Shoot!")


# ASK FOR A USER INPUT
# source https://docs.python.org/3/library/functions.html#input
# s = input('--> ')  

x = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(x)

# VALIDATE THE USER INPUT

#if x == "rock": # "paper" "scissors"
#    print("VALID")
#else:
#   print("OOPS, INVALID, PLEASE TRY AGAIN")
#    exit()

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

#print("LATER MESSAGES")

print("USER CHOSE: ", x)

# GENERATE A COMPUTER CHOICE
# source https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#
# import random   
#
# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))


# valid_options - ("rock", "paper", "scissors") # tuple

valid_options = ["rock", "paper", "scissors"] # list

c = random.choice(valid_options)

print("COMPUTER CHOSE:", c)

# DETERMINE THE WINNER

if (c == x):
    print("tie")
elif(c == "rock") and (x == "scissors"):
    print("Computer won")
elif(c == "scissors") and (x == "rock"):
    print("You won")
elif(c == "paper") and (x == "rock"):
    print("Computer won")
elif(c == "rock") and (x == "paper"):
    print("You won")
elif(c == "scissors") and (x == "paper"):
    print("Computer won")
elif(c == "paper") and (x == "scissors"):
    print("You won")




