'''
Enunciado: Crie um programa que pergunta ao usuário a sua idade e o número de ingressos que deseja comprar para um cinema. O programa deve calcular e exibir o valor total a ser pago, considerando que cada ingresso custa R$ 25,00. Contudo, se a pessoa for menor de 18 anos ou maior de 60 anos, ela tem direito a 20% de desconto no valor total da compra.
'''

print('=== Cinema do Bruno ===')
idade = int(input('Digite a sua idade: '))
quant_ingressos = int(input('Digite a quantidade de ingressos que deseja: '))

preco_total = 0
preco_ingresso = 25
if idade < 18 or idade > 60:
    preco_ingressos = preco_ingresso - (preco_ingresso * 0.2)
    preco_total = quant_ingressos * preco_ingressos
else:
    preco_total = quant_ingressos * preco_ingresso
    
print(f'Valor total: R${preco_total}')