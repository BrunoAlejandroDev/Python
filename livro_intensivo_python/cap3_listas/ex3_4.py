'''
Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.
'''

lista_convidados = ['Alicia', 'Souza', 'Leonardo']
mensagem_p1 = f'{lista_convidados[0]}, meu amor, estou enviando este convite para lhe convidar para um jantar romantico, você aceita?'
mensagem_p2 = f'Ola, {lista_convidados[1]}. Estou enviando este convite para um jantar, para discutirmos sobre nosso projeto.'
mensagem_p3 = f'Ola, {lista_convidados[2]}. Estou lhe chamando para um jantar para discutirmos o seguimento do meu TCC.'

print(mensagem_p1)
print(mensagem_p2)
print(mensagem_p3)

#* questao 3.5
print(f'O {lista_convidados[1]} nao podera comparecer ao jantar.')