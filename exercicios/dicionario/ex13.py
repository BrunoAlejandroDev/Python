'''
Crie um dicionário chamado perfil_usuario. Adicione as seguintes chaves e valores:

'nome': "Carlos"
'idade': 32
'cidade': "São Paulo"
'profissao': "Engenheiro"
Depois, realize as seguintes ações:

Imprima o nome e a profissão do usuário.
Atualize a idade do usuário para 33.
Adicione uma nova chave 'hobbies' com uma lista de dois hobbies de sua escolha (ex: ['ler', 'correr']).
Remova a chave 'cidade' do dicionário.
Imprima o dicionário final.
'''

perfil_usuario = {
    'nome' : 'Carlos',
    'idade': 32,
    'cidade' : 'Sao Paulo',
    'profissao' : 'Engenheiro'
}

#* Imprimir informacoes
print('Original:')
def imprimir_informações():
    print('=== Dados ===')
    print(perfil_usuario)
    print()
imprimir_informações()

#* Atualizar idade
print('Idade atualizada:')
perfil_usuario['idade'] = 33
imprimir_informações()

#* Adicionar uma nova chave
perfil_usuario.update({'Hobbies' : ['Ler', 'Correr']})
print('Adicao de uma nova chave:')
imprimir_informações()

if 'cidade' in perfil_usuario:
    perfil_usuario.pop('cidade')
print('Remocao da chave cidade:')
imprimir_informações()