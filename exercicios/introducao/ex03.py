'''
Escreva um programa que leia um número inteiro e um número decimal do teclado e, em 
seguida, exiba a soma desses números no console.
'''

def entrada_de_dados():
    numero_inteiro = int(input('Digite um numero inteiro: '))
    numero_decimal = float(input('Digite um numero decimal: '))
    
    soma = numero_inteiro + numero_decimal
    print(f'A soma dos numeros: {soma}')
    
entrada_de_dados()