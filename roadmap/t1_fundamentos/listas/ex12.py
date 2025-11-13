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

tres_primeiras_letras = letras[:3]
print(f'Tres primeiras letras: {tres_primeiras_letras}')

elementos_do_meio = letras[2:6]
print(f'Fatia do meio da lista: {elementos_do_meio}')

tres_ultimas_letras = letras[-3:]
print(f'Tres ultimas letras: {tres_ultimas_letras}')

for letra in letras[::-1]:
    print(letra)