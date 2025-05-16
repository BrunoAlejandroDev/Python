'''
Tente remover o número 2:
a. Primeiro usando remove()
b. Depois usando discard()
'''

numeros = {1, 3, 5, 7}
# remove = numeros.remove(2)
# print(f'Remocao com remove: {remove}')

discard = numeros.discard(2)
if discard:
    print('elemento encontrado e removido')
else:
    print('elemento nao encontrado')
print(f'Remocao com discard: {discard}')