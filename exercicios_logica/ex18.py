'''
Data: 17/06/25
Exercício: Sistema de Votação
Enunciado: Crie um programa que simule um sistema de votação. Os candidatos são representados por números. O programa deve:
    Receber votos (números inteiros) um a um até que o número 0 seja digitado para encerrar a votação.
    Contabilizar os votos para cada candidato.
    Contabilizar votos nulos (qualquer voto para um candidato inexistente, ex: número negativo) e votos em branco (use um número específico, como 99).
Ao final, exibir um relatório com:
    O total de votos para cada candidato.
    O total de votos nulos e em branco.
    O candidato vencedor.
Exemplo de Votação: Entradas: 1, 2, 1, 3, 1, 2, 99, -5, 0 (encerra)
'''

dict_candidatos = {
    'Carlin caba bom' : {'numero_candidato' : 1, 'votos' : 0},
    'Chico da promessa' : {'numero_candidato' : 2, 'votos' : 0},
    'Ana da fruta' : {'numero_candidato' : 3, 'votos' : 0},
    'Titia leila' : {'numero_candidato' : 4, 'votos' : 0},
}

def urna_eletronica(voto):
    votos_branco = 0
    votos_nulos = 0
    votos_validos = 0

    #* Verificar se o voto eh branco
    if voto == 99:
        votos_branco += 1
        return 'Voto em branco registrado com sucesso.'

    #* Verificar se o voto eh nulo
    if voto < 0:
        votos_nulos += 1
        return 'Voto nulo registrado com sucesso.'

    #* Verificar votos validos
    voto_registrado = False
    for candidato, dados in dict_candidatos.items():
        if voto == dados['numero_candidato']:
            dados['votos'] += 1
            votos_validos += 1
            voto_registrado = True
            return 'Voto registrado com sucesso.'
    
    #* Verificar se dentre os votos validos teve algum valor divergente
    if not voto_registrado:
        votos_nulos += 1

def apresentar_resultado():
    print('\n=== Resultados da Eleicao ===')
    for nome, dados in dict_candidatos.items():
        print(f'Nome do candidato(a): {nome} | Numero de votos: {dados["votos"]}')
    print()

def main():
    #* Mostrar os candidatos ao usuario
    for nome, numero in dict_candidatos.items():
        print(f'Nome do candidato(a): {nome} | Numero do candidato(a): {numero["numero_candidato"]}')

    #* Pedir o voto do usuario
    print('\n=== URNA ELETRONICA ===')
    print('Regras:\n Digite o numero do candidato para realizar o voto no mesmo\n Digite 99 para voto nulo\n Digite 0 para sair\n')
    while True:
        try:
            voto_usuario = int(input('Digite o numero do candidato: '))
            if voto_usuario == 0:
                break
            urna_eletronica(voto_usuario)
        except ValueError:
            print('Entrada inválida! Digite apenas numeros inteiros.')

    resultado = input('Voce deseja ver o resultado da eleicao (s/n)? ')
    if resultado.lower() == 's':
        apresentar_resultado()
    else:
        main()

main()