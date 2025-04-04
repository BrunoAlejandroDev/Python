'''
Questão 2: Tratamento de Arquivos Inexistentes
Crie um programa que tenta abrir um arquivo chamado "dados.txt", lê seu conteúdo e o imprime na tela. Se o arquivo não existir, o programa deve capturar a exceção e exibir uma mensagem amigável.
'''

def abrir_arquivo():
    try:
        arquivo = open(r'C:\Python\dados.txt')
        print(arquivo.read())
    except FileNotFoundError as fnf:
        print(f'Error: {fnf}. O arquivo nao foi encontrado')

abrir_arquivo()