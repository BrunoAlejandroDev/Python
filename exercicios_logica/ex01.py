'''
a) Enunciado:
Crie um programa que solicita ao usuário um número inteiro e verifica se ele é "Par e Positivo", "Ímpar e Positivo", "Par e Negativo", "Ímpar e Negativo" ou "Neutro" (caso seja zero). O programa deve imprimir a classificação correspondente.
'''

#* verificacao do valor
def verificar_valor(valor):
    if valor % 2 == 0 and valor > 0:
        return 'Par e Positivo'
    elif valor % 2 == 0 and valor < 0:
        return 'Par e Negativo'
    elif valor % 2 != 0 and valor > 0:
        return 'Impar e Positivo'
    elif valor % 2 != 0 and valor < 0:
        return 'Impar e Negativo'
    else:
        return 'Neutro'
    
#* entrada do usuario
entrada_usuario = int(input('Digite um numero: '))

#* chamada da funcao
print(verificar_valor(entrada_usuario))