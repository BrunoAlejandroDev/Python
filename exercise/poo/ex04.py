'''
Crie uma classe Playlist que contenha uma lista de objetos Midia. Adicione métodos para adicionar e remover mídias, e um método para exibir as informações de todas as mídias na playlist.
'''

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