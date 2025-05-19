'''
4. Acrescente um novo atributo profissão à classe, mas faça com que ele tenha um valor padrão "Indefinido" caso não seja informado na criação do objeto.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao = 'Indefinido'):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def apresentar(self):
        return f'Ola, meu nome e {self.nome} e eu tenho {self.idade} anos. Minha profissao eh {self.profissao}'
    
pessoa1 = Pessoa('Bruno', 24, 'Programador')
pessoa2 = Pessoa('Alicia', 22)

print(pessoa1.apresentar())
print(pessoa2.apresentar())