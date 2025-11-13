'''
Exercício: Validador de Senha Simples
Enunciado: Crie uma função chamada validar_senha que recebe uma string como argumento. A função deve retornar True se a senha for válida e False caso contrário. Uma senha válida deve atender a todos os seguintes critérios:
Ter no mínimo 8 caracteres.
Conter pelo menos uma letra maiúscula.
Conter pelo menos um número.
'''

def validar_senha(nome, senha):
    #* Formatar senha
    senha_formatada = []
    for letra in senha:
        senha_formatada.append(letra)
    
    #* Flags booleanas
    tamanho_minimo_senha = False
    tem_letra_maiuscula = False
    tem_caractere_numerico = False
    
    #* Verificar numero de caracteres
    if len(senha) >= 8:
        tamanho_minimo_senha = True
    else:
        tamanho_minimo_senha = False

    #* Verificar se tem letra maiuscula
    contador_maiusculas = 0
    if tamanho_minimo_senha: # se o tamanho minimo de caracteres tiver sido atendido
        for letra in senha_formatada:
            if letra.upper():
                contador_maiusculas += 1
                
    if contador_maiusculas >= 1: # se encontrou pelo menos uma letra maiuscula
        tem_letra_maiuscula = True
    else:
        tem_letra_maiuscula = False
    
    #* Verificar se tem caractere numerico
    caractere_numerico = 0
    if tem_letra_maiuscula: # se tiver encontrado ao menos uma letra maiuscula
        for letra in senha_formatada:
            if letra.isdigit():
                caractere_numerico += 1

    if caractere_numerico >= 1: # se encontrou pelo menos um numero
        tem_caractere_numerico = True
    else:
        tem_caractere_numerico = False
    
    #* Retorno caso a senha seja valida
    if tem_caractere_numerico and tem_letra_maiuscula and tamanho_minimo_senha:
        return f'Seja bem vindo, {nome}'
    else:
        return 'Error: A senha deve possui pelo menos 8 caracteres, uma letra maiuscula e um numero'
    
print('=== Faça seu login para continuar ===')
nome = input('Digite seu nome de usuario: ')
senha = input('Digite sua senha: ')
validar_acesso = validar_senha(nome, senha)
print(validar_acesso)