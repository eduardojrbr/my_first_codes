from time import sleep
print('=========================')
print('- CONFRATERNIZAÇÃO 2022 -')
print('=========================')
print('''Por favor, a fim de organizarmos nossa confraternização
esse ano, responda com sua opinião. Será importante. Obrigado!''')
option = 0
while True:
    print('''Escolha uma das opções abaixo:
    [1] Levar um prato
    [2] Pagar um buffet
    [3] Pedir a La carte
    [4] Não irei participar''')
    option = int(input('Escolha uma das opções: '))
    if option == 1:
        print('Sua opção foi registrada. Obrigado!')
        break
    elif option == 2:
        value = int(input('Até que valor você pagaria: '))
        print('Sua opção foi registrada. Obrigado!')
        break
    elif option == 3:
        sugest = str(input('Sua sugestão de restaurante: '))
        print('Sua opção foi registrada. Obrigado!')
        break
    elif option == 4:
        print('Que pena! Esperamos você na próxima.')
        break
    else:
        print('Opção inválida. Tente novamente.')
        sleep(2.5)
