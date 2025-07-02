'''
Data: 02/07/25
Exercício: Frequência de Caracteres
Enunciado: Crie um programa que recebe uma frase como entrada e retorna um dicionário onde cada chave é um caractere da frase e o valor é o número de vezes que aquele caractere aparece. Ignore a diferença entre maiúsculas e minúsculas e desconsidere espaços.
Exemplo:
Entrada: "O sucesso e um professor perverso"

Saída (a ordem não importa): {'o': 5, 's': 5, 'u': 2, 'c': 1, 'e': 4, 'm': 1, 'p': 2, 'r': 3, 'f': 1, 'v': 1}
'''

def frequencia_caracteres(frase):

    dicionario = {} #* dicionario para armazenar os caracteres e suas quantidades
    frase_normalizada = frase.lower() #* normalizar a frase transformando todas as letras em minusculas

    #* Itera sobre cada palavra da frase
    for palavra in frase_normalizada: 
        palavra_sem_espaco = palavra.strip(' ') #* retirar espaço em branco de cada palavra

        #* Iterar sobre cada letra da palavra atual
        for letra in palavra_sem_espaco:
            chave_caractere = letra #* salvar cada letra em uma variavel
            if not chave_caractere in dicionario: #* verificar se a letra ja existe no dicionario
                dicionario[chave_caractere] = 1 #* caso nao, ele adiciona a letra como uma chave e coloca o valor 1 para ela
            else:
                dicionario[chave_caractere] += 1 #* caso a letra ja esteja no dicionario, ele adiciona mais um ao valor

    return dicionario

frase = 'O sucesso e um professor perverso'
print(frequencia_caracteres(frase))