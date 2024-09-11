# Deposito
def deposito(saldo, valor, extrato):

    saldo += valor

    print(f'Deposito de R$ {valor:.2f} realizado com sucesso!')

    print(f'Seu saldo atual é de R$ {saldo:.2f}')

    extrato.append(f'Depósito de: R$ {valor:.2f}')

    return saldo

# Saque
def saque(saldo, valor, extrato, quantidade_saque, limite_saque=3):

    quantidade_saque += 1

    if valor > saldo:
        print('Saldo insuficiente!')

    elif valor <= 0:
        print('Valor inválido!')

    elif valor > 500:
        print('Valor máximo para saque é de R$ 500,00!')

    elif quantidade_saque > limite_saque:
        print('Limite de saques diários atingido, tente novamente amanhã!')

    else:
        saldo -= valor
        print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
        extrato.append(f'Saque de: R$ -{valor:.2f}')

        if quantidade_saque == 1:
            print(f'Você realizou o seu primeiro saque do dia, você poderá realizar mais {limite_saque - quantidade_saque} saques hoje.')
        
        elif quantidade_saque > 1 and quantidade_saque < 3:
            print(f'Você realizou {quantidade_saque} saques hoje, você pode realizar mais {limite_saque - quantidade_saque} saque hoje.')
        
        elif quantidade_saque == 3:
            print('''
                 ATENÇÃO!
    Este é o seu último saque do dia. 
                    :)
                  ''')
            
    return saldo

# Extrato
def ver_extrato(extrato, saldo):

    print('Extrato bancário:')

    for i in extrato:
                print(i)

    print(f'Seu saldo atual é de R$ {saldo:.2f}')

# Menu
def menu():

    print('\n1 - Depósito\n2 - Saldo\n3 - Saque\n4 - Extrato\n5 - Sair')

    escolha = int(input('Escolha uma opção: '))

    return escolha

def banco():

    saldo = 0
    quantidade_saque = 0
    extrato = []

    while True:

        # Menu
        escolha = menu()
        
        if escolha == 1:
            print('='*44)
            valor = float(input('Por favor, informe o valor a ser depositado: '))
            saldo = deposito(saldo, valor, extrato)
            print('='*44)

        elif escolha == 2:
            print('='*44)
            print(f'Seu saldo atual é de R$ {saldo:.2f}')
            print('='*44)

        elif escolha == 3:
            print('='*44)
            valor = float(input('Por favor, informe o valor a ser sacado: '))
            saldo = saque(saldo, valor, extrato, quantidade_saque)
            quantidade_saque += 1
            print('='*44)

        elif escolha == 4:
            print('='*44)
            ver_extrato(extrato, saldo)
            print('='*44)

        elif escolha == 5:
            print('='*44)
            print('Obrigado por utilizar nossos serviços!\nVolte sempre!')
            print('='*44)
            break

        else:
            print('Opção inválida!')

banco()