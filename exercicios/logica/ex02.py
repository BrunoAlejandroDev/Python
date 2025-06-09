'''
Crie uma função chamada inverter_e_filtrar_pares que receba uma lista de números inteiros. A função deve retornar uma nova lista contendo apenas os números ímpares da lista original, mas em ordem invertida.
'''

def inverter_pares(lista_numeros):
    lista_impares = []
    lista_invertida = []
    
    for numero in lista_numeros:
        if numero % 2 != 0: # verifico se o numero eh impar
            lista_impares.append(numero)
            
    for numero in lista_impares[::-1]: # itero sobre a lista na ordem invertida
        lista_invertida.append(numero) # insiro os numeros na nova lista
        
    return lista_invertida
            
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(inverter_pares(lista))