'''
Exercício 1
Data: 22/07/2025

Enunciado: Crie uma função que recebe uma string como argumento e retorna um dicionário contendo a contagem de cada vogal (a, e, i, o, u) presente na string. A contagem não deve diferenciar maiúsculas de minúsculas.

Exemplo:
Entrada: "Abacate"
Saída: {'a': 3, 'e': 1, 'i': 0, 'o': 0, 'u': 0}

Habilidades desenvolvidas: Manipulação de strings, laços de repetição (for), estruturas condicionais (if), dicionários.
'''

def contar_letras(palavra):
    
    #* Criar dicionario
    dicionario = {
        'a' : 0,
        'e' : 0,
        'i': 0,
        'o' : 0,
        'u' : 0
    }

    #* Iterar sobre cada letra da palavra
    for letra in palavra.lower(): #* usar lower para tornar todas as letras minusculas
        if letra in dicionario:
            dicionario[letra] += 1

    return dicionario

print(contar_letras('paralelepipedo'))