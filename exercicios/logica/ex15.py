'''
Data: 16/06/25
Exercício: Conversor de Idade
Enunciado: Crie um programa que pergunte o ano de nascimento de uma pessoa e o ano atual. Com base nessas informações, calcule e exiba a idade da pessoa em anos, meses e dias. Considere que todo ano tem 365 dias e todo mês tem 30 dias para simplificar o cálculo.
Exemplo:
Ano de Nascimento: 1995
Ano Atual: 2025
Saída Esperada:
Idade em anos: 30
Idade em meses: 360
Idade em dias: 10950
'''

from datetime import datetime

def conversor_de_idade(ano_usuario):
    dia_atual = datetime.now()
    ano_atual = dia_atual.year

    idade_em_anos = ano_atual - ano_usuario
    idade_em_meses = idade_em_anos * 12
    idade_em_dias = idade_em_meses * 365

    return f'Idade em anos: {idade_em_anos}\nIdade em meses: {idade_em_meses}\nIdade em dias: {idade_em_dias}'

ano_nascimento_usuario = int(input('Digite o ano do seu nascimento: '))
retorno = conversor_de_idade(ano_nascimento_usuario)
print(retorno)