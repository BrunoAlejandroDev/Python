'''
Crie uma função maior_e_menor(lista) que receba uma lista e retorne a maior e a menor nota (como tupla).
a) Use a função com uma lista [8.2, 5.6, 9.1, 7.0] e imprima o maior e o menor valor.
'''

def maior_menor(lista):
    maior_nota = lista[0]
    menor_nota = lista[0]

    for numero in lista:
        if numero > maior_nota:
            maior_nota = numero
        if numero < menor_nota:
            menor_nota = numero

    return maior_nota, menor_nota

lista = [8.2, 5.6, 9.1, 7.0]
tupla = tuple(maior_menor(lista))
print(tupla)