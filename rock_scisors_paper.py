from random import randint
from time import sleep
print('== ROCK, SCISORS AND PAPER ==')
print('Let us play!')
elements = ('Rock','Scisors','Paper')
computer = randint(0,2)
print('''Your options:
[0] Rock
[1] Scisors
[2] Paper''')
player = 0
computer = 0
wins = 0
while wins<3:
    player = int(input('Choose your option: '))
    if player > 2:
        print('Invalid option. Try again.')
        continue
    # else: 
        # break
    print('\033[1;30mRock...\033[m')
    sleep(1)
    print('\033[1;35mScisors...\033[m')
    sleep(1)
    print('\033[1;37mPaper!\033[m')
    sleep(1)
    print('=-='*10)
    print(f'Computer chose: {elements[computer]}.')
    print(f'Player chose: {elements[player]}.')
    print('=-='*10)
    if computer == 0: #computer chose (Rock)
        if player == 0:
            print('\033[1;34mended in a TIE!\033[m')
            print("Let's try again!")
        elif player == 1:
            print('\033[1;33mThe computer WON!\033[m')
            wins = wins+1
            computer=computer+1
        elif player == 2:
            print('\033[1;32mYou WON!\033[m')
            wins=wins+1
            player=player+1
    elif computer == 1: #computer chose (Scisors)
        if player == 0:
            print('\033[1;32mYou WON!\033[m')
            wins=wins+1
            player=player+1
        elif player == 1:
            print('\033[1;34mended in a TIE!\033[m')
            print("Let's try again!")
        elif player == 2:
            print('\033[1;33mThe computer WON!\033[m')
            wins=wins+1
            computer=computer+1
    elif computer == 2: #computer chose (Paper)
        if player == 0:
            print('\033[1;33mThe computer WON!\033[m')
            wins=wins+1
            computer=computer+1
        elif player == 1:
            print('\033[1;32mYou WON!\033[m')
            wins=wins+1
            player=player+1
        elif player == 2:
            print('\033[1;34mended in a TIE!\033[m')
            print("Let's try again!")
if player>computer:
    print('You is the WINNER!!!')
else:
    print('Computer is the WINNER!!!')