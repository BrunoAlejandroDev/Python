
#* Classificação Numérica: Crie uma função classificar_numero(numero). Ela deve retornar uma string: "Positivo e Par", "Positivo e Ímpar", "Negativo" ou "Zero".

def classificar_numero(numero):

    if numero % 2 == 0 and numero > 0:
        return 'Positivo e Par'
    
    elif numero % 2 != 0 and numero > 0:
        return 'Positivo e Impar'
    
    elif numero < 0:
        return 'Negativo'
    
    else:
        return 'Zero'
    
print(classificar_numero(-123412))