'''
Crie uma classe chamada Midia com atributos titulo e duracao. Adicione um método exibir_informacoes que imprime o título e a duração da mídia.
'''
class Midia:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}')