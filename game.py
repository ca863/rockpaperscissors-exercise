#Welcome player (finished)
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("--------------------------------")
# This is extra credit Number 2
def determine_winner(user_input,computer_input):
    if(user_input == computer_input):
        winner = None
    if(user_input == "rock"):
        if(computer_input == "paper"):
           winner = "paper"
        if(computer_input == "scissors"):
            winner = "rock"
    if(user_input == "paper"):
        if(computer_input == "rock"):
           winner = "paper"
        if(computer_input== "scissors"):
           winner = "scissors"
    if(user_input == "scissors"):
        if(computer_input == "rock"):
           winner = "rock"
        if(computer_input == "paper"):
           winner = "scissors"
    return winner


#This is extra credit Number 1
import os
player_name = os.getenv("PLAYER_NAME", default="Player One")

#ask for user input (finished)
user_input = input("Please choose one of: 'rock', 'paper', 'scissors':") #asks for user input
valid_choices = ["rock","paper","scissors"] #lists out the possible choices
if user_input not in valid_choices:
    print("That is not a valid choice, please try again!")
    exit()
else:
    print("You chose:",user_input) #prints out user's input

#computer choice (finished)
import random
computer_input = random.choice(valid_choices) #computer randomnly picks rock, paper or scissors
print("The computer chose:", computer_input) #prints out the computer's choice
print("--------------------------------")

#determine the winner, adapted from Slack (finsihed) & display results
#if user_input == computer_input:
#else if user_input == "rock":
#if computer_input == "scissors":
# print("Rock crushes scissors. You won!")
#else:
#print("Paper covers rock You lost! It's ok.")
#print("Paper covers rock. You lost! It's ok.")

#print("--------------------------------")

winner = determine_winner(user_input,computer_input)
if (winner == None):
    print ("Game is a tie!")
if(winner == computer_input):
    print("Computer wins!")
if(winner == user_input):
    if(player_name == "Player One"):
        print("You won!")
    else:
        print(player_name, "wins!")

#farewell message
print("Thank you for playing! Please play again!")