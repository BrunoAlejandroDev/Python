'''
Data: 18/06/25
Exercício: Contador de Vogais e Consoantes
Enunciado: Crie uma função chamada contar_letras que recebe uma string (uma palavra ou frase) como argumento. A função deve contar e retornar o número de vogais e o número de consoantes na string. Ignore espaços e caracteres especiais, considerando apenas letras.
Exemplo:
Entrada: Lógica de Programação
Saída esperada: Vogais: 7, Consoantes: 13
Dicas:
Você pode criar uma string ou lista com todas as vogais para facilitar a verificação.
Lembre-se de tratar tanto letras maiúsculas quanto minúsculas, talvez convertendo a string de entrada para um único formato (ex: lower()).
'''

def contar_vogais_consoantes(palavra):
    #* Normalizar palavra e Desconsiderar espacao em branco
    palavra_normalizada = palavra.lower().replace(' ', '')

    #* Lista de vogais
    lista_vogais = ['a', 'e', 'i', 'o', 'u']

    numero_vogais = 0
    numero_consoantes = 0
    #* Percorrer a palavra depois percorrer cada letra e comparar
    for palavra in palavra_normalizada:
        for letra in palavra:
            if letra in lista_vogais:
                numero_vogais += 1
            else:
                numero_consoantes += 1

    return f'Vogais: {numero_vogais}\nConsoantes: {numero_consoantes}'

palavra = 'logica de programacao'
print(f'Palavra: {palavra}\n{contar_vogais_consoantes(palavra)}')