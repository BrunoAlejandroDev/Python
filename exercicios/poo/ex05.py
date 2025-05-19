'''
5. Implemente um método aniversario() que incremente a idade em 1 ano e retorne a nova idade.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao = 'Indefinido'):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def apresentar(self):
        return f'Ola, meu nome e {self.nome} e eu tenho {self.idade} anos. Minha profissao eh {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
        return self.idade
    
pessoa1 = Pessoa('Bruno', 24, 'programador')
print(pessoa1.apresentar())
pessoa1.aniversario()
print(pessoa1.apresentar())