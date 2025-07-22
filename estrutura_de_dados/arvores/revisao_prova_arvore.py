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
        
class BinaryTree:
    #* Criar o construtor da arvore e definir sua raiz como None
    def __init__(self):
        self.root = None 
    
    #* ===== PROCESSO DE INSERÇÃO =====
    def insert(self, livro):
        #* Verificar se a arvore está vazia
        if self.root is None:
            novo_no = Node(livro) #* criar novo nó para ser inserido na arvore
            self.root = novo_no #* define a raiz da arvore como sendo o novo nó
            print('Novo no inserido na raiz')
        
        #* Caso a arvore não esteja vazia, chamar função recursiva
        else:
            self._insert(self.root, livro)
            
    def _insert(self, no_atual, livro):
        
        print('Iniciar processo de insercao recursiva')
        
        #* Caso 1: Verificar se valor do nó é menor que o do nó atual
        
        #* Verificar se o valor atual do no é menor que o valor do nó que será verificado, se sim ir para a esquerda
        if livro.codigo < no_atual.livro.codigo:
            #* Verificar se o no da esquerda está vazio
            if no_atual.esquerda is None:
                novo_no = Node(livro) #* criar novo nó
                no_atual.esquerda = novo_no #* inserir o novo nó na esquerda do nó atual
                print('-- valor inserido no nó da esquerda')
            #* Caso o nó da esquerda já possua elemento, chamar a função recursiva passando o no_atual.esquerda
            else:
                self._insert(no_atual.esquerda, livro)
                
        #* Caso 2: Verificar se o valor do nó é maior que o do nó atual
        else:
            #* Verificar se o nó da direita está vazio
            if no_atual.direita is None:
                novo_no = Node(livro) #* criar novo nó
                no_atual.direita = novo_no #* inserir o novo nó na esquerda do nó atual
                print('-- valor inserido no nó da direita')
            
            #* Caso nó da direita esteja com algum valor, chamar função recursiva para o no_atual.direita
            else:
                self._insert(no_atual.direita, livro)
                
    #* ===== PROCESSO DE PERCURSO =====
    
    #* Percurso 1 - In-Order
    def in_order_traverse(self):
        lista_livros = []
        self._in_order_traverse(self.root, lista_livros)
        return lista_livros
    
    def _in_order_traverse(self, no_atual, lista_livros):
        
        #* Verificar se o nó não existe
        if no_atual is None:
            return
        
        #* Passo 1 - ir para a esquerda
        self._in_order_traverse(no_atual.esquerda, lista_livros)
        
        #* Passo 2 - processar o nó atual
        lista_livros.append(no_atual.livro)
        
        #* Passo 3 - ir para a direita
        self._in_order_traverse(no_atual.direita, lista_livros)
    
    #* Percurso 2 - Pre-Order
    def pre_order_traverse(self):
        lista_livros = []
        self._pre_order_traverse(self.root, lista_livros)
        return lista_livros
    
    def _pre_order_traverse(self, no_atual, lista_livros):
        
        #* Verificar se o nó não existe
        if no_atual is None:
            return
        
        #* Passo 1 - processar o nó atual
        lista_livros.append(no_atual.livro)
        
        #* Passo 2 - ir para a esquerda
        self._pre_order_traverse(no_atual.esquerda, lista_livros)
        
        #* Passo 3 - ir para a direita
        self._pre_order_traverse(no_atual.direita, lista_livros)
        
    #* Percurso 3 - Post-Order 
    def post_order_traverse(self):
        lista_livros = []
        self._post_order_traverse(self.root, lista_livros)
        return lista_livros
    
    def _post_order_traverse(self, no_atual, lista_livros):
        
        #* Verificar se o nó não existe
        if no_atual is None:
            return
        
        #* Passo 1: ir para a esquerda
        self._post_order_traverse(no_atual.esquerda, lista_livros)
        
        #* Passo 2 - ir para a direita
        self._post_order_traverse(no_atual.direita, lista_livros)
        
        #* Passo 3 - processar o nó atual
        lista_livros.append(no_atual.livro)
    
livro1 = Livro(1, 'Vespera')
livro2 = Livro(3, 'O Alquimista')
livro3 = Livro(7, 'Solaris')
livro4 = Livro(2, 'Perguntaram-me se acredito em Deus')

arvore_teste = BinaryTree()
arvore_teste.insert(livro1)
arvore_teste.insert(livro2)
arvore_teste.insert(livro3)
arvore_teste.insert(livro4)

print('\nResultado in-order')
in_order = arvore_teste.in_order_traverse()
for livro in in_order:
    print(livro)

print('\nResultado pre-order')
pre_order = arvore_teste.pre_order_traverse()
for livro in pre_order:
    print(livro)

print('\nResultado post-order')
post_order = arvore_teste.post_order_traverse()
for livro in post_order:
    print(livro)

# print(arvore_teste.root.livro)
# no = Node(livro1)
# print(no.livro.titulo)
