import random

game=['rock','paper','scissors']
 
computer=''

you_point=0
computer_point=0 

loop_game=True


while(loop_game):



    you = input("select!(paper,rock,scissors) ")

    if you=="0":
        shart_bazi=False


    rand=random.randint(0,2)
    computer=game[rand]

    if you=="rock" and computer=='paper':
        computer_point=computer_point+1

    if you=='scissors' and computer=='paper':
        you_point=you_point+1


    if you=='rock' and computer=='scissors':
        you_point=you_point+1

    if you=='paper' and computer=='scissors':
        computer_point=computer_point+1


    if you=='scissors' and computer=='rock':
        computer_point=computer_point+1

    if you=='paper' and computer=='rock':
        you_point=you_point+1



    print("YOU: (", you_point  ,")",   you,"     COM:(", computer_point  ,")",computer)

    if you_point>=3 or computer_point>=3:
        loop_game=False




if you_point>computer_point:
    print("")
    print("YOU WIN!")
else:
    print("")
    print("YOU LOSE :(")

print("YOU: ",you_point)
print("COM: ",computer_point)

