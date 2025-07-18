'''
Data: 18/07/25
Exercício 2: Contador de Vogais

Enunciado: Escreva uma função chamada contar_vogais que recebe uma string e retorna a quantidade de vogais (a, e, i, o, u) presentes nela. A função não deve diferenciar maiúsculas de minúsculas.

Exemplo:
Entrada: 'Abacaxi'
Saída: 4

Entrada: 'Python'
Saída: 1

Habilidades desenvolvidas: Laços de repetição (for), estruturas condicionais, manipulação de strings (lower/upper), listas.
'''

def contar_vogais(palavra):

    #* Normalizar a palavra
    palavra_normalizada = palavra.lower()

    #* Lista de vogais para posterior comparação
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    
    #* Variavel contadora
    contador_vogais = 0

    #* Loop para percorrer cada letra da palavra
    for letra in palavra_normalizada:
        #* Para cada letra, verificar se esta presente na lista
        if letra in lista_vogais:
            contador_vogais += 1

    return contador_vogais

palavra = 'python'
print(contar_vogais(palavra))