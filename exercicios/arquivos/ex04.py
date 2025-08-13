'''
Crie um script que leia todas as tarefas do arquivo tarefas.txt (criado no exercício anterior) e as exiba no console, numerando cada uma delas.
'''

with open(r'C:\Users\Usuário\Downloads\tarefa.txt', 'r') as arquivo:
    tarefa = arquivo.readlines()
    for indice, trf in enumerate(tarefa):
        trf = tarefa[0][:-1]
        print(f'{indice}: {trf}')