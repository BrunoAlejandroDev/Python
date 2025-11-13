'''
Exercício: Validador de Senha Simples
Enunciado: Crie uma função chamada validar_senha que recebe uma string como parâmetro. A função deve retornar True se a senha atender a todos os seguintes critérios e False caso contrário:
Ter no mínimo 8 caracteres.
Conter pelo menos uma letra maiúscula.
Conter pelo menos um número.
Exemplo 1:
Entrada: validar_senha("Senha123")
Saída: True
Exemplo 2:
Entrada: validar_senha("senhafraca")
Saída: False
Dicas:
Você pode iterar sobre cada caractere da string e usar métodos como .isupper() e .isdigit().
Pense em usar variáveis "flags" (booleanas) para rastrear se cada critério foi atendido.
'''

def validar_senha(senha):
    senha_separada = []
    for letra in senha:
        senha_separada.append(letra)

    letras_maiusculas = 0
    digitos_numericos = 0

    if len(senha) >= 8:
        for letra in senha_separada:
            if letra.isupper():
                letras_maiusculas += 1
        if letras_maiusculas >= 1:
            for letra in senha_separada:
                if letra.isdigit():
                    digitos_numericos += 1
            if digitos_numericos >= 1:
                print('Senha valida')
                return True
            else:
                print('A senha precisa ter pelo menos uma letra maiuscula e um numero')
                return False
        else:
            print('A senha precisa ter pelo menos uma letra maiuscula e um numero')
            return False
    else:
        print('A senha precisa ter no minimo 8 caracteres')
        return False

senha = 'senhafraca'
print(validar_senha(senha))