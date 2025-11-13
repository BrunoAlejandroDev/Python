'''
Exercício: O Guardião da Ponte (Condição do Triângulo)
Enunciado:
Para atravessar uma ponte mágica, você precisa provar que entende de geometria. O guardião pede que você informe três comprimentos de varetas e ele dirá se é possível formar um triângulo com elas.
A regra para formar um triângulo é: a soma de quaisquer dois lados deve ser sempre maior que o terceiro lado.
Seu programa deve ler três valores (A, B, C) e imprimir "Podem formar um triângulo" ou "Não podem formar um triângulo".

Restrição Matemática:
Para formar um triângulo, as seguintes condições devem ser verdadeiras: A+B>C, A+C>B e B+C>A.
'''

def guardiao_da_ponte(ladoA, ladoB, ladoC):
    try:
        forma_triangulo = False
        if ladoA + ladoB > ladoC:
            print('Entrei no primeiro if')
            forma_triangulo = True
        elif ladoA + ladoC > ladoB:
            print('Entrei no primeiro elif')
            forma_triangulo = True
        elif ladoB + ladoC > ladoA:
            print('Entrei no segundo elif')
            forma_triangulo = True
        else:
            print('Entrei no else')
            forma_triangulo = False

        if forma_triangulo:
            return 'Podem formar um triangulo'
        else:
            raise ValueError('Nao podem formar um triangulo')

    except ValueError:
        print()

ladoA = 3
ladoB = 3
ladoC = 3
print(guardiao_da_ponte(ladoA, ladoB, ladoC))