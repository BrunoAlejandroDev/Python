'''
Crie uma subclasse Foto que herda de Midia e adiciona atributos resolucao e formato. Adicione um método exibir_informacoes que imprime o título, a duração, a resolução e o formato da foto.
'''

class Foto(Midia):
    def __init__(self, titulo, duracao, resolucao, formato):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
        self.formato = formato

    def exibir_informacoes(self):
         print(f'Titulo: {self.titulo}\nDuracao: {self.duracao}\nResolucao: {self.resolucao}\nFormato: {self.formato}')
         