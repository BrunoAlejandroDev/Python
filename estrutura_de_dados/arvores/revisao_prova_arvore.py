''''
EXERCICIO ARVORE BINARIA DE BUSCA - LIVROS
'''

class Livro:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        
    def __str__(self):
        return f'{self.codigo} | {self.titulo}'
    
    