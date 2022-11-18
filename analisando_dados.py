from time import sleep
question = 'S'
count = soma = average = bigest = smaller = 0
while question in 'Ss':
    number = int(input('Digite um valor: '))
    count += 1
    soma += number
    if count == 1:
        bigest = smaller = number
    else:
        if number>bigest:
            bigest = number
        if number<smaller:
            smaller = number
    question = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
print('Finalizando...')
sleep(2.5)
average = soma/count                
print(f'''Valores digitados: {count}
Maior valor digitado: {bigest}
Menor valor digitado: {smaller}
Soma dos valores digitados: {soma}
Média dos valores digitados: {average}''')