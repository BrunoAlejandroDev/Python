'''
Questão 14 — Herança Múltipla
    Crie duas classes:
    Voador, com o método voar() que retorna "Voando alto!"
    Nadador, com o método nadar() que retorna "Nadando rápido!"
    Depois, crie uma classe Pato que herda de Animal, Voador e Nadador.
    Reutilize o construtor de Animal com super()
    Crie um método habilidades() que chama voar() e nadar()
    Teste a instância de Pato para verificar se ela fala, apresenta-se, voa e nada.
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
    
class Voador():
    def __init__(self):
        pass

    def voar(self):
        return 'Voando alto!'
    
class Nadador():
    def __init__(self):
        pass

    def nadar(self):
        return 'Nadando rapido'