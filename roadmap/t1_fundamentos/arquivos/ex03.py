'''
Escreva uma função adicionar_tarefa(tarefa) que recebe uma string como parâmetro e a escreve em um arquivo tarefas.txt. Cada tarefa deve ocupar uma única linha.
'''
import os

#* Criar a funcao
def adicionar_tarefa(tarefa):    
    try:
        with open(r'C:\Users\Usuário\Downloads\tarefa.txt', 'a', encoding='utf-8') as file:
            file.write(f'{tarefa}\n')        
    except FileNotFoundError:
        print('Arquivo nao encontrado.')
        
def main():
    tarefa = input('Digite uma tarefa para ser adicionada a lista: ')
    adicionar_tarefa(tarefa)
    print(f'-- tarefa {tarefa} adicionada com sucesso!')
    
if __name__ == '__main__':
    main()