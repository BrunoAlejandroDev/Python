
#* Importacao do modulo random
import random

#* Importacao de funcoes
from obter_palpite_jogador import obter_palpite

print('===== Bem Vindo(a) ao Jogo da Adivinhacao =====')

#* Gerar numero aleatorio que deve ser adivinhado
numero_secreto = random.randint(1, 100)

#* Definir numero de tentativas do jogador 
tentativas = 0

while True:
    
    #* Pegar palpite do jogador
    palpite_jogador = obter_palpite()
    
    #* Incrementar o numero de tentativas
    tentativas += 1
    
    if palpite_jogador == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        print(f"Você precisou de {tentativas} tentativas.")
        break
    elif palpite_jogador > numero_secreto:
        print('-- Muito alto. Tente novamente!')
    else:
        print('-- Muito baixo. Tente novamente!')