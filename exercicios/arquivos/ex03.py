'''
Escreva uma função adicionar_tarefa(tarefa) que recebe uma string como parâmetro e a escreve em um arquivo tarefas.txt. Cada tarefa deve ocupar uma única linha.
'''
import os

#* Criar o arquivo
arquivo = open(r'C:\Users\Usuário\Downloads\tarefa.txt', 'a')
arquivo.close()

#* Criar a funcao
def adicionar_tarefa(tarefa):
    #* Pegar o path do arquivo
    caminho_arquivo = r'C:\Users\Usuário\Downloads\tarefa.txt'

    try:
        #* Verificar se ele existe
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'a') as file:
                file.write(f'\n{tarefa}')  
        else:
            raise FileNotFoundError
        
    except FileNotFoundError:
        print('Arquivo nao existe')
        
def main():
    tarefa = input('Digite uma tarefa: ')
    adicionar_tarefa(tarefa)
    
if __name__ == '__main__':
    main()