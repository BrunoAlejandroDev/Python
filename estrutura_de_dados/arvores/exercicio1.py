
#* Parte 1 - Construção do no da arvore
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None #* referencia para o filho da esquerda
        self.direita = None #* referencia para o filho da direita
    
#* Parte 2 - Criação manual dos nós da arvore e conexão dos nós com a raiz
no_raiz = Node(11)
no_esquerda = Node(9)
no_direita = Node(15)

no_raiz.esquerda = no_esquerda
no_raiz.direita = no_direita

#* Parte 3 - Criar a arvore binaria
class BinaryTree:
    def __init__(self):
        self.root = None #* definição inicial da arvore, logo sua raiz é vazia
        
    def insert(self, valor):
        #* 1: verificar se a arvore esta vazia
        if self.root is None:
           novo_no = Node(valor) #* cria o valor para o novo no raiz
           self.root = novo_no #* define a raiz com o novo valor
           print('valor inserido na raiz')
        else:
            #* 2: caso a arvore não esteja vazia
            self._insert(self.root, valor) #* chama a função de recursao
           
    def _insert(self, no_atual, valor):
        print('entrei na recursao')
        
        #* Verificar se o valor atual é menor que a raiz. Se sim, inserção a esquerda
        if valor < no_atual.valor: 
            if no_atual.esquerda is None: #* verifica se o primeiro no da esquerda esta vazio
                print('valor inserido no nó da esquerda')
                novo_no = Node(valor)
                no_atual.esquerda = novo_no #* insere o valor no nó da esquerda
            else: #* caso ja tenha um no na esquerda, acessa esse no e começa a inserçao a partir dele
                self._insert(no_atual.esquerda, valor)
                
        #* Caso valor atual seja maior que a raiz
        else:
            if no_atual.direita is None: #* verifica se o primeiro nó da direita esta vazio
                print('valor inserido no nó da direita')
                novo_no = Node(valor)
                no_atual.direita = novo_no #* insere o valor no nó da direita
            else: #* caso ja tenha um no na direita, acessa esse nó e começa a inserçao a partir dele
                self._insert(no_atual.direita, valor)
                
    #* Passo 4 - Metodo in-order
    def _in_order_traverse(self, no_atual, lista_resultado):
        #* Caso base -> nó não existe
        if no_atual is None:
            return
        
        #* Passo 1 -> ir para a esquerda
        self._in_order_traverse(no_atual.esquerda, lista_resultado)
        
        #* Passo 2 -> processar o nó atual
        lista_resultado.append(no_atual.valor)
        
        #* Passo 3 -> ir para  direita
        self._in_order_traverse(no_atual.direita, lista_resultado)
        
    def in_order_traverse(self):
        lista_valores = []
        self._in_order_traverse(self.root, lista_valores)
        return lista_valores
    
    #* Passo 5 - Metodo pre-order
    def _pre_order_traverse(self, no_atual, lista_valores):
        #* Caso base: verificar se o no atual é none
        if no_atual is None:
            return

        #* Passo 1: ir para a raiz e imprimir o valor
        lista_valores.append(no_atual.valor)
        
        #* Passo 2: ir para a esquerda
        self._pre_order_traverse(no_atual.esquerda, lista_valores)
        
        #* Passo 3: ir para a direita
        self._pre_order_traverse(no_atual.direita, lista_valores)
        
    def pre_order_traverse(self):
        lista_valores = []
        self._pre_order_traverse(self.root, lista_valores)
        return lista_valores
                
    #TODO escrever o metodo post order
    #* Passo 6 - Metodo post order
    
arvore = BinaryTree()
arvore.insert(11)
print()
arvore.insert(9)
print()
arvore.insert(12)
print()
arvore.insert(8)
print()
arvore.insert(14)

# print(arvore.root.esquerda.valor)

resultado_ordenado = arvore.in_order_traverse()
print(f'resultado do percurso (in-order): {resultado_ordenado}')

resultado_ordenado = arvore.pre_order_traverse()
print(f'resultado do percurso (pre-order): {resultado_ordenado}')