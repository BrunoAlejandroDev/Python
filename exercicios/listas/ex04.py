'''
Crie um programa que leia 8 números inteiros e exiba todos os valores pares
armazenados no array.
'''
lista = []
for i in range(1, 9):
    lista_numeros = int(input(f'Digite o numero {i}: '))
    lista.append(lista_numeros)

for num in lista:
    if num % 2 == 0:
        print(num)

pares = [num for num in lista if num % 2 == 0]
print(pares)