from datetime import date
print('====================')
print('ALISTAMENTO MILITAR')
print('====================')
name = str(input('Informe o seu nome: '))
sex = str(input('Sexo: '))
if sex.capitalize() == 'Feminino':
    print('O alistamento militar obrigatório destina-se somente a individuos do sexo masculino.')
else:
    born = int(input('Informe o seu ano de nascimento: '))
    current = date.today().year
    correct = born + 18
    age = current-born
    if born < 2004:
        print('Você tem {} anos. Seu período de alistamento já venceu.'.format(age))
        print('Você deveria ter se alistado em {}. Já se passaram {} ano(s). Você se alistou?'.format(correct, (current - correct)))
    elif born == 2004:
        print('Você tem {} anos. ATENÇÃO! Você deve realizar alistamento militar no corrente ano.'.format(age))
        print('ALISTE-SE! Esperamos por você.')
    elif born > 2004:
        print('Você tem {} anos. Seu período de alistamento ainda não chegou, mas fique ligado!'.format(age))
        print('Você deve se alistar em {}. Falta(m) {} ano(s).'.format(correct, (correct - current)))



