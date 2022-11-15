from random import randint
computer = randint(1,10)
print('Sou o seu computer. Acabei de pensar em um número de 0 a 10.')
print('Será que vocé é capaz de adivinhar?')
acertou = False
palpites = 0
while not acertou:
    player=int(input('Qual o seu palpite? '))
    palpites += 1
    if player==computer:
        acertou = True
    else:
        if player < computer:
            print('Mais! Tenta outra vez.')
        if player > computer:
            print('Menos! Tenta novamente.')
print(f'\033[1;32mNa mosca!\033[m Você precisou de {palpites} palpites.')