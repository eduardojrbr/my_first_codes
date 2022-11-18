from time import sleep
print('Olá! Por favor, informe abaixo dois valores diferentes.')
value1 = int(input('Informe o 1º valor: '))
value2 = int(input('Informe o 2º valor: '))
option = 0
while option !=5:
    print('''Escolha uma das opões abaixo:
    [1] Somar valores
    [2] Mutiplicar valores
    [3] Mostrar maior valor
    [4] Informar novos valores
    [5] Sair''')
    option = int(input('Qual a sua opção? '))
    if option == 1:
        soma = value1+value2
        print(f'A soma entre {value1} e {value2} é {soma}.')
    elif option == 2:
        produto = value1 * value2
        print(f'O produto entre {value1} e {value2} é {produto}.')
    elif option == 3:
        if value1>value2:
            bigest = value1
        else:
            bigest = value2
        print(f'O maior valor entre {value1} e {value2} é {bigest}')
    elif option == 4:
        print('Informe novamente os valores:')
        value1 = int(input('Informe o 1º valor: '))
        value2 = int(input('Informe o 2º valor: '))
    elif option == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=-=-='*4)
    sleep(1)
print('Obrigado! Volte Sempre!')
