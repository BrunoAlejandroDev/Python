
#* importar modulo random
import random

#* Perguntar ao usuario qual o tamanho da senha que ele deseja criar
tamanho_senha = int(input('Digite a quantidade de caracteres da senha. A senha precisa ter pelo menos 5 caracteres: '))

#* Verificar se o numero enviado eh maior que o numero minimo
while tamanho_senha < 5:
    print('-- A senha precisa ter pelo menos 5 caracteres. Insira um valor correto')
    tamanho_senha = int(input('Digite a quantidade de caracteres da senha. A senha precisa ter pelo menos 5 caracteres: '))
    
    if tamanho_senha >= 5:
        break
    
caracteres_letras = 'abcdefghijklmnopqrstuvwyxz'
caracteres_numeros = '123456789'
caracteres_simbolos = '!@#%'
todos_caracteres = caracteres_letras + caracteres_numeros + caracteres_simbolos

senha = ''

for s in range(tamanho_senha):
    senha += random.choice(todos_caracteres)
        
print(senha)