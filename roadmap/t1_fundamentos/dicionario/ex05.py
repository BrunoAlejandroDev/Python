'''
Crie um dicionário perfil com chaves: nome, idade, cidade.

Altere o valor de "cidade" para outra cidade.
Adicione uma nova chave chamada "email".
'''

perfil = {
    'nome' : 'nome',
    'idade' : 'idade',
    'cidade' : 'cidade',
}
print(perfil)

#* item a 
perfil.update({'cidade' : 'Fortaleza'})
print(perfil)

#* item b
perfil.update({'email' : 'email'})
print(perfil)