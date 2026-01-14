
#* Matemática: Crie uma função dobrar(numero) que receba um inteiro e retorne o dobro dele.

#* criar funcao e retornar dobro
def dobrar(numero):
    return numero*2 

#* pedir numero ao usuario
numero_usuario = float(input('Digite um numero: '))

#* chamar funcao e exibir valor
print(f'Dobro de {numero_usuario}: {dobrar(numero_usuario)}')