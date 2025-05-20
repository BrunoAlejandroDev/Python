'''
Questão 12 — Reutilização com super()
    Altere a classe Animal para receber nome e idade no construtor. Faça com que as subclasses Cachorro e Gato reutilizem o construtor da superclasse usando super().
    Adicione um método apresentar() em Animal que imprime Olá, eu sou {nome} e tenho {idade} anos. Teste nas subclasses.
'''

class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return 'som de animal'
    
    def apresentar(self):
        return f'Ola, eu sou {self.nome} e eu tenho {self.idade} anos.'
    
    def __str__(self):
        return self.apresentar()

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return 'Au Au!'
    
class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return 'Miau!'
    
animal = Animal('generico', 5)
cachorro = Cachorro('bob', 7)
gato = Gato('Claudinho', 3)

print(animal.apresentar())
print(cachorro.apresentar())
print(gato.apresentar())