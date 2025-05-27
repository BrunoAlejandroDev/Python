class Node:
    def __init__(self, nome = None, proximo = None):
        self.nome = nome
        self.proximo = proximo
        
class ListaEncadeada:
    def __init__(self):
        self.head = None
        
    def imprimir_lista(self):
        if self.head is None: #* verificar se a cabeça esta vazia
            print('Lista esta vazia')
            return

        #* Iterar pela lista e imprimir os valores
        pos_atual = self.head # variavel de posicao inicial
        lista_elementos = '' # "lista" para salvar cada elemento e exibir
        while pos_atual:
            lista_elementos += str(pos_atual.nome) + ' --> ' if pos_atual.proximo else str(pos_atual.nome)
            pos_atual = pos_atual.proximo
        print(lista_elementos)
        
    def adicionar_no_inicio(self, nome):
        elemento = Node(nome, self.head)
        self.head = elemento
        
    def adicionar_no_final(self, nome):
        #* verificar se a cabeça esta vazia
        if self.head is None: 
            elemento = Node(nome, self.head) # novo elemento inserido no inicio
            self.head = elemento
            return
            
        pos_atual = self.head
        while pos_atual.proximo:
            pos_atual = pos_atual.proximo # iterar por toda a lista
        
        pos_atual.proximo = Node(nome, None) # o ultimo elemento (none) vai receber o novo elemento
            
    def tamanho_lista(self):
        pos_atual = self.head
        contador = 0
        
        while pos_atual:
            contador += 1
            pos_atual = pos_atual.proximo
        
        return contador
    
if __name__ == '__main__':
    lista_encadeada = ListaEncadeada()
    lista_encadeada.imprimir_lista()
    lista_encadeada.adicionar_no_inicio('banana')
    lista_encadeada.imprimir_lista()
    lista_encadeada.adicionar_no_final('melao')
    lista_encadeada.imprimir_lista()
    print(lista_encadeada.tamanho_lista())