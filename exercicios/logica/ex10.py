'''
Exercício: Contador de Vogais e Consoantes
Enunciado: Crie um programa que solicita ao usuário uma palavra e, em seguida, conta e exibe o número de vogais e o número de consoantes na palavra.
'''

from unidecode import unidecode

def contar_vogais_consoantes(palavra):
    #* Formatar a palavra
    palavra_formatada = palavra.lower().split()
    
    contador_vogais = 0
    contador_consoantes = 0 
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    
    #* Iterar sobre cada letra e verificar
    for palavra in palavra_formatada:
        palavra_limpa = unidecode(palavra)
        for letra in palavra_limpa:
            if letra in lista_vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1
    
    print(f'Numero de vogais: {contador_vogais}')
    print(f'Numero de consoantes: {contador_consoantes}')
    
palavra_usuario = input('Digite uma palavra: ')
contar_vogais_consoantes(palavra_usuario)