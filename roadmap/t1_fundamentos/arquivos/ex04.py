'''
Crie um script que leia todas as tarefas do arquivo tarefas.txt (criado no exercício anterior) e as exiba no console, numerando cada uma delas.
'''
try:
    with open(r'C:\Users\Usuário\Downloads\tarefa.txt', 'r', encoding='utf-8') as arquivo:
        print('=== Lista de Tarefas ===')
        
        #* Loop for com enumerate para percorrer a lista de tarefas e enumerar
        for indice, tarefa in enumerate(arquivo, start=1):
            print(f'{indice}: {tarefa.strip()}') #* o uso do strip serve para remover espaços em branco e quebras de linha
except FileNotFoundError:
    print('Arquivo nao encontrado.')