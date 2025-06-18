'''
Data: 18/06/25
Exercício: O Ajudante de Feira
Enunciado: Um feirante precisa de um programa simples para calcular o total a pagar por um tipo de fruta, baseado na quantidade comprada. O programa deve perguntar o nome da fruta, o preço unitário e a quantidade desejada. Ao final, deve exibir uma mensagem com o nome da fruta e o valor total da compra.
Exemplo:
Entrada:
Nome da fruta: Maçã
Preço unitário: 2.50
Quantidade: 4
Saída esperada:
O total para 4 unidades de Maçã é R$ 10.00.
'''

def calcular_total(quantidade, preco):
    return quantidade * preco

def main():
    nome_fruta = input('Digite o nome da fruta: ')
    preco_unidade = float(input('Digite o preco da fruta: '))
    quantidade = int(input('Digite a quantidade de frutas: '))

    preco_final = round(calcular_total(quantidade, preco_unidade), 2)

    print(f'O total para {quantidade} unidades de {nome_fruta} eh R$ {preco_final}.')

main()