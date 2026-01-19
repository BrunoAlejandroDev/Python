
#* Slicing Simples: Crie uma função tres_primeiros(lista) que retorne os 3 primeiros elementos de qualquer lista usando fatiamento ([:]).

def tres_primeiros_lista(lista):
    return lista[:3]

lista = ['Messi', 'Connor', 'Jones', 'Brunao']
print(tres_primeiros_lista(lista))