
#* String para Lista: Crie uma função palavras_da_frase(frase) que receba uma string (ex: "Python é legal") e retorne uma lista de palavras (ex: ['Python', 'é', 'legal']).

palavra = 'tapioquinha branquinha bombom'

def palavras_da_frase(frase):
    palavra_separada = frase.split()
    return palavra_separada

print(palavras_da_frase(palavra))