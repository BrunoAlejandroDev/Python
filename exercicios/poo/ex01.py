'''
1. Crie uma classe chamada Pessoa que possua os atributos:
    nome (string)
    idade (int)
    E um método chamado apresentar() que imprime:
        "Olá, meu nome é <nome> e tenho <idade> anos."
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f'Ola, meu nome e {self.nome} e eu tenho {self.idade} anos'
    
#* Criar Instancia da Classe Pessoa
pessoa1 = Pessoa('Bruno', 24)
print(pessoa1.apresentar())