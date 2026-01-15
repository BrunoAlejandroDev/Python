
#* Condicional Simples: Crie uma função verificar_idade(idade) que retorne a string "Maior de idade" se idade >= 18, senão retorna "Menor de idade".

def verificar_idade(idade):
    '''
    Função que recebe um valor (idade) e retorna se maior ou menor de idade
    
    Args:
        idade: Int

    Returns: 
        String: Maior de idade ou Menor de idade
    '''

    if idade >= 18:
        return 'Maior de idade'
    else:
        return 'Menor de idade'
    
idade = 24

print(verificar_idade(idade))