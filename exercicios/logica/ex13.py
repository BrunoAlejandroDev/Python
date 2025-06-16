'''
Exercício: Contagem Regressiva para o Lançamento
Enunciado:
Escreva um programa que simule uma contagem regressiva para o lançamento de um foguete. O programa deve pedir ao usuário um número inteiro (ex: 10) e então imprimir na tela a contagem de forma decrescente, de um em um, até o 1. Ao final da contagem, o programa deve exibir a mensagem "Fogo!".
'''

def contador(numero):
    try:
        while numero <= 0:
            raise ValueError
        
        if numero > 0:
            for i in range(1, numero+1)[::-1]:
                print(i)
            print('Fogo!')
    
    except ValueError:
        print('Error. Por favor, digite um numero maior que zero.')
        numero_usuario = int(input('Digite um numero: '))
        contador(numero_usuario)

numero_usuario = int(input('Digite um numero: '))
contador(numero_usuario)
