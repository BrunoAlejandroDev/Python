'''
Data: 01/07/25
Exercício 6: Consulta em Dados Aninhados
    Imagine que você tem dados de alunos armazenados em um dicionário aninhado. Crie uma função chamada consultar_nota que recebe o nome de um aluno, a matéria e o dicionário de dados. A função deve retornar a nota do aluno na matéria especificada.

Dados:
    dados_alunos = {
        'João': {'matematica': 9.5, 'portugues': 8.0, 'ciencias': 7.5},
        'Maria': {'matematica': 10.0, 'portugues': 9.0, 'ciencias': 8.5},
        'Pedro': {'matematica': 7.0, 'portugues': 6.5, 'ciencias': 6.0}
    }

Exemplo de uso: consultar_nota('Maria', 'matematica', dados_alunos) deve retornar 10.0.

Desafio extra: Faça a função retornar a mensagem "Aluno não encontrado" ou "Matéria não encontrada" se for o caso, utilizando tratamento de exceções (try...except KeyError).
'''

dados_alunos = {
    'João': {'matematica': 9.5, 'portugues': 8.0, 'ciencias': 7.5},
    'Maria': {'matematica': 10.0, 'portugues': 9.0, 'ciencias': 8.5},
    'Pedro': {'matematica': 7.0, 'portugues': 6.5, 'ciencias': 6.0}
}

for nome, dados in dados_alunos.items():
    print(dados)
    for materia, nota in dados:
        print(materia)
            
        # if nome_aluno in nome:
        #     print(f'Aluno: {nome_aluno}\nNota {dados[f"{materia}"]} em {dados[f"{materia}"]}') 
    
