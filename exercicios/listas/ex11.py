'''
Exercício 4: Verificando a Existência de um Elemento

Descrição: Crie uma função chamada contem_numero que receba uma lista de números e um número como argumentos. A função deve retornar True se o número estiver presente na lista e False caso contrário.
Exemplo: contem_numero([1, 2, 3, 4, 5], 3) deve retornar True.
Exemplo: contem_numero([1, 2, 3, 4, 5], 6) deve retornar False.
Restrição: Tente implementar a lógica de busca usando um laço for e uma estrutura condicional, sem usar o operador in diretamente na verificação principal (você pode usá-lo para comparar, mas a lógica de varredura deve ser manual).
'''

def contem_numero(lista_numeros, numero):
    for num in lista_numeros:
        if num == numero:
            return True
    return False
        
lista_numeros = [2, 4, 6]
print(contem_numero(lista_numeros, 1))
print(contem_numero(lista_numeros, 3))
print(contem_numero(lista_numeros, 6))