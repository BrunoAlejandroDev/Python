
#* Importacao do modulo random
import random

#* Gerar numero aleatorio que deve ser adivinhado
numero_aleatorio = random.randint(1, 100)

#* Solicitar palpite do usuario
num_usuario = int(input('Digite um numero entre 1 e 100: '))

num_eh_aceito = False

if num_usuario >= 1 and num_usuario <= 100:
    num_eh_aceito = True
    
while num_usuario < 1 or num_usuario > 100:
    print(f'ATENÇAO: Voce deve digitar um numero entre 1 e 100. O numero {num_usuario} nao eh aceito.')
    
    #* pedir novamente para usuario digitar um numero
    num_usuario = int(input('Digite um numero entre 1 e 100: '))
    
    if num_usuario >= 1 and num_usuario <= 100:
        num_eh_aceito = True
        break
    
if num_eh_aceito:
    while True:
        if num_usuario == numero_aleatorio:
            print('-- Parabens, voce acertou o numero!')
            break
        elif num_usuario > numero_aleatorio:
            print('-- Parece que seu palpite foi maior que o numero a ser adivinhado, tente novamente!')
            num_usuario = int(input('Digite um numero entre 1 e 100: '))
        else:
            print('-- Parece que seu palpite foi menor que o numero a ser adivinhado, tente novamente!')
            num_usuario = int(input('Digite um numero entre 1 e 100: '))