'''
Data: 18/06/25
Exercício: Catraca de Acesso
Enunciado: Crie um programa que simula uma catraca de acesso a um evento. O programa deve perguntar a idade do usuário. Se a idade for 18 anos ou mais, ele deve exibir a mensagem "Acesso liberado". Caso contrário, deve exibir "Acesso negado".
Exemplo:
Entrada: 25
Saída esperada: Acesso liberado.
Entrada: 16
Saída esperada: Acesso negado.
'''

def liberar_entrada(idade):
    if idade >= 18:
        return 'Acesso liberado.'
    else:
        return 'Acesso negado.'

print('Sistema de acesso iniciado. Digite 999 para sair\n')
while True:
    try:
        verificar_idade = int(input('Digite a sua idade: '))
        if verificar_idade <= 0:
            raise ValueError
        if verificar_idade == 999:
            break
        print(liberar_entrada(verificar_idade))
    except ValueError:
        print('Error. Digite um valor de idade válida')