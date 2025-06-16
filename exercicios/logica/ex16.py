'''
Data: 16/06/25
Exercício: Semáforo de Trânsito
Enunciado: Escreva um programa que recebe uma cor de semáforo como entrada ("verde", "amarelo" ou "vermelho") e exibe uma mensagem correspondente: "Siga", "Atenção" ou "Pare". Se a cor for inválida, informe o usuário.
Exemplo:
Entrada: "amarelo"
Saída: "Atenção"
Entrada: "azul"
Saída: "Cor inválida."
'''

def sinal_de_transito(cor):
    dict_cores_sinal = {
        'verde' : 'Siga',
        'amarelo' : 'Atencao',
        'vermelho' : 'Pare'
    }
    cor_formatada = cor.lower() # formata a cor para minusculo para ficar igual ao dicionario

    for cor_sinal, mensagem in dict_cores_sinal.items():
        if cor_formatada == cor_sinal:
            return mensagem
    return 'Cor invalida'
        
cor_semaforo = 'verde'
print(sinal_de_transito(cor_semaforo))