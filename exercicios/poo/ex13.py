'''
Questão 13 — Polimorfismo com Sobrescrita
    Crie uma função chamada apresentar_animal(animal) que recebe um objeto Animal e chama o método falar() e apresentar().
    Crie uma lista com um Cachorro, um Gato e um Animal genérico. Passe cada um para a função apresentar_animal.
    Explique o comportamento observado.
'''

class Animal:
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

def apresentar_animal(Animal):
    print(Animal.falar())
    print(Animal.apresentar())

cachorro = Cachorro('Mel', 7)
gato = Gato('Nina', 4)
generico = Animal('samuel', 10)

lista_animais = [
    cachorro,
    gato,
    generico
]

for animal in lista_animais:
    apresentar_animal(animal)