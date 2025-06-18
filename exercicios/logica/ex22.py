'''
Data: 18/06/25
Exercício: O Robô de Limpeza
Enunciado: Você está programando um robô de limpeza que se move em uma linha. Ele começa na posição 0. Crie uma função que recebe uma lista de comandos, onde cada comando é uma string: "DIREITA" ou "ESQUERDA". Para cada comando "DIREITA", a posição do robô aumenta em 1. Para cada comando "ESQUERDA", a posição diminui em 1. A função deve retornar a posição final do robô.
Exemplo:
Entrada: ["DIREITA", "DIREITA", "ESQUERDA", "DIREITA"]
Saída esperada: 2
Dica:
Inicialize uma variável para armazenar a posição do robô antes de começar a percorrer a lista de comandos.
'''

def automatizar_robo(lista_posicoes):
    posicao_robo = 0

    #* Iterar a lista de posicoes
    for posicao in lista_posicoes:
        posicao_normalizada = posicao.lower()
        if posicao_normalizada == 'direita':
            posicao_robo += 1
        elif posicao_normalizada == 'esquerda':
            posicao_robo -= 1
    return posicao_robo

lista_posicoes = ['DIREITA', 'DIREITA', 'ESQUERDA', 'DIREITA']
print(f'Posicao: {automatizar_robo(lista_posicoes)}')