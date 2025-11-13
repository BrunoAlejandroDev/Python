'''
Descrição: Crie uma lista chamada minhas_frutas contendo os nomes de cinco das suas frutas favoritas.
Imprima a lista completa.
Imprima a primeira fruta da lista.
Imprima a terceira fruta da lista.
Imprima a última fruta da lista usando indexação negativa.
'''

minhas_frutas = ['Banana', 'Melao', 'Melancia', 'Maca', 'Uva']
for fruta in minhas_frutas:
    print(fruta)

primeira_fruta = minhas_frutas[0]
print(f'Primeira fruta: {primeira_fruta}')

for indice, fruta in enumerate(minhas_frutas):
    if indice == 2:
        print(minhas_frutas[indice])

ultima_fruta = minhas_frutas[-1]
print(f'Ultima fruta: {ultima_fruta}')