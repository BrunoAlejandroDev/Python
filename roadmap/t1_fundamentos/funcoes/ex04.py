
#* Lógica Booleana: Crie uma função eh_positivo(numero) que retorne True se o número for estritamente maior que zero e False caso contrário.

def eh_positivo(numero):
    '''
    Recebe um numero e verifica se ele eh positivo

    Args:
        numero: valor numerico inteiro

    Returns:
        boolean: TRUE caso numero maior que zero. FALSE caso numero menor que zero
    '''

    if numero > 0:
        return True
    else:
        return False
    
#* Pedir numero ao usuario
while True:
    try:
        numero = int(input('Digite um numero: '))
        break

    except ValueError:
        print('Digite apenas valores numericos inteiros.')

#* chamar funcao e exibir valor
print(f'O numero {numero} eh positivo? {eh_positivo(numero)}')