'''
Dado um dicionário com nomes e idades, filtre os nomes das pessoas com mais de 18 anos usando list comprehension:
'''

pessoas = {"Mel": 22, "Bob": 17, "Alicia": 19, 'Bruno' : 24}
maiores_idade = [chave for chave, valor in pessoas.items() if valor >= 18]
print(maiores_idade)