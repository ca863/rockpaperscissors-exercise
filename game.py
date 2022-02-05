#This is extra credit number 2
def determine_winner(user_input, computer_input):
    if (user_input == computer_input):
        winner = None
    if (user_input == "rock"):
        if (computer_input =="paper"):
            winner = "paper"
        if (computer_input == "scissors"):
            winner = "rock"
    if (user_input == "paper"):
        if (computer_input =="rock"):
            winner = "paper"
        if (computer_input == "scissors"):
            winner = "scissors"
    if (user_input == "scissors"):
        if (computer_input =="rock"):
            winner = "rock"
        if (computer_input == "paper"):
            winner = "scissors"
    return winner
if __name__ == "_main_":
    #This is extra credit number 1
    import os
    player_name = os.getenv("PLAYER_NAME", default="Player One")

    #Welcome player (finished)
    print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
    print("--------------------------------")

    #ask for user input (finished)
    user_input = input("Please choose one of: 'rock', 'paper', 'scissors':") #asks for user input
    user_input = user_input.lower() #converts to lower case to encompass all combinations

    #validate user input
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

    #determining winner (Extra Credit)
    winner = determine_winner(user_input, computer_input)

#determine the winner, adapted from Slack (finsihed) & display results
#if user_input == computer_input:
   # print("Both players played", user_input, "It's a tie!")
#elif user_input == "paper":
    #if computer_input == "rock":
        #print("Paper covers rock. You won!")
    #else:
        #print("Scissors cuts paper. You lost! It's ok.")
#elif user_input == "scissors":
    #if computer_input == "paper":
        #print("Scissors cuts paper. You won!")
    #else:
       # print("Rock crushes scissors. You lost! It's ok.")
#elif user_input == "rock":
    #if computer_input == "scissors":
       # print("Rock crushes scissors. You won!")
   # else:
      #  print("Paper covers rock. You lost! It's ok.")

    print("--------------------------------")

    if (winner == None):
        print("Game is a tie!")
    if (winner == computer_input):
        print("Computer wins :(")
    if (winner == user_input):
        if (player_name == "Player One"):
            print ("You Win!! :)")
        else:
            print(player_name, "wins! :")

    #farewell message
    print("Thank you for playing! Please play again!")
