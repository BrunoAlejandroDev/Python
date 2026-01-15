
#* Manipulação de String: Crie uma função gritar(texto) que receba uma string e a retorne em caixa alta (Use .upper()).

def gritar(texto):
    '''
    Funcao que recebe um texto e retorna ele em caixa alta
    
    Args:
        texto: String

    Returns:
        String: Texto em caixa alta
    '''

    texto_caixa_alta = texto.upper()
    return texto_caixa_alta

print(gritar('bruno'))