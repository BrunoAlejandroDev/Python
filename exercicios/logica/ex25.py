produtos = [
    {'nome': 'Maçã', 'categoria': 'Fruta'},
    {'nome': 'Alface', 'categoria': 'Verdura'},
    {'nome': 'Banana', 'categoria': 'Fruta'},
    {'nome': 'Cenoura', 'categoria': 'Legume'},
    {'nome': 'Tomate', 'categoria': 'Fruta'} 
]

categorias_agrupadas = {}
for produto in produtos:
    nome_produto = produto['nome']
    categoria = produto['categoria']
    
    if not categoria in categorias_agrupadas:
        categorias_agrupadas[categoria] = [nome_produto]
    else:
        categorias_agrupadas[categoria] += [nome_produto]
    
print(categorias_agrupadas)