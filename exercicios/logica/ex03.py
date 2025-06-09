'''
Crie uma função chamada analisar_texto que recebe uma string (um parágrafo, por exemplo) e retorna um dicionário contendo três informações:
    total_palavras: o número total de palavras no texto.
    palavra_mais_longa: a palavra mais longa encontrada no texto.
    frequencia_vogais: um dicionário contando a frequência de cada vogal (a, e, i, o, u), desconsiderando acentos e maiúsculas/minúsculas.
'''

def analisar_texto(texto):
    palavra_mais_longa = ''
    frequencia_de_vogais = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0
    }
    
    palavras = texto.lower().split() # dividir o texto em uma lista de palavras em minusculo
    print(palavras)
    
    #* Total de Palavras
    total_palavras = len(palavras)
    
    for palavra in palavras:
        palavra_limpa = palavra.strip('.,!?;:') # remove pontuacoes para cada palavra
        
        #* Achar Palavra Mais Longa
        if len(palavra_limpa) > len(palavra_mais_longa): # verifica cada palavra e compara com a variavel palavra_mais_longa
            palavra_mais_longa = palavra_limpa
            
        #* Contar o Numero de Vogais
        for letra in palavra_limpa:
            if letra in frequencia_de_vogais:
                frequencia_de_vogais[letra] += 1
    
    dicionario = {
        'total_palavras' : total_palavras,
        'palavra_mais_longa' : palavra_mais_longa,
        'frequencia_vogais' : frequencia_de_vogais
    }
    return dicionario
    
texto = 'O Python é uma linguagem de programação poderosa e versátil.'
print(analisar_texto(texto))