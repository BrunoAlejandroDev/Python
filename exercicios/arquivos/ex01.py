'''
Exercício 1: Diário Pessoal
Crie uma função chamada escrever_diario que recebe uma mensagem do usuário (usando input()) e a adiciona como uma nova linha em um arquivo chamado diario.txt. A cada nova execução, a nova mensagem deve ser adicionada ao final do arquivo, sem apagar as anteriores.
'''

def escrever_diario(texto):
    with open(r'C:\Users\Usuário\Downloads\diario.txt', 'a') as arquivo:
        arquivo.write(texto)
    
    arquivo.close() 

input_usuario = input('Digite sua mensagem: ')
escrever_diario(input_usuario)