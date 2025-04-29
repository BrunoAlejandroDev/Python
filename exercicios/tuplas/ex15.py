'''
Crie uma lista animais = ["gato", "cachorro", "papagaio"].
a) Converta-a para tupla.
b) Tente alterar um dos elementos da tupla. O que acontece?
'''

animais = ['gato', 'cachorro', 'papagaio']
print(f'Lista: {animais}')
lista_para_tupla = tuple(animais)
print(lista_para_tupla)

lista_para_tupla[0] = 'coelho' # modificacao nao permitida pois tuplas sao imutaveis
print(lista_para_tupla)