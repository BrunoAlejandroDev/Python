'''
Data: 30/06/25
Exercício: Agrupando por Categoria
Enunciado: Você recebeu uma lista de produtos, onde cada produto é um dicionário. Crie uma função que agrupe esses produtos por categoria e retorne um dicionário onde as chaves são as categorias e os valores são listas com os nomes dos produtos daquela categoria.

Exemplo:
Entrada:
produtos = [
    {"nome": "Maçã", "categoria": "Fruta"},
    {"nome": "Alface", "categoria": "Verdura"},
    {"nome": "Banana", "categoria": "Fruta"},
    {"nome": "Cenoura", "categoria": "Legume"},
    {"nome": "Laranja", "categoria": "Fruta"},
]
Saída esperada:
{
    "Fruta": ["Maçã", "Banana", "Laranja"],
    "Verdura": ["Alface"],
    "Legume": ["Cenoura"]
}
'''

produtos = [
    {"nome": "Maçã", "categoria": "Fruta"},
    {"nome": "Alface", "categoria": "Verdura"},
    {"nome": "Banana", "categoria": "Fruta"},
    {"nome": "Cenoura", "categoria": "Legume"},
    {"nome": "Laranja", "categoria": "Fruta"},
]

#* Novo dicionario
categoria_de_produtos = {}

#* Percorrer as chaves de cada dicionario
for produto in produtos:
    categoria = produto['categoria'] # variavel de acesso ao nome de cada categoria
    nome_produto = produto['nome'] # variavel de acesso ao nome de cada produto

    #* Verificar se a chave categoria existe no novo dicionario e adicionar uma nova categoria e o produto associado
    if not categoria in categoria_de_produtos:
        categoria_de_produtos[categoria] = [nome_produto]
    else: #* caso a categoria ja exista, adicione apenas o produto correspondente a categoria 
        categoria_de_produtos[categoria].append(nome_produto)

print(categoria_de_produtos)