'''
1. Transforme os atributos da classe Pessoa em "protegidos" (use _ antes dos nomes). Depois, implemente métodos get_idade() e set_idade(nova_idade) para controlar o acesso ao atributo idade.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao = 'Indefinido'):
        self._nome = nome
        self._idade = idade
        self.profissao = profissao
        
    def apresentar(self):
        return f'Ola, meu nome e {self._nome} e eu tenho {self._idade} anos. Minha profissao eh {self.profissao}'
    
    def aniversario(self):
        self._idade += 1
        return self._idade
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            raise ValueError('A idade deve ser um numero inteiro positivo')
        
pessoa1 = Pessoa('Bruno', 24, 'Programador')
print(pessoa1.get_idade())
pessoa1.set_idade(25)
print(pessoa1.get_idade())