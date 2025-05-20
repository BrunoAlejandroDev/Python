'''
Agora transforme o atributo profissão em privado (__profissao) e adicione métodos de acesso (getter e setter). Faça com que o setter só aceite valores que sejam strings com pelo menos 2 caracteres.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self.__profissao = profissao

    def fazer_aniversario(self):
        self._idade += 1
        return self._idade
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError('A idade nao pode ser menor que zero')
        else:
            self._idade = nova_idade

    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self, profissao):
        if not isinstance(profissao, str) or len(profissao) < 2:
            raise ValueError('Profissao invalida: forneca uma string com ao menos 2 caracteres.')
        else:
            self.__profissao = profissao

    def __str__(self):
        return f'Ola, meu nome eh {self._nome}. Tenho {self.idade} anos e sou {self.profissao}'