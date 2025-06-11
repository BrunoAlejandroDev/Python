'''
Enunciado: Crie um programa que pede ao usuário para digitar dois números inteiros. Se a soma dos dois números for maior que 100, o programa deve exibir a soma. Caso contrário, ele deve exibir o produto (a multiplicação) dos dois números.
Exemplo 1:
Entrada: 80, 30
Saída: 110
Exemplo 2:
Entrada: 10, 5
Saída: 50
'''

def somar_multiplicar(numero1, numero2):
    soma = numero1 + numero2
    if soma > 100:
        return f'A soma entre os dois numeros foi: {soma}'
    else:
        multiplicacao = numero1 * numero2
        return f'O produto entre os dois numeros foi: {multiplicacao}'
    
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
print(somar_multiplicar(numero1, numero2))