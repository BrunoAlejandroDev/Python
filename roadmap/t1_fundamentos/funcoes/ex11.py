
#* Validação de Senha (While): Crie uma função pedir_senha(). Ela deve usar input dentro de um while e só retornar True quando o usuário digitar "1234". Enquanto errar, ela printa "Senha incorreta".

def pedir_senha():
    while True:
        try:
            senha = input('Digite a senha: ')
            if senha == '1234':
                print('Senha correta.')
                break
            else:
                raise ValueError
        except ValueError:
            print('Senha incorreta. Digite apenas numeros')

pedir_senha()