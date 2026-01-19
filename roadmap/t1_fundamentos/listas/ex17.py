
#* Criação e Acesso: Crie uma função pegar_primeiro_e_ultimo(lista) que receba uma lista de qualquer tamanho e retorne uma nova lista contendo apenas o primeiro e o último elemento.

lista = [1, 2, 6, 1, 19, 20, 12, 543, 6, 91, 0]

def pegar_primeiro_ultimo(lista):
    primeiro_elemento = lista[:1]
    ultimo_elemento = lista[-1:]
    lista_nova = primeiro_elemento + ultimo_elemento
    return lista_nova

print(pegar_primeiro_ultimo(lista))