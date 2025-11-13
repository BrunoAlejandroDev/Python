'''
Faturamento do melhor  do pior mês do ano
Pergunta: qual foi o valor de vendas do melhor mês do ano? e o valor do pior mês do ano?
'''

meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
valores_primeiro_semestre = [25000, 29000, 22200, 17750, 15870, 19900]
valores_segundo_semestre = [19850, 20120, 17540, 15555, 49051, 9650]

#* Juntas as duas listas em uma lista unica
valores_anuais = valores_primeiro_semestre + valores_segundo_semestre
print(f'Valores anuais: {valores_anuais}')

#* Maior valor de venda
maior_valor_venda = max(valores_anuais)
print(f'Maior valor de venda: R${maior_valor_venda}')

#* Menor valor de venda
menor_valor_venda = min(valores_anuais)
print(f'Menor valor de venda: R${menor_valor_venda}')

#* Descobrir o indice do maior valor para descobrir o mes correspondente
indice_maior_valor = valores_anuais.index(maior_valor_venda)
print(f'Indice do maior valor de venda: {indice_maior_valor + 1}')

mes_maior_valor = meses[indice_maior_valor]
print(f'Mes de maior valor: {mes_maior_valor}')

#* Descobrir o indice do menor valor para descobrir o mes correspondente
indice_menor_valor = valores_anuais.index(menor_valor_venda)
print(f'Indice do menor valor de venda: {indice_menor_valor + 1}')

mes_menor_valor = meses[indice_menor_valor]
print(f'Mes de menor valor: {mes_menor_valor}')

#? Segunda questao: agora relacione as duas listas para printar "O melhor mes do ano foi {} com {} vendas" e o mesmo para o pior mes do ano
print(f'O melhor mes do ano foi {mes_maior_valor} com R${maior_valor_venda}')
print(f'O pior mes do ano foi {mes_menor_valor} com R${menor_valor_venda}')

#? Terceira questao: calcular faturamento total e exibir os tres maiores valores da lista de valores anuais
#* Faturamento total do ano
faturamento_total = sum(valores_anuais)
print(f'Faturamento anual: R${faturamento_total:,}')

#* Representacao melhor mes no faturamento
representacao_melhor_mes = round((maior_valor_venda * 100) / faturamento_total, 2)
print(f'Porcentagem de representacao do melhor mes no faturamento anual: {representacao_melhor_mes}%')

#* Top 3 maiores valores do ano
lista_maiores_valores = []
for i in range(1, 4):
    maior_valor = max(valores_anuais)
    lista_maiores_valores.append(maior_valor)
    valores_anuais.remove(maior_valor)
print(lista_maiores_valores)