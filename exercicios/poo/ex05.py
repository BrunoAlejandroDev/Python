'''
Crie um método na classe Playlist que percorra a lista de mídias e chame o método exibir_informacoes para cada objeto, demonstrando polimorfismo.
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

playlist1 = Playlist()
playlist1.adicionar_midias(midia1)
playlist1.adicionar_midias(video1)
playlist1.adicionar_midias(audio1)
playlist1.exibir_informacoes()