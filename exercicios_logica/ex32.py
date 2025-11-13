'''
Data: 18/07/25
Exercício 1: Validador de Senha Simples

Enunciado: Crie uma função chamada validar_senha que recebe uma string como argumento. A função deve verificar se a senha atende a um único critério: ter no mínimo 8 caracteres. Se a senha for válida, a função deve retornar True; caso contrário, deve retornar False.

Exemplo:
Entrada: 'senha123'
Saída: True

Entrada: 'abc'
Saída: False

Habilidades desenvolvidas: Funções, estruturas condicionais, operadores lógicos, manipulação de strings (len).
'''

def validar_senha(senha:str):
    
    #* Normalizar a senha
    senha_normalizada = senha.lower()

    #* Verificar tamanho da senha
    tamanho_senha = len(senha_normalizada)

    #* Verificar se a senha possui o tamanho minimo
    if tamanho_senha >= 8:
        return True
    else:
        return False


senha = 'abc'
print(validar_senha(senha))