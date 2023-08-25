import random
import time

opponent_variety = ("rock", "paper", "scissors")
opponent_select = random.choice(opponent_variety)

question_1 = input("Hey! Do you want to play Rock, Paper, Scissors with me?: ")
if question_1 == "yes":
    print("Great, let's get started!")
for i in range(1):
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    print("Shoot!")

player_select = input("Your Choice: ")
if player_select == opponent_select:
    print("Opponent Choice:", opponent_select)
    time.sleep(1)
    print("It's a tie!")
    time.sleep(1)

elif player_select == "rock":
    if opponent_select == "paper":
        print("Opponent Choice:", opponent_select)
        time.sleep(1)
        print("You Lose!")
        time.sleep(1)
    if opponent_select == "scissors":
        print("Opponent Choice:", opponent_select)
        time.sleep(1)
        print("You Win!")
        time.sleep(1)

elif player_select == "scissors":
    if opponent_select == "rock":
        print("Opponent Choice:", opponent_select)
        time.sleep(1)
        print("You Lose!")
        time.sleep(1)
    if opponent_select == "paper":
        print("Opponent Choice:", opponent_select)
        time.sleep(1)
        print("You Win!")
        time.sleep(1)

elif player_select == "paper":
    if opponent_select == "rock":
        print("Opponent Choice:", opponent_select)
        time.sleep(1)
        print("You Win!")
        time.sleep(1)
    if opponent_select == "scissors":
        print("Opponent Choice:", opponent_select)
        time.sleep(1)
        print("You Lose!")
        time.sleep(1)
