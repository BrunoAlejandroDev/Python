'''
Implemente o método especial __str__ para que print(pessoa) retorne a mesma string que o método apresentar() fornecia antes.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao = 'Indefinido'):
        self._nome = nome
        self._idade = idade
        self.profissao = profissao
    
    def apresentar(self):
        return f'Ola, meu nome e {self._nome} e eu tenho {self._idade} anos. Minha profissao eh {self.profissao}'

    def __str__(self):
        return self.apresentar()
    
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

pessoa = Pessoa('Bruno', 24, 'Estagiario')
print(pessoa)