'''
Exercício 5: Fatiamento de Listas (Slicing)

Descrição: Dada a lista letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
Crie uma nova lista contendo os três primeiros elementos de letras.
Crie uma nova lista contendo os elementos da posição 2 até a posição 5 (inclusive).
Crie uma nova lista contendo os últimos três elementos de letras.
Crie uma nova lista contendo todos os elementos de letras em ordem invertida, usando slicing.
Imprima todas as novas listas criadas.
'''

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

tres_primeiras_letras = letras[0 : 3]
for letra in tres_primeiras_letras:
    print(letra)

print()
nova_lista_letras = letras[2:6]
for letra in nova_lista_letras:
    print(letra)

print()
ordem_invertida = len(letras[-1])
for letra in letras[::-1]:
    print(letra)