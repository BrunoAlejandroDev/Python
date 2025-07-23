'''
Exercício 3
Data: 23/07/2025

Enunciado: Crie uma função que receba uma string e verifique se ela é um palíndromo, ou seja, se pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda. A verificação deve ignorar espaços e não diferenciar maiúsculas de minúsculas.

Exemplo:
Entrada: "Anotaram a data da maratona" -> Saída: True
Entrada: "Python" -> Saída: False

Dicas:
    Primeiro, trate a string de entrada para remover os espaços e convertê-la para uma única caixa (maiúscula ou minúscula). Métodos como .replace() e .lower() são úteis.

    Uma forma de verificar se uma string é igual à sua versão invertida é usando a técnica de fatiamento (slicing): minha_string[::-1].

Habilidades desenvolvidas: Manipulação de strings, fatiamento (slicing), pensamento algorítmico, decomposição de problema.
'''

def verificar_palindromo(frase):

    #* Normalizar a frase
    frase_normalizada = frase.lower()

    #* Formatar a frase para tirar espaços em branco
    frase_formatada = frase_normalizada.replace(' ', '')

    #* Variavel para receber a palavra invertida
    frase_invertida = ''.join(reversed(frase_formatada))

    #* Verificar palindromo
    if frase_formatada == frase_invertida:
        print('Eh palindromo')
    else:
        print('Nao eh palindromo')

frase = 'O rato roeu a roupa do rei de roma'
verificar_palindromo(frase)