
#* Contador de Vogais: Crie uma função contar_vogais(texto) que percorra a string com um loop e retorne quantas vogais (a, e, i, o, u) ela tem.

def contar_vogais(texto):
    '''
    Docstring para contar_vogais
    
    :param texto: Descrição
    '''
    
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    contador_vogais = 0

    #* Loop para percorrer cada palavra do texto
    for palavra in texto:
        palavra_formatada = palavra.strip() #* formatacao para retirar espacos em branco
        #* Loop para percorrer cada letra da palavra atual
        for letra in palavra_formatada: 
            if letra in lista_vogais:
                contador_vogais += 1

    return contador_vogais

print(contar_vogais('arara azul branca'))