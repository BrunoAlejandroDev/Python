'''
Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Então faça o seguinte:
 • Adicione uma nova pizza à lista original.
 • Adicione uma pizza diferente à lista friend_pizzas.
 • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada
'''
import copy

pizzas = ['calabresa', 'frango com bacon', 'chocolate']
friend_pizzas = copy.copy(pizzas)

#* Adicionar uma nova pizza a lista original
pizzas.append('portuguesa')
print(f'Lista original com adicao de novo sabor: {pizzas}')

#* Adicionar uma pizza diferente a lista friend_pizzas
friend_pizzas.append('carne do sol')
print(f'Lista do amigo com adicao de novo sabor: {friend_pizzas}')

#* Exibir as listas
print('Minhas pizzas favoritas sao: ')
for pizza in pizzas:
    print(pizza)
    
print('As pizzas favoritas do meu amigo sao: ')
for pizza in friend_pizzas:
    print(pizza)