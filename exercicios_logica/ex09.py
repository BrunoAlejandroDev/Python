'''
Exercício: Encontrando o "Elemento Intruso"
Enunciado: Crie uma função que recebe uma lista de números. A lista contém vários números que seguem um padrão, exceto por um único "elemento intruso". O padrão é que todos os números são pares ou todos são ímpares, com exceção de um. A função deve identificar e retornar esse elemento intruso.
Exemplo 1:
Entrada: [2, 4, 6, 9, 10, 12]
Saída: 9
Exemplo 2:
Entrada: [1, 3, 7, 5, 21, 8]
Saída: 8
Dicas:
Uma boa estratégia é analisar os três primeiros elementos. O padrão da lista (par ou ímpar) será definido pela maioria entre eles.
Após descobrir qual é o padrão (se a lista é majoritariamente de pares ou ímpares), percorra a lista para encontrar o número que não se encaixa.
'''

def encontrar_elemento_intruso(lista_numeros):
    verificar_tres_primeiros_pares = False
    verificar_tres_primeiros_impares = False
    toda_lista_par = False
    toda_lista_impar = False
    tres_primeiros_numeros = lista_numeros[:3]

    print('Verificando os tres primeiros numeros')
    for numero in tres_primeiros_numeros:
        if numero % 2 != 0:
            print(f'-- um dos tres primeiros numeros eh impar: {numero}')
            verificar_tres_primeiros_pares = False
            break
        elif numero % 2 != 1:
            print(f'-- um dos tres primeiros numeros eh par: {numero}')
            verificar_tres_primeiros_impares = False
            break

    print('Verificando todos os numeros da lista')
    if verificar_tres_primeiros_pares:
        for numero in lista_numeros:
            if numero % 2 != 0:
                print(f'-- elemento intruso encontrado: {numero}')
                toda_lista_par = False
                break
    
    elif verificar_tres_primeiros_impares:
        for numero in lista_numeros:
            if numero % 2 != 1:
                print(f'-- elemento intruso encontrado: {numero}')
                toda_lista_impar = False
                break

    if toda_lista_par:
        print('Todos os numeros da lista sao pares')
    else:
        print('A lista contem um elemento impar')

    if toda_lista_impar:
        print('Todos os numeros da lista sao impares')
    else:
        print('A lista contem um elemento par')

numeros = [1, 3, 7, 5, 21, 8]
encontrar_elemento_intruso(numeros)