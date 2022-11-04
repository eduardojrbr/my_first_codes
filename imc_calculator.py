print('====================')
print('---IMC CALCULATOR---')
print('====================')
weight = float(input('Inform your weight: '))
height = float(input('Inform your height: '))
imc = weight / (height**2)
print('---------------')
print('IMC calculation: {:.1f}'.format(imc))
print('---------------')
if imc < 18.5:
    print('\033[1;33mUNDER WEIGHT\033[m')
elif 25 > imc >= 18.5:
    print('\033[1;32mNORMAL WEIGHT\033[m')
elif 30 > imc >=25:
    print('\033[1;36mOVERWEIGHT\033[m')
elif 40 > imc >= 30:
    print('\033[1;35mOBESITY\033[m')
else:
    print('\033[1;31mMORBID OBESITY\033[m')
    