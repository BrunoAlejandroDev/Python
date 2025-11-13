'''
Exercício 1: Diário Pessoal
Crie uma função chamada escrever_diario que recebe uma mensagem do usuário (usando input()) e a adiciona como uma nova linha em um arquivo chamado diario.txt. A cada nova execução, a nova mensagem deve ser adicionada ao final do arquivo, sem apagar as anteriores.

#? DICA: ao usar with open, não se faz necessário fechar o arquivo. O próprio with open faz esse trabalho.
#? DICA: é sempre bom colocar o tipo de codificação para não ter problemas com acentuação.
'''

def escrever_diario(texto):
    #* Criar o arquivo usando o modo "append" (a)
    with open(r'C:\Users\Usuário\Downloads\diario.txt', 'a', encoding='utf-8') as arquivo: 
        arquivo.write(f'{texto}\n') #* escreve a mensagem no arquivo e pula para a próxima linha

input_usuario = input('Digite sua mensagem no diario: ')
escrever_diario(input_usuario)