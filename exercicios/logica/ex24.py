'''
Data: 19/06/25
Exercício: Validador de Senha Simples
Enunciado: Crie uma função chamada validar_senha que recebe uma string como argumento. A função deve retornar True se a senha atender a todos os seguintes critérios e False caso contrário:
Ter no mínimo 8 caracteres.
Conter pelo menos uma letra maiúscula.
Conter pelo menos um número.
Exemplo:
Entrada: validar_senha("Senha123")
Saída: True
Entrada: validar_senha("senhafraca")
Saída: False
'''

def validar_senha(senha):
    
    #* Verificar o tamanho da senha
    tamanho_senha = False
    if len(senha) >= 8:
        tamanho_senha = True
    
    #* normalizar senha
    senha_normalizada = senha.split()
    
    #* Se tamanho da senha for atendido
    if tamanho_senha:
        #* Flag para verificar letra maiuscula
        tem_letra_maiuscula = False
        tem_letra_minuscula = False
        
        #* Loop para iterar sobre cada letra da senha
        for palavra in senha_normalizada:
            for letra in palavra:
                if letra.isupper():
                    tem_letra_maiuscula = True
                if letra.lower():
                    tem_letra_minuscula = True
        
        #* Verificar se a senha tem letra maiuscula e minuscula para passar para a proxima verificaçao
        if tem_letra_maiuscula and tem_letra_minuscula:
            #* Flag para verificar numero
            tem_numero = False
            
            for palavra in senha_normalizada:
                for caractere in palavra:
                    if caractere.isdigit():
                        tem_numero = True
                        
            if tem_numero:
                return True
            else:
                return False       
        else:
            return False
    else:
        return False
    
print(validar_senha('Senhafraca'))