'''
Exercício 4
Data: 22/07/2025

Enunciado: Crie uma função que simule o resultado de um jogo de "Pedra, Papel e Tesoura". A função deve receber duas strings, jogador1 e jogador2, que podem ser "pedra", "papel" ou "tesoura". O retorno deve ser uma string indicando o vencedor: "Jogador 1 venceu", "Jogador 2 venceu" ou "Empate".

Exemplo:
Entrada: jogador1 = "pedra", jogador2 = "tesoura"
Saída: "Jogador 1 venceu"

Dicas:
Considere estruturar a lógica usando um dicionário para mapear as condições de vitória (ex: vitorias = {"pedra": "tesoura", ...}).
Lembre-se de tratar o caso de empate primeiro para simplificar as outras condições.

Habilidades desenvolvidas: Estruturas condicionais aninhadas (if/elif/else), pensamento algorítmico, dicionários, lógica de regras.
'''

jogada1 = 'papel'
jogada2 = 'tesoura'

vitorias = {
    'pedra' : 'tesoura',
    'tesoura' : 'papel',
    'papel' : 'pedra'
}

#* Verificar se ocorreu um empate
if jogada1 == jogada2:
    print('empate')

#* Verificar se jogador 1 venceu verificando se o valor da sua jogada está presente como chave no dicionário, se sim, comparar o valor que a chave possui
elif vitorias[jogada1] == jogada2:
    print('jogador 1 venceu')

#* Caso não seja empate nem vitória do jogador 1, jogador 2 venceu
else:
    print('jogador 2 venceu')