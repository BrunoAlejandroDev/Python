'''
Crie um script que leia a primeira linha de um arquivo chamado config.txt. Suponha que essa linha contenha o nome de um usuário. O seu programa deve ler esse nome e imprimir uma mensagem de boas-vindas, como: "Bem-vindo(a) de volta, [Nome do Usuário]!".

Para testar, crie manualmente o arquivo config.txt e escreva um nome nele.
'''

arquivo = open(r'C:\Users\Usuário\Downloads\config.txt', 'w')
arquivo.write('Bruno')
arquivo.close()

with open(r'C:\Users\Usuário\Downloads\config.txt', 'r') as file:
    conteudo = file.readlines()
    nome = conteudo[0][:-1]
    print(f'Bem vindo(a) de volta, {nome}!')