
#* Reimplementando Matemática: Sem usar o operador **, crie uma função elevar_potencia(base, expoente) que use um loop for ou while para calcular o resultado.

def elevar_potencia(base, potencia):
    '''
    Função que recebe dois parâmetros (base e potencia) e retorna a base elevada pela potencia
    
    :param base: valor numerico inteiro
    :param potencia: valor numerico inteiro

    :returns Int: valor final da base elavada pela potencia
    '''
    valor_final = 1
    for i in range(potencia):
        valor_final *= base

    return valor_final

print(elevar_potencia(2, 5))