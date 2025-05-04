'''
Escreva um programa que leia 10 números inteiros e calcule a média dos
valores inseridos, utilizando um array para armazenar os números.
'''

lista_numeros = []

for num in range(1, 11):
    num_usuario = int(input(f'Digite o numero {num}: '))
    lista_numeros.append(num_usuario)

media = sum(lista_numeros) / len(lista_numeros)
print(f'Media: {media}')