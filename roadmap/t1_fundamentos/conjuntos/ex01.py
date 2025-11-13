'''
Crie um conjunto com os elementos 10, 20, 30, 40 e imprima:
O tipo da variável.
Se o número 20 pertence ao conjunto.
'''

conjunto = {10, 20, 30, 40}
print(type(conjunto))

if 20 in conjunto:
    print('sim')
else:
    print('nao')