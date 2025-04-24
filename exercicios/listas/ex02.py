'''
Desenvolva um programa que leia 5 números inteiros do usuário, armazene-os
em um array e calcule a soma de todos os elementos.
'''
lista_numeros = []
for i in range(1, 6):
    num_usuarios = int(input(f'Digite o numero {i}: '))
    lista_numeros.append(num_usuarios)

#* calcular a soma dos elementos
soma = sum(lista_numeros)
print(f'Soma: {soma}')