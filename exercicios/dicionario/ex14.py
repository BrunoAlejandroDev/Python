'''
Exercício: Contagem de Palavras
Crie uma função chamada contar_palavras que recebe uma frase (string) como argumento. A função deve retornar um dicionário onde cada chave é uma palavra da frase e o valor é o número de vezes que essa palavra aparece.
    Exemplo: Se a entrada for "o gato é um gato feliz", o retorno deve ser {'o': 1, 'gato': 2, 'é': 1, 'um': 1, 'feliz': 1}.
    Dica: Você pode usar o método .split() para transformar a frase em uma lista de palavras.
'''

def contar_palavras(texto):
    #* Formatar a frase
    texto_formatado = texto.lower().split()
    
    dicionario = {}
    for palavra in texto_formatado:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
            
    return dicionario
    
texto = 'o gato é um gato feliz'
print(contar_palavras(texto))