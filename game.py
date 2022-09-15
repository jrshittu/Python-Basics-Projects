from random import randint
from time import sleep

rock = 1
paper = 2
scissors = 3

name = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
robot_score = 0

def start():
    print("Let's play the game of Rock, Paper and Scissors")
    while game():
        pass
    score()

def game():
    player = move()
    robot = randint(1, 3)
    result(player, robot)
    return play_again()

def move():
    while True:
        print()
        player = input("Rock = 1\n Paper = 2\n Scissors = 3\n Make a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            print("Ooops! I didn't understand that. Please enter 1, 2, or 3")
            
def result(player, robot):
    print("1...")
    sleep(1)
    print("2...")
    sleep(1)
    print("3!")
    sleep(0.5)
    print("Computer threw {0}!".format(name[robot]))
    global player_score, robot_score
    if player == robot:
        print("Tie")
    else:
        if rules[player] == robot:
            print("Player Won")
            player_score += 1
        else:
            print("You are being lectured by a robot")
            robot_score += 1
def play_again():
    answer = input("Like to play Again?Y/N:")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print("See you next time")
def score():
    global player_score, robot_score
    print("High Scores")
    print("player", player_score)
    print("robot", robot_score)

if __name__ == "__main__":
    start()
