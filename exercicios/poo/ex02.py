'''
2. Instancie dois objetos da classe Pessoa com valores diferentes e chame o método apresentar() para cada um.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f'Ola, meu nome e {self.nome} e eu tenho {self.idade} anos'
    
#* Instancias da Classe Pessoa
pessoa1 = Pessoa('Bruno', 24)
pessoa2 = Pessoa('Alicia', 22)

print(pessoa1.apresentar())
print(pessoa2.apresentar())