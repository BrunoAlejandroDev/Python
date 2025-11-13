'''
Imprima apenas as palavras que têm mais de 4 letras.
'''

palavras = {'Python', 'C++', 'Go', 'Rust', 'Javascript'}
filtro_letras = [palavra for palavra in palavras if len(palavra) > 4]
print(filtro_letras)