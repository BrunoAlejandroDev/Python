'''
Tente acessar uma chave que não existe diretamente (ex: perfil["telefone"]) e depois usando .get().
Observe a diferença de comportamento.
'''

perfil = {
    'nome' : 'nome',
    'idade' : 'idade',
    'cidade' : 'cidade',
}

# print(perfil['telefone'])
print(perfil.get('telefone'))