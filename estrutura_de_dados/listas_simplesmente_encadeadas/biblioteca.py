class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.proximo = None # variavel para apontar para o proximo livro da lista

    def __str__(self):
        status = 'disponivel' if self.disponivel else 'emprestado'
        return f'Livro:\nTitulo: {self.titulo}\nAutor: {self.autor}\nStatus: {status}'
    
    def emprestrar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.head = None
        self.inicializar_biblioteca()
        self.exibir_livros_disponiveis()
        self.emprestar_livro()

    def inicializar_biblioteca(self):
        livros_iniciais = [
            ('Solaris', 'Stanislaw lem', True),
            ('A natureza da mordida', 'Carla Madeira', False),
            ('Jogador Numero 1', 'Ernest Cline', False),
        ]

        ultimo_livro_adicionado = None
        for nome, autor, status in livros_iniciais:
            novo_livro = Livro(nome, autor, status)

            if self.head is None:
                self.head = novo_livro
            else:
                ultimo_livro_adicionado.proximo = novo_livro
            ultimo_livro_adicionado = novo_livro

    def exibir_livros_disponiveis(self):
        livro_atual = self.head # comeca no primeiro livro da lista encadeada
        while livro_atual: # percorre a lista de livros enquanto estiver livros disponiveis
            if livro_atual.status == True: # verifica a disponibilidade
                print(livro_atual)
            livro_atual = livro_atual.proximo

    def emprestar_livro(self, titulo):
        livro_atual = self.head # variavel para inicializar o livro atual como o primeiro da lista
        while livro_atual:
            if livro_atual.titulo == titulo: # verifica se o titulo passado eh o mesmo do livro atual
                if livro_atual.status:
                    livro_atual.status = False  
                    print(f'Livro: {titulo} emprestado com sucesso.')
                else:
                    print(f'Livro: {titulo} nao esta disponivel')
                return
            livro_atual = livro_atual.proximo # atualizar o valor da variavel livro atual para a proxima referencia
        print(f'Livro: {titulo} nao esta na biblioteca.')