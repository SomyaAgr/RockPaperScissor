import random

while True:
    picks=["rock","paper","scissors"]

    computer= random.choice(picks)
    player=None

    while player not in picks:
        player= input("rock, paper, or scissors?: ").lower()


    if player == computer:
        print("computer: " ,computer)
        print("players: ",player)
        print("Tie!")
    elif player =="rock":
        if computer =="paper":
            print("computer: " ,computer)
            print("players: ",player)
            print("You lose: ")   
        if computer =="scissors":
            print("computer: " ,computer)
            print("players: ",player)
            print("You Win: ") 
    elif player =="scissors":
        if computer =="rock":
            print("computer: " ,computer)
            print("players: ",player)
            print("You lose: ")   
        if computer =="paper":
            print("computer: " ,computer)
            print("players: ",player)
            print("You Win: ") 
    elif player =="paper":
        if computer =="scissors":
            print("computer: " ,computer)
            print("players: ",player)
            print("You lose: ")   
        if computer =="rocks":
            print("computer: " ,computer)
            print("players: ",player)
            print("You Win: ") 
    
    play_again = input("play again? (yes/no): ").lower()

    if play_again !="yes":
        break

print("bye!!")