'''
Exercício 5: Contador de Palavras
Crie uma função contar_palavras(caminho_arquivo) que recebe o nome de um arquivo como parâmetro, lê seu conteúdo e retorna o número total de palavras no arquivo.

Dica: Você pode usar o método .split() para separar o texto em palavras.

Crie um arquivo de teste artigo.txt com algum texto para validar sua função.
'''

def escrever(caminho_arquivo, texto):
    '''
    Função para escrever palavras em um arquivo.
    '''
    with open(caminho_arquivo, 'a', encoding='utf-8') as file:
        file.write(f'{texto}\n')

def contar_palavras(arquivo):
    '''
    Função para contar a quantidade de palavras presentes em um arquivo
    '''
    try:
        #* Ler todo o conteúdo presente no arquivo
        with open(arquivo, 'r', encoding='utf-8') as file:
            conteudo_arquivo = file.read() #* o read serve para ler todo o conteudo presente em um arquivo
            
            #* Separar o conteudo do arquivo em palavras
            total_palavras = conteudo_arquivo.split() #* o split serve para separar por espaços
            
            #* Contar a quantidade de palavras
            return len(total_palavras)
    except FileNotFoundError:
        print('Arquivo nao encontrado.')

def main():
    caminho_arquivo = 'meu_arquivo.txt'
    texto = 'Esta é uma frase de exemplo.\nEla tem várias linhas e várias palavras.'
    
    #* Executar função para escrever no arquivo
    escrever(caminho_arquivo, texto)
    
    #* Executar função para contar o número de palavras
    total_palavras = contar_palavras(caminho_arquivo)
    print(f'Total de palavras: {total_palavras}')
    
if __name__ == '__main__':
    main()