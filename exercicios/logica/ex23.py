'''
Data: 19/06/25
Exercício: Calculadora de Média Ponderada
Enunciado: Escreva um programa que calcula a média ponderada de três notas. O programa deve solicitar ao usuário as três notas e seus respectivos pesos. A média ponderada é calculada pela fórmula da media ponderada
Exemplo:
Entrada:
Nota 1: 8.0, Peso 1: 2
Nota 2: 7.0, Peso 2: 3
Nota 3: 9.0, Peso 3: 5
Saída: A média ponderada é 8.3.
'''

def calcular_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
    return media

def main():
    nota1 = float(input('Digite a primeira nota: '))
    peso1 = float(input('Digite o peso da primeira nota: '))
    
    nota2 = float(input('Digite a segunda nota: '))
    peso2 = float(input('Digite o peso da segunda nota: '))
    
    nota3 = float(input('Digite a terceira nota: '))
    peso3 = float(input('Digite o peso da terceira nota: '))
    
    media = calcular_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3)
    print(f'A média ponderada é {media}')
        
main()