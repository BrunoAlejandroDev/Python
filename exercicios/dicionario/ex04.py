'''
Atualize o autor para "Ernest Cline" - feito
Adicione o campo "ano" com valor 2044 - feito
Acesse a chave "editora" usando .get() com valor padrão "Desconhecida"
'''

livro = {'titulo' : 'Solaris', 'autor' : 'Stanilaw Lem'}
print(livro)

#* item a
livro.update({'autor' : 'Ernest Cline'})
print(livro)

#* item b
livro.update({'ano' : 2044})
print(livro)

#* item c
editora = livro.get('editora', 'Desconhecida')
print(editora)