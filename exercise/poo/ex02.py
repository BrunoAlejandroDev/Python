'''
Crie uma subclasse Video que herda de Midia e adiciona um atributo resolucao. Adicione um método exibir_informacoes que imprime o título, a duração e a resolução do vídeo.
'''

class Midia:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}')

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def exibir_informacoes(self):
        return super().exibir_informacoes()