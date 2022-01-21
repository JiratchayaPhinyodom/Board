#Create Function
import random
def toss_dice():
    return random.randint(1,6) #Random dice to player

def initialize_list(p): #First, before start Round 1 create list each distance of players.
    list1 = []
    for i in range(p):
        list1.append(0) #In initializing append distance of players = 0.
    return list1

def print_distance_list(list1):
    for i in range(1,p+1):
        print(f"Player {i} : Distance = {i*list1}") #Show the result of the initializing.


def play_one_round(list1):
    for i in range(len(list1)):
        list1[i] = list1[i]+toss_dice()
        print(f"Player {i+1} : Distance = {list1[i]}") #Show the result of the playing and will increase every roundใ

def play_all_round(r,list1):
    for i in range(1,r+1):
        print(f"Round {i}")     #Show the result of the Round
        play_one_round(list1)  #And then use play_one_round(list1) function .

def find_winner(list1):
    return list1.index(max(list1)) #Find the player who have the most score.

#Show Result
p = int(input("Enter number of players: "))
r = int(input("Enter number of rounds: "))
list1 = initialize_list(p)
print("Initializing...")
print_distance_list(0)
print("Playing...")
play_all_round(r,list1)
print("Game Over...")
print(f"Player {find_winner(list1)} wins with maximum distance = {max(list1)}")