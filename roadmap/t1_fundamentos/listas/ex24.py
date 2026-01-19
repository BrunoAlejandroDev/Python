
#* Filtro Manual: Crie uma função filtrar_maiores(lista_numeros, limite). Ela deve retornar uma nova lista contendo apenas os números que forem maiores que o limite.

def filtrar_maiores(lista_numeros, limite):
    lista_final = []

    for numero in lista_numeros:
        if numero > limite:
            lista_final.append(numero)
    
    return lista_final

lista = [12, 56, 48, 23, 8, 9, 3, 63, 159, 72, 93, 42, 81, 2, 31]

print(filtrar_maiores(lista, 70))