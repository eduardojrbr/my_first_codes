sumage = 0
majorman = 0
oldmanname = 0
totalwoman20 = 0
totalman = 0
totalwoman = 0
for person in range(1,5):
    print(f' --- {person}ª pessoa ---')
    print('---------------------------')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip()
    print('--------------------------')
    sumage += age
    average = sumage/4
    if sex in "Ff":
        totalwoman += 1
    if sex in "Mm":
        totalman += 1
    if person==1 and sex in "Mm":
        majorman =  age
        oldmanname = name
    if sex in "Mm" and age>majorman:
        majorman = age
        oldmanname = name
    if sex in "Ff" and age<20:
        totalwoman20 += 1

print('A média de idade das pessoas informadas é de {:.0f} anos.'.format(average))
print(f'Ao todo, são {totalman} homem(s) e {totalwoman} mulher(s).')
print(f'O homem mais velho se chama {oldmanname} e tem {majorman} ano(s)')
print(f'Há {totalwoman20} mulher(s) com menos de 20 anos.')