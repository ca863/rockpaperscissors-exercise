import random

#Welcome player
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

#ask for user input
user_input = input("Please choose one of: 'rock', 'paper', 'scissors':") #asks for user input
user_input = user_input.lower() #converts to lower case to encompass all combinations

#validate user input
valid_choices = ["rock","paper","scissors"] #lists out the possible choices
if user_input not in valid_choices:
    print("That is not a valid choice, please try again!")
    user_input = input("Please choose one of: 'rock', 'paper', 'scissors':").lower
else:
    print("You chose:", u)


    #figure out how to do loops and 

#computer choice

computer_input = random.choice(valid_choices) #computer randomnly picks rock, paper or scissors
print("The computer chose: ", computer_input) #prints out the computer's choice

#determine the winner
if user_input == computer_input
    print("It's a tie!")
    elif

#display the results

#farewell message and option to play the game again?
print("Thanks for playing. Please play again!")