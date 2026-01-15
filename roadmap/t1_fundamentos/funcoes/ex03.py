
#* Conversão de Tempo: Crie uma função minutos_para_segundos(minutos) que receba um valor em minutos e retorne o total em segundos.

def minutos_para_segundos(minutos):
    '''
    Converte um valor numerico em minutos e retorna o valor em segundos

    Args:
        minutos: valor numerico

    Returns:
        int: valor em segundos 
    '''
    
    return minutos * 60

#* Pedir valor ao usuario
minutos = int(input('Digite o valor em minutos: '))

#* Chamar funcao e exibir retorno
print(minutos_para_segundos(minutos))