'''
i=1
while i<=10:  # print values from 1-10
    print(i)
    i=i+1

i=10
while i>=1:  # print values from 10-1
    print(i)
    i=i-1

moves = 15
winning_point = int(input("tell how many moves is required to win the game:"))
while moves >= 1:
    if 15- winning_point == moves:
        print("You won the game")
        break
    print(f"{moves} are left")
    moves-=1
else:
    print("GAME OVER")
'''
bullets = 10
while bullets > 0:
    print(f"you have {bullets} bullets, You can shoot them!!")
    bullets-=1
else:
    print("GAME OVER")
