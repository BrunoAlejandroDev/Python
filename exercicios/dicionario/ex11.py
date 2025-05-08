'''
Crie um dicionário com 3 produtos e seus preços.
a. Imprima cada par como: "Produto: [nome], Preço: [valor]"
b. Liste todas as chaves usando for chave in dict.
'''

estoque = {
    'placa de video' : 2000,
    'headset gamer' : 350,
    'teclado mecanico' : 300
}

#* item a:
for produto, preco in estoque.items():
    if produto in estoque:
        print(f'Produto: {produto} - Preco: {preco}')

#* item b
for nome_produto in estoque.keys():
    print(nome_produto)