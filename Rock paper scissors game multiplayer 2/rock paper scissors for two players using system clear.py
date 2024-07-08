import random
from os import system

while True:
    choices = ["rock","paper","scissors"]
    player1 = None
    player2 = None

    while player1 not in choices:
        player1 = input("rock, paper, or scissors?: ")
    system('clear')
    while player2 not in choices:
        player2 = input("rock, paper, or scissors?: ")
    system('clear')

    print("Player1: ",player1)
    print("Player2: ",player2)

    if player1 == player2:
        print("Tie!")

    elif player1 == "rock":
        if player2 == "scissors":
            print("You Win Player1!")
        if player2 == "paper":
            print("You Win Player2!")

    elif player1 == "paper":
        if player2 == "rock":
            print("You Win Player1!")
        if player2 == "scissors":
            print("You Win Player2!")

    elif player1 == "scissors":
        if player2 == "paper":
            print("You Win Player1!")
        if player2 == "rock":
            print("You Win Player2!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Byee!")