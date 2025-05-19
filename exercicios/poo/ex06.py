'''
1. Transforme os atributos da classe Pessoa em "protegidos" (use _ antes dos nomes). Depois, implemente métodos get_idade() e set_idade(nova_idade) para controlar o acesso ao atributo idade.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao = 'Indefinido'):
        self._nome = nome
        self._idade = idade
        self.profissao = profissao
        
    def apresentar(self):
        return f'Ola, meu nome e {self.nome} e eu tenho {self.idade} anos. Minha profissao eh {self.profissao}'
    
    def aniversario(self):
        self._idade += 1
        return self._idade
    
    def get_idade(self):
        return f'{self._idade}'
    
    def set_idade(self, nova_idade):
        self.idade = nova_idade
        
pessoa1 = Pessoa('Bruno', 24, 'Programador')
print(pessoa1.get_idade())