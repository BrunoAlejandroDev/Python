'''
Crie uma exceção personalizada chamada SaldoInsuficienteError. Em seguida, desenvolva uma função verificar_saldo(valor, saldo) que levanta essa exceção se o usuário tentar sacar um valor maior do que o saldo disponível.
'''

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f'Saldo insufuciente. SD')