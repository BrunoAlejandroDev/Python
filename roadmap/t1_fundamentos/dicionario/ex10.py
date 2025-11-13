'''
Imprima apenas as matérias com nota maior ou igual a 7.
'''

notas = {
    'matematica' : 10,
    'fisica' : 8.7,
    'biologia' : 4,
    'historia' : 6.8
}

for materia, nota in notas.items():
    if nota >= 7:
        print(f'Materia: {materia} - Nota: {nota}')