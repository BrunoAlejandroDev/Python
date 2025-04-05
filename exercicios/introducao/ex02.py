'''
Crie um programa que utilize a palavra-chave para declarar uma constante que representa 
a velocidade da luz no vácuo. Tente alterar o valor da constante e observe o comportamento 
do Python. 
'''

def constante():
    VELOCIDADE_DA_LUZ = 299792458
    print(VELOCIDADE_DA_LUZ)
    
    try:
        VELOCIDADE_DA_LUZ = 300000000
    except Exception as e:
        print(f'Error: {e}. Nao eh possivel mudar valores constantes.')
        
constante()