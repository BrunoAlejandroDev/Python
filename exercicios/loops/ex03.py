'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite o salario: '))
sexo = input('Digite seu sexo (m/f): ')
estado_civil = input('Digite seu estado civil (s, c, v, d): ')

while len(nome) < 3:
  print('Nome precisa ter pelo menos 3 caracteres')
  nome = input('Digite seu nome: ')

while idade <= 0 or idade > 100:
  idade = int(input('Digite sua idade: '))

while salario <= 0:
  salario = float(input('Digite o salario: '))

while (sexo != 'm') and (sexo != 'f'):
  sexo = input('Digite seu sexo (m/f): ')

while (estado_civil!='s') and (estado_civil!='c') and (estado_civil!='v') and (estado_civil!='d'):
  estado_civil = input('Digite seu estado civil (s, c, v, d): ')