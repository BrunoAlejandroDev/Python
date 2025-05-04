'''
Desenvolva um programa que leia 10 números inteiros e armazene-os em um
array. Encontre e exiba o menor e o maior valor presentes no array.
'''

lista_numeros = []
maior_valor = lista_numeros[0]
menor_valor = lista_numeros[0]

for i in range(1, 11):
    numeros = int(input(f'Digite o numero {i}: '))
    lista_numeros.append(numeros)

for numero in lista_numeros:
    if numero > maior_valor:
        maior_valor = numero
    if numero < menor_valor: 
        menor_valor = numero
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')