'''
Crie uma classe Usuario com atributos nome, id e playlist (que será uma instância da classe Playlist). Adicione métodos para adicionar 
e remover mídias da playlist do usuário, e um método para exibir a playlist do usuário.
'''

class Midia:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}\n')

midia1 = Midia('This is me trying', 3)
# midia1.exibir_informacoes()

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}\nResolucao: {self.resolucao}\n')

video1 = Video('Machine learning com python', 12, 1080)
# video1.exibir_informacoes()
    
class Audio(Midia):
    def __init__(self, titulo, duracao, formato):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}\nFormato: {self.formato}\n')

class Playlist():
    def __init__(self):
        self.midias = [] # criando a lista vazia para armazenas as midias
    
    def adicionar_midias(self, midia):
        self.midias.append(midia)

    def remover_midia(self, midia):
        if midia in self.midias:
            self.midias.remove(midia)
    
    def exibir_informacoes(self):
        for midia in self.midias:
            midia.exibir_informacoes()

class Usuario():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.playlist = Playlist()
        self.midias_usuario = []

    def adicionar_midia_usuario(self, midia):
        self.playlist.adicionar_midias(midia)

    def remover_midia_usuario(self, midia):
        if midia in self.midias_usuario:
            self.playlist.remover_midia(midia)

    def exibir_informacoes(self):
        print(f'Playlist do usuario {self.nome}')
        self.playlist.exibir_informacoes()

usuario1 = Usuario('Bruno', 2)
midia_usuario = Midia('loja do mestre andre', 3)
usuario1.adicionar_midia_usuario(midia_usuario)
usuario1.exibir_informacoes()