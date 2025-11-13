'''
Data: 02/07/25
Exercício: Simulador de Caixa Eletrônico (Gerenciamento de Estado)

Enunciado: Crie uma função que simula as operações básicas de um caixa eletrônico. A função deve inicializar com um saldo = 1000. Em seguida, entrar em um loop while que pergunta ao usuário qual operação ele deseja realizar: 1-Depositar, 2-Sacar, 3-Ver Saldo, 4-Sair.

    Depositar: Pede um valor ao usuário e o adiciona ao saldo.
    Sacar: Pede um valor ao usuário e o subtrai do saldo, mas apenas se houver saldo suficiente.
    Ver Saldo: Apenas exibe o saldo atual.
    Sair: Encerra o loop e o programa.
'''


# def depositar(valor, saldo_conta):
#     saldo_conta += valor
#     return f'Saldo atual: {saldo_conta}'

# def caixa_eletronico(operacao):
#     saldo_conta = 1000
#     if operacao == 1:
#         print('Opcao Deposito escolhida.\nIniciando processo de deposito...\n')
#         valor = float(input('Digite o valor do deposito: '))
#         print(depositar(valor, saldo_conta))

def main():
    saldo_conta = 1000
    print('Bem vindo ao banco\n')

    while True:
        print('Operacoes disponiveis')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Ver saldo')
        print('4. sair')

        operacao = int(input('Digite a operacao desejada: '))

        if operacao == 4:
            quit()

        elif operacao == 1:
            print('\nOpcao Deposito escolhida.\nIniciando processo de deposito...\n')
            valor = float(input('Digite o valor do deposito: '))
            saldo_conta += valor
            print(f'\nDeposito efetuado com sucesso!\nSaldo atual: {saldo_conta}\n')

        elif operacao == 2:
            print('\nOpcao Saque escolhida.\nIniciando processo de saque...\n')
            saque = float(input('Digite o valor do saque: '))

            if saque > saldo_conta:
                print('Erro. Saque maior que valor disponivel em conta.\n')
                continue
            else:
                saldo_conta -= saque
                print('\nSaque realizado com sucesso!')
            
            print(f'Saldo atual: {saldo_conta}\n')

        elif operacao == 3:
            print(f'\nSaldo atual: {saldo_conta}\n')

        else:
            print('Erro. Digite uma opcão válida.')
            continue

if __name__ == '__main__':
    main()