import random

#Welcome player (finished)
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

#ask for user input (finished)
user_input = input("Please choose one of: 'rock', 'paper', 'scissors':") #asks for user input
user_input = user_input.lower() #converts to lower case to encompass all combinations

#validate user input
valid_choices = ["rock","paper","scissors"] #lists out the possible choices

if user_input not in valid_choices:
    print("That is not a valid choice, please try again!")
    exit()

#computer choice (finished)
computer_input = random.choice(valid_choices) #computer randomnly picks rock, paper or scissors
print("The computer chose:", computer_input) #prints out the computer's choice

#determine the winner, adapted from Slack (finsihed) & display results
if user_input == computer_input:
    print("Both players played", user_input, "It's a tie!")
elif user_input == "paper":
    if computer_input == "rock":
        print("Paper covers rock. You won!")
    else:
        print("Scissors cuts paper. You lost! It's ok.")
elif user_input == "scissors":
    if computer_input == "paper":
        print("Scissors cuts paper. You won!")
    else:
        print("Rock crushes scissors. You lost! It's ok.")
elif user_input == "rock":
    if computer_input == "scissors":
        print("Rock crushes scissors. You won!")
    else:
        print("Paper covers rock You lost! It's ok.")

#farewell message
print("Thank you for playing! Please play again!")
