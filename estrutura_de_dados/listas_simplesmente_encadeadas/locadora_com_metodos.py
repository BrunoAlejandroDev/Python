class Jogo:
    def __init__(self, id, nome, genero):
        self.id = id
        self.nome = nome
        self.genero = genero

    def __str__(self):
        return f'Detalhes do Jogo:\nId: {self.id}\nNome: {self.nome}\nGenero: {self.genero}'
    
    