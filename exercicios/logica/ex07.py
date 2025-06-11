'''
Escreva um programa que solicita um número inteiro positivo ao usuário e, em seguida, exibe uma contagem regressiva a partir desse número até 1. Durante a contagem, o programa deve indicar quais números são pares.
Exemplo:
Entrada: 10
Saída:
10 (É par)
9
8 (É par)
7
6 (É par)
5
4 (É par)
3
2 (É par)
1
'''

def regressiva_pares(numero):
    for num in range(1, numero+1)[::-1]:
        if num % 2 == 0:
            print(f'{num} (eh par)')
        else:
            print(num)

numero = int(input('Digite um numero: '))
regressiva_pares(numero)