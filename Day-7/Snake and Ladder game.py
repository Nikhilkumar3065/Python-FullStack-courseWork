import random    # throw random value
import sys
def dice():
    return random.randint(1,6)
player_1 = input("Enter the player1 Name:").title()
player_2 = input("Enter the player2 Name:").title()

player1_score,player2_score = 0,0
winning_point=100
snakes = {5:1,12:2,16:8,43:23,50:21,76:34}
ladders = {2:15,10:35,37:78,26:89,29:68}

def player1_turn():
    global player1_score
    player1_status = input(f"{player_1} You Want to [c]ontinue or [q]UIT:").lower()
    if player1_status=='c':
        cur_dic = dice()
        print(f'dice:{cur_dic}')
        if player1_score+cur_dic<=winning_point:
            player1_score+=cur_dic
            if player1_score>=winning_point:
                print(f'congrats {player_1} You won the GAME')
                sys.exit()  #to terminate the program
            if player1_score in snakes:
                player1_score = snakes[player1_score]
                print(f'Board position after snake:{player1_score}-----------------')
            elif player1_score in ladders:
                player1_score = ladders[player1_score]
                print(f'Board position after ladders: {player1_score}+++++++++++')
            if winning_point>100:
                sys.exit()
            else:
                print(f'Board position: {player1_score}')
        else:
            print(f'Board position: {player1_score} is same')
            
    else:
        print(f'congrats {player_2}, you won the GAME!!!!')

def player2_turn():
    global player2_score
    player2_status = input(f"{player_2} You Want to [c]ontinue or [q]UIT:").lower()
    if player2_status=='c':
        cur_dic = dice()
        print(f'dice:{cur_dic}')
        if player2_score+cur_dic<=winning_point:
            player2_score+=cur_dic
            if winning_point>100:
                sys.exit()
            if player2_score in snakes:
                player2_score = snakes[player2_score]
                print(f'Board position after snake: {player2_score}-----------------')
            elif player2_score in ladders:
                 player2_score = ladders[player2_score]
                 print(f'Board position after ladders: {player2_score}+++++++++++')
            else:
                print(f'Board position: {player2_score}')
        else:
            print(f'Board position: {player2_score} is same')
    else:
        print(f'congrats {player_1}, you won the GAME!!!!')

while player1_score<winning_point and player2_score<winning_point:
    player1_turn()
    player2_turn()
if player1_score>player2_score:
            print(f'congrats {player_1}, you won the GAME!!!!')
else:
    print(f'congrats {player_2}, you won the GAME!!!!')

    
