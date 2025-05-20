'''
Questão 11 — Herança Básica
    Crie uma classe Animal com um método falar() que retorna a string "Som de animal". Em seguida, crie duas subclasses:
        Cachorro, que sobrescreve falar() retornando "Au au!"
        Gato, que sobrescreve falar() retornando "Miau!"
        Crie instâncias de ambas e chame falar() para verificar o comportamento.
'''

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return 'som de animal'
    
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return 'Au Au!'
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return 'Miau!'
    
animal = Animal('animal')
print(animal.falar())

cachorro = Cachorro('Laika')
print(cachorro.falar())

gato = Gato('Anita')
print(gato.falar())