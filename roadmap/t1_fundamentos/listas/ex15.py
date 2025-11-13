'''
Exercício 8: Lista de Compras Interativa
    Descrição: Crie um programa que simule uma lista de compras. O programa deve permitir ao usuário:
    Adicionar um item à lista.
    Remover um item da lista (o usuário deve digitar o nome do item a ser removido).
    Visualizar a lista de compras atual.
    Sair do programa.
    Utilize um laço while para manter o programa em execução até que o usuário escolha sair.
    Use input() para obter as escolhas e os itens do usuário.
    Trate o caso de tentar remover um item que não está na lista (exiba uma mensagem amigável).
'''

print('=== Lista de Compras ===')

lista_compras = []
while True:
    print('1. Adicionar um item na lista')
    print('2. Remover um item da lista')
    print('3. visualizar a lista de compras atual')
    print('4. sair')
    escolha_usuario = int(input('Digite sua opcao: '))
    
    if escolha_usuario == 1:
        produto = input('Digite o nome do produto a ser adicionado: ').lower()
        lista_compras.append(produto)
        print(f'Produto {produto} adicionado com sucesso\n')
        
    elif escolha_usuario == 2:
        if len(lista_compras) == 0:
            print('Lista vazia. Nao existem produtos para remover\n')
        else:
            produto_removido = input('Digite o nome do produto a ser removido: ').lower()
            for produto in lista_compras:
                if produto == produto_removido:
                    lista_compras.pop(produto)
            print(f'Produto {produto_removido} nao encontrado\n')
            
    elif escolha_usuario == 3:
        if len(lista_compras) == 0:
            print('A lista de compras esta vazia.\n')
        else:
            print('\nLista de compras:')
            print(lista_compras)
        
    elif escolha_usuario == 4:
        break
    
    else:
        print('Digite um valor valido')