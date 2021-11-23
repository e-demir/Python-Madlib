import random

def play():
    user = input("What is your choise ?  'R' for rock, 'P' for paper, 'S' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It is a tie"

    if(is_win(user,computer)):
        return f"You won! Your choise is {user} and computers is {computer}"
    
    return "You lost!"
    
    # r > s, s > p, p > r

def is_win(player, opponent):
    # return true if player wins
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True

print(play())

