
#* Saudação: Crie uma função cumprimentar(nome) que receba um nome e retorne a string "Olá, [nome], seja bem-vindo!".

#* Criar a funcao com parametro padrao e retornar frase
def comprimentar(nome='Usuario'):
    return f'Ola, {nome}, seja bem vindo!'

#* Pedir nome ao usuario
nome = input('Digite seu nome: ')

#* chamar funcao e exibir resposta
print(comprimentar(nome))