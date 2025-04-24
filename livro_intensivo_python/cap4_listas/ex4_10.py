'''
Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
 • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
 • Exiba a mensagem Três itens do meio da lista são: Use uma fatia para exibir três itens do meio da lista.
 • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.
'''
#* Tres primeiros itens
lista = ['Python', 'Java', 'Go', 'C#', 'Javascript', 'Rust', 'Cobol']
tres_primeiros_itens = lista[:3]
print(f'Tres primeiros itens: {tres_primeiros_itens}')

#* Tres itens do meio da lista
tres_itens_meio = lista[2:5]
print(f'Tres itens do meio: {tres_itens_meio}')

#* Tres ultimos itens
tres_ultimos_itens = lista[4:]
print(f'Trez ultimos itens: {tres_ultimos_itens}')