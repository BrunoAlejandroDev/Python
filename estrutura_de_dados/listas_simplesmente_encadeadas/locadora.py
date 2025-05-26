class Jogo:
    def __init__(self, id, nome, genero):
        self.id = id
        self.nome = nome
        self.genero = genero
        self.proximo = None #* variavel que serve como ponteiro
        
    def __str__(self):
        return f'Id do jogo: {self.id}\nNome do jogo: {self.nome}\nGenero do jogo: {self.genero}\n======'

class Locadora:
    def __init__(self):
        self.head = None # inicializando a posicao inical como none
        self.inicializar_locadora()
        self.adicionar_jogo
        self.remover_jogo
        self.listar_jogos
        self.exibir_jogos
        
    def inicializar_locadora(self):
        jogos_disponiveis = [
            ('01', 'The Witcher', 'RPG'),
            ('02', 'GTA', 'Multiplos'),
            ('03', 'Fifa', 'Esportes'),
            ('04', 'The Last of Us', 'Pos-apocalipse'),
            ('05', 'Detroit: become human', 'Investigacao')
        ]
        
        anterior = None
        for id, nome, genero in jogos_disponiveis:
            novo_jogo = Jogo(id, nome, genero)
            if self.head == None: #* verifica se a posicao inicial da lista esta vazia
                self.head = novo_jogo
            else:
                anterior.proximo = novo_jogo #* caso contrario, inicializa a proxima posicao com o novo jogo
            anterior = novo_jogo #* anterior passa a apontar para o proximo jogo
            
    def adicionar_jogo(self, id, nome, genero):
        novo_jogo = Jogo(id, nome, genero)
        
        #* primeira verificacao: checar se a posicao inicial esta ou nao vazia, caso nao, inicializar um novo elemento nela
        if not self.head:
            self.head = novo_jogo
            return
        
        #* segunda verificacao: a lista nao esta vazia e eh necessario percorre-la para alcançar a ultima posicao
        atual = self.head # inicializar uma variavel que aponte para a cabeça
        while atual.proximo: # enquanto houver elemento na lista, faça algo
            atual = atual.proximo # muda o ponteiro do atual para o elemento seguinte ate chegar ao final da lista
        atual.proximo = novo_jogo # cria uma nova posicao depois do ultimo elemento da lista
        
    def remover_jogo(self, id):
        atual = self.head
        anterior = None
        
        #* loop para percorrer toda a lista de jogos
        while atual and atual.id != id:
            anterior = atual
            atual = atual.proximo
        
        #* 1 verificacao: lista percorrida e elemento nao encontrado
        if atual is None:
            print('Jogo nao encontrado')
            return

        #* segunda verificacao: o elemento buscado era o primeiro da lista
        if anterior is None:
            self.head = atual.proximo # atualiza o elemento inicial da lista
            
        #* terceira verificacao: elemento encontrado e desconecta-lo da lista
        else:
            anterior.proximo = atual.proximo
            
        print(f'Elemento de id {id} encontrado e removido com sucesso!')
        
    def listar_jogos(self):
        lista_jogos = []
        atual = self.head
        
        while atual:
            lista_jogos.append(atual)
            atual = atual.proximo
        return lista_jogos
    
    def exibir_jogos(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo
            
jogo_locadora = Locadora()
print(jogo_locadora.exibir_jogos())