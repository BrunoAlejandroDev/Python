'''
Crie um script que leia a primeira linha de um arquivo chamado config.txt. Suponha que essa linha contenha o nome de um usuário. O seu programa deve ler esse nome e imprimir uma mensagem de boas-vindas, como: "Bem-vindo(a) de volta, [Nome do Usuário]!".

Para testar, crie manualmente o arquivo config.txt e escreva um nome nele.
'''

#* Criar o arquivo e adicionar um nome nele
arquivo = open(r'C:\Users\Usuário\Downloads\config.txt', 'w')
arquivo.write('Bruno')
arquivo.close()

#* Abrir o arquivo, ler suas informações e coletar o nome presente no arquivo
try:
    #* Abrir o arquivo no modo de leitura (r)
    with open(r'C:\Users\Usuário\Downloads\config.txt', 'r', encoding='utf-8') as file:
        primeira_linha = file.readline() #* ler apenas a primeira linha do arquivo
        nome = primeira_linha.strip() #* remover espaços em branco e quebras de linha
        
        print(f'Bem vindo(a) de volta, {nome}!') #* exibir nome presente no arquivo
        
except FileNotFoundError:
    print('Arquivo não encontrado')