while True:
    print(' JUST $1 STORE ')
    product = float(input('Total amount of purchases: '))
    print('''Payment methods:
    [1] Cash/Check
    [2] Credit card due date
    [3] 2 Installments
    [4] 3 or more installments''')
    payment_method = str(input('Inform the payment method: '))
    if payment_method == '1':
        total = product - (0.10 * product)
        print('Your total amount is ${}. You have 10% Off. You need to pay ${}.'.format(product, total))
        break
    elif payment_method == '2':
        total = product - (0.05 * product)
        print('Your total amount is ${}. You have 5% Off. You need to pay ${}.'.format(product, total))
        break
    elif payment_method == '3':
        total = product
        installments = product / 2
        print('Your total amount is ${}. You have to pay 2x ${:.2f}'.format(product, installments))
        break
    elif payment_method == '4':
        total = product + (0.20 * product)
        total_inst = int(input('How many installments: '))
        installments = total / total_inst
        print('Your total amount is ${:.2f}. You have to pay {}x ${:.2f}.'.format(total, total_inst, installments))
        break
    else:
        print('\033[1;31mInvalid option. Try again.\033[m')


