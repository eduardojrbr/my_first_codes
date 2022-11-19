print('''Consulte a tabuada do número que desejar.
Para SAIR, digite um número negativo.''')
while True:
    number = int(input('Digite um número: '))
    print('------'*3)
    for t in range(1,11):
        print(f'{number} x {t} = {number*t}')
    print('-----'*3)
    if number < 0:
        break
print('PROGRAMA ENCERRADO')