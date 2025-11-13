'''
Exercício 1
Data: 23/07/2025

Enunciado: Crie uma função que receba uma lista de palavras e retorne uma nova lista contendo apenas as palavras que têm 5 ou mais caracteres.

Exemplo:
Entrada: ["python", "sol", "logica", "céu", "desafio"]
Saída: ['python', 'logica', 'desafio']

Habilidades desenvolvidas: Manipulação de listas, laços de repetição (for), condicionais (if), função len().
'''

def contar_letras(lista_palavras):

    #* Criar a nova lista
    lista_palavras_finais = []

    #* Iterar sobre a lista de palavras 
    for palavra in lista_palavras:

        #* Normalizar cada palavra da lista
        palavra_normalizada = palavra.lower()

        #* Verificar o tamanho da palavra atual do loop 
        if len(palavra_normalizada) >= 5:
            
            #* Caso tenha mais de 5 caracteres, inserir na lista final
            lista_palavras_finais.append(palavra_normalizada)

    return lista_palavras_finais

Entrada = ["python", "sol", "logica", "céu", "desafio", 'java', 'garrafa', 'claro', 'pao', 'banana']
print(contar_letras(Entrada))