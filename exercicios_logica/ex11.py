'''
Exercício: Somador de Intervalo
Enunciado: Escreva um programa que pede ao usuário dois números inteiros. O programa deve calcular e exibir a soma de todos os números inteiros que estão entre os dois números fornecidos (incluindo eles).
'''

def somador_de_intervalo(numero1, numero2):
    soma = 0
    
    if numero2 > numero1:
        for i in range (numero2, numero1+1):
            soma += i
    
    for i in range(numero1, numero2+1):
        soma += i
        
    return soma

v1 = 3
v2 = 4
print(somador_de_intervalo(v1, v2))