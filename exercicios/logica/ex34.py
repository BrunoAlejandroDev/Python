'''
Data: 18/07/25
Exercício 3: Jogo da Adivinhação de Números

Enunciado:
    Crie uma função jogo_adivinhacao que não recebe argumentos. Dentro dela, gere um número aleatório entre 1 e 50. Em seguida, peça ao usuário para adivinhar o número. O programa deve dar dicas se o palpite do usuário é "maior" ou "menor" que o número secreto. O jogo termina quando o usuário acerta, e a função deve retornar o número de tentativas que ele levou.

Observações:
    Utilize o módulo random para gerar o número aleatório (random.randint(1, 50)).

Exemplo de interação:
    (Número secreto é 25)
    Digite seu palpite: 10
    O número secreto é MAIOR.
    Digite seu palpite: 30
    O número secreto é MENOR.
    Digite seu palpite: 25
    Parabéns, você acertou!
    Saída (retorno da função): 3

Dicas:
    Use um laço while True para continuar pedindo palpites até que o usuário acerte.
    Crie uma variável para contar as tentativas e a incremente a cada palpite.

Habilidades desenvolvidas:
    Laços de repetição (while), decomposição do problema, entrada e saída de dados, uso de bibliotecas (random), lógica condicional.
'''

import random

def jogo_adivinhacao():
    
    #* Variaveis de maximo e minimo
    valor_inicial = 1
    valor_final = 20

    #* Passo 1: criar variavel de controle
    tentativas = 5

    #* Passo 2: gerar um numero aleatorio
    numero_aleatorio = random.randint(valor_inicial, valor_final)

    #* Passo 3: Criar lógica de execução
    while tentativas > 0:
        
        #* pedir um valor ao usuario
        numero_usuario = int(input(f'Digite um numero de {valor_inicial} a {valor_final}: '))

        if numero_usuario >= valor_inicial and numero_usuario <= valor_final:

            #* Passo 4: fazer a comparação de valor
            if numero_usuario == numero_aleatorio:
                print('Parabéns, você adivinhou o numero secreto!')
                break

            elif numero_usuario < numero_aleatorio:
                print('O numero que você digitou é menor que o numero secreto')
                tentativas -= 1

            elif numero_usuario > numero_aleatorio:
                print('O numero que você digitou é maior que o numero secreto')
                tentativas -= 1

        else:
            raise ValueError('Digite um numero valido')