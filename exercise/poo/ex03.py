'''
Crie uma subclasse Audio que herda de Midia e adiciona um atributo formato. Adicione um método exibir_informacoes que imprime o título, a duração e o formato do áudio.
'''

class Midia:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}\n')

midia1 = Midia('This is me trying', 3)
# midia1.exibir_informacoes()
    
class Audio(Midia):
    def __init__(self, titulo, duracao, formato):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}\nFormato: {self.formato}\n')

audio1 = Audio('blablabla', 5, 'MP4')
audio1.exibir_informacoes()