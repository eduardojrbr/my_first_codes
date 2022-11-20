from random import randint

print('-=-'*9)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-=-'*9)
v = 0
while True:
    player = int(input('Informe um valor de 1 a 10: '))
    computer = randint(1,10)
    soma = computer + player
    cond = ' ' 
    while cond not in 'PI':
        cond = str(input('Par ou Ímpar [P/I]: '))
    print(f'Você jogou {player} e o computador jogou {computer}. Total deu {soma}.')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    if cond == 'P':
        if soma %2==0:
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif cond == 'I':
        if soma % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print('GAME OVER!')
print(f'Você vence {v} vez(es).')
