'''
Questão 1: Conversão Segura de Entrada do Usuário
Escreva um programa que solicite ao usuário um número inteiro e o converta corretamente. Se o usuário digitar um valor inválido (como letras ou símbolos), capture a exceção e exiba uma mensagem amigável solicitando que ele tente novamente.
'''


'''
#* Minha resposta:
import logging
try:
    num_inteiro = int(input('Digite um valor numerico: '))
    print(num_inteiro)
except ValueError as e:
    print(f'Erro: {e}. Por favor, insira um numero inteiro')
    num_inteiro = int(input('Digite um valor numerico: '))
'''

#* Resposta recomendada
while True: 
    try: 
        num_inteiro = int(input('Digite um valor numerico: '))
        print(f'Você digitou: {num_inteiro}')
        break
    except ValueError as e:
        print(f'Error: {e}. Por favor, insira um numero inteiro')