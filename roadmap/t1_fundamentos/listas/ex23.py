
#* Soma de Lista: Crie uma função somar_lista(lista_numeros) que percorra a lista com um for e retorne a soma de todos os elementos.

def somar_lista(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    
    return soma

numeros = [45, 90, 81, 1, 59, 10, 3]
print(somar_lista(numeros))