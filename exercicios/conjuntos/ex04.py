'''
Considere os conjuntos abaixo e realize as seguintes operações:
a. União
b. Interseção
c. Diferença de backend - frontend
d. Diferença de frontend - backend
e. Diferença simétrica
'''

linguagens_backend = {'Python', 'Java', 'Go', 'Ruby'}
linguagens_frontend = {'JavaScript', 'TypeScript', 'Ruby', 'Python'}

#* uniao
uniao = linguagens_backend | linguagens_frontend
print(f'Uniao: {uniao}\n')

#* Intersecao
intersecao = linguagens_backend & linguagens_frontend
print(f'Intersecao: {intersecao}\n') 

#* Diferença de backend - frontend
diferenca_back_front = linguagens_backend - linguagens_frontend
print(f'Diferenca back front: {diferenca_back_front}\n')

#* Diferenca entre frontend - backend
diferenca_front_back = linguagens_frontend - linguagens_backend
print(f'Diferenca front back: {diferenca_front_back}\n')

#* Diferenca simetrica
diferenca_simetrica = linguagens_backend ^ linguagens_frontend
print(f'Diferenca simetrica: {diferenca_simetrica}')