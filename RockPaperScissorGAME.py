if __name__ == '__main__':
    import random  # here we are importing the random module

choices = ["rock", "paper", "scissors"]  # here we have 3 options

computer = random.choice(choices)  # he will randomly choose a option
# print(computer)
player = None

while player not in choices:
    player = input("rock, paper or scissors?: ").lower()

def Win():
    print("\nThe bot chose:", computer)
    print("The player chose: ", player)
    print("\nPlayer Wins!!!")

def Lose():
    print("\nThe bot chose:", computer)
    print("The player chose: ", player)
    print("\nPlayer loses!")

def Tie():
    print("\nThe bot chose:", computer)
    print("The player chose: ", player)
    print("\nit's a Tie!")

if player == computer:
    Tie()
elif player == "rock" and computer == "scissors":
    Win()
elif player == "paper" and computer == "rock":
    Win()
elif player == "scissors" and computer == "paper":
    Win()
else:
    Lose()
