
#* Manipulação Básica (Append): Crie uma função gerar_sequencia(n) que receba um número inteiro n e retorne uma lista contendo os números de 0 até n (sem usar range ou list comprehension, use while ou for e .append()).

numero = 5

def gerar_sequencia(n):
    lista = []
    contador = 0

    while contador <= n:
        lista.append(contador)
        contador += 1

    return lista

print(gerar_sequencia(numero))