class Alimento:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.price = preco
        self.proximo = None # este atributo apenas aponta para algo na memoria, como um endereco
    def __str__(self):
        return f'ID: {self.id}\nNome: {self.nome}\nPreco: {self.preco}'
    
class Supermercado:
    def __init__(self):
        self.head = None
        self.inicialiar_supermercado()
        self.adicionar_alimento()
        self.remover_alimento()

        #* Criar Funcao  Inicializar
        def inicializar_supermercado(self):
            alimentos_iniciais = [
                ('1', 'Arroz', 12.5),
                ('2', 'Feijao', 10.7),
                ('3', 'Macarrao', 5.5),
            ]

            ultimo_adicionado = None
            for id, nome, preco in alimentos_iniciais:
                novo_alimento = Alimento(id, nome, preco)
                if self.head == None:
                    self.head = novo_alimento
                else:
                    ultimo_adicionado.proximo = novo_alimento
                ultimo_adicionado = novo_alimento

        def adicionar_alimento(self, id, nome, preco):
            novo_alimento = Alimento(id, nome, preco)

            if not self.head: # verifica se o ponteiro do head esta vazio -> equivalente a if self.head == None
                self.head = novo_alimento # define a primeira posicao da lista
                return
            
            alimento_atual = self.head
            while alimento_atual.proximo: # enquanto o proximo do meu alimento atual existir, percorra o loop
                alimento_atual = alimento_atual.proximo # o loop while vai percorrer toda a lista ate encontrar o alimento final, cujo proximo eh vazio
            alimento_atual = novo_alimento

        def remover_alimento(self, id):
            atual = self.head # essa variavel sera usada para percorrer a lista a partir da posicao inicial
            anterior = None # essa variavel sera utilizada para acessar a posicao anterior ao elemento atual e eh inicializada como vazia pois o elemento inicial eh o primeiro

            while atual and atual.id != id: # percorre a lista encadeada ate encontrar o elemento desejado ou ate o fim da lista
                anterior = atual # guarda o atual para manter a referencia
                atual = anterior.proximo
            if atual is None:
                print('Alimento nao encontrado')
                return
            if anterior is None:
                self.head = atual.proximo
            else:
                anterior.proximo = atual.proximo
            print('Alimento removido.')