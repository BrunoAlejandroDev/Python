'''
Crie uma list comprehension que retorne apenas os nomes com mais de 4 letras de uma lista:
'''

lista_nomes = ['Bruno', 'Alicia', 'Joao', 'Ana', 'Fernando']
lista_maiores_nomes = [nome for nome in lista_nomes if len(nome) > 4]
print(lista_maiores_nomes)