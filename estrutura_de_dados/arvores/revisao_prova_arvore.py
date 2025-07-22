''''
EXERCICIO ARVORE BINARIA DE BUSCA - LIVROS
'''

class Livro:
    '''
    Classe para representar um objeto Livro.
    Possui código e titulo como propriedades
    '''
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        
    def __str__(self):
        return f'{self.codigo} | {self.titulo}'
    
class Node:
    '''
    Classe para representar um nó da árvore.
    Cada nó será responsável por armazenar um livro, além de possuir acessos aos filhos da esquerda e direita.
    '''
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None
        
livro1 = Livro(1, 'Vespera')
no = Node(livro1)
print(no.livro.titulo)