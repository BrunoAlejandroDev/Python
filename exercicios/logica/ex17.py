'''
Data: 17/06/25
Exercício: Caça ao Número Primo
Enunciado: Crie uma função que recebe um número inteiro e verifica se ele é um número primo. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo. A função deve retornar True se for primo e False caso contrário.
Exemplo:
Entrada: 7 -> Saída: True
Entrada: 10 -> Saída: False
Dicas:
Lembre-se que o número 1 não é primo.
Você pode usar um laço for para testar a divisibilidade do número desde 2 até a sua raiz quadrada. Se encontrar algum divisor, ele não é primo.
'''
import math

def encontrar_num_primo(numero):
    try:
        #* Verificar se numero eh igual a 1
        if numero == 1:
            return f'O numero {numero} nao eh primo'
        
        #* Verificar se o numero eh igual ou menor que 0
        if numero <= 0:
            raise ValueError('Error. Nao sao aceitos numeros menores ou iguais a 0.')
        
        #* Verificar se eh primo ou nao
        if numero > 1:
            for i in range(2, int(math.sqrt(numero))):
                if numero % i == 0:
                    return f'Numero {numero} nao eh numero primo'
            return f'O numero {numero} eh um numero primo'
    except ValueError as ve:
        return ve
    
numero = 5
print(encontrar_num_primo(numero))