'''
Data: 30/06/25
Exercício: Jogo da Forca - Validador de Palavra
Enunciado: No jogo da forca, o jogador tenta adivinhar uma palavra secreta letra por letra. A cada rodada, o jogador sugere uma letra. Crie uma função atualizar_palavra(palavra_secreta, palavra_mostrada, letra) que simule a lógica de atualização da palavra a ser exibida para o jogador.
    - palavra_secreta: A palavra completa que o jogador precisa adivinhar (ex: "PYTHON").
    - palavra_mostrada: Uma string com o estado atual do que o jogador vê, com underlines para letras não adivinhadas (ex: "_Y____").
    - letra: A letra que o jogador acabou de chutar (ex: "P").
    - A função deve retornar a nova palavra_mostrada após verificar a letra em todas as posições da palavra_secreta.

Exemplo:
    - Entrada: atualizar_palavra("PYTHON", "_Y____", "P")
    - Saída: "PY____"
    - Entrada: atualizar_palavra("LOGICA", "L_____", "A")
    - Saída: "L__I_A" (note que a letra "A" aparece duas vezes)

Dicas:
    Strings em Python são imutáveis. É mais fácil converter a palavra_mostrada para uma lista de caracteres, modificar a lista nas posições corretas e, ao final, juntar a lista de volta em uma string.
    Use um laço com enumerate para ter acesso tanto ao índice quanto ao caractere da palavra_secreta ao mesmo tempo.
'''

def atualizar_palavra(palavra_secreta, palavra_mostrada, letra_usuario):
    lista_palavra_mostrada = []
    for letra in palavra_mostrada:
        lista_palavra_mostrada.append(letra)
    print(lista_palavra_mostrada)

    #* Percorrer com enumerate a palavra secreta
    for indice, letra_palavra_secreta in enumerate(palavra_secreta):
        if letra_usuario == letra_palavra_secreta:
            lista_palavra_mostrada[indice] = letra_usuario

    return ''.join(lista_palavra_mostrada)

def main():
    palavra_secreta = 'python'
    palavra_mostrada = '_' * len(palavra_secreta)
    tentativas = 6
    letras_chutadas = []

    while '_' in palavra_mostrada and tentativas > 0:
        #* Mostrar status do usuario
        print(f'Palavra: {palavra_mostrada}')
        print(f'Tentativas: {tentativas}')
        print(f'Letras chutadas> {' '.join(letras_chutadas)}')

        #* Pedir letra ao usuario
        letra_usuario = input('Digite uma letra: ')

        #* Validacao de entrada
        if letra_usuario != 1 or not letra_usuario.isalpha():
            print('Por favor, digite uma letra valida.')
            continue
        if letra_usuario in letras_chutadas:
            print('Você ja chutou essa letra. Digite uma letra diferente')
            continue

        #* Atualizar lista de letras chutadas
        letras_chutadas.append(letra_usuario)

        #* Verificar se a letra esta na palavra secreta
        if letra_usuario in palavra_secreta:
            print('Parabens, a letra esta na palavra!')
            palavra = atualizar_palavra(palavra_secreta, palavra_mostrada, letra_usuario)
        else:
            print('Letra nao encontrada na palavra secreta. Tente novamente!')
            tentativas -= 1