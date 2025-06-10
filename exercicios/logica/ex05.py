'''
Enunciado: Escreva uma função chamada analisar_texto que recebe uma string como argumento. A função deve retornar um dicionário contendo a contagem de três itens:

O número total de palavras na string.
O número de vogais (sem diferenciar maiúsculas de minúsculas).
A frequência de cada palavra (quantas vezes cada palavra aparece).
'''

def analisar_texto(texto):
    #* Formatar texto
    texto_formatado = texto.lower().split() # transformo em minusculas e separo o texto
    
    #* Descobrir total de palavras
    total_palavras = len(texto_formatado)
    
    #* Contar o numero de vogais
    total_vogais = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for palavra in texto_formatado:
        for letra in palavra:
            if letra in vogais:
                total_vogais += 1
    
    #* Descobrir a frequencia de palavras
    frequencia_palavras = {}
    for palavra in texto_formatado:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        else: 
            frequencia_palavras[palavra] = 1
    
    dicionario = {
        'total_palavras' : total_palavras,
        'numero_vogais' : total_vogais,
        'frequencia_de_palavras' : frequencia_palavras
    }
    return dicionario
    
texto = 'O rato roeu a roupa do rei de Roma e do Japao'
print(analisar_texto(texto))