'''
Crie uma tupla numeros de 1 a 10.
a) Conte quantas vezes o número 5 aparece.
b) Desempacote os três primeiros elementos em a, b e c.
'''

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#* item a:
numero5 = numeros.count(5)
print(numero5)

#* item b:
primeiros_numeros = numeros[:3]
numero1, numero2, numero3 = primeiros_numeros
print(f'{numero1}, {numero2}, {numero3}')