def obter_palpite():
    '''
    O objetivo dessa função é pedir o palpite do usuário, validar a entrada (se é numero e se está no intervalo). 
    Deve retornar apenas em casa de valor válido.
    '''
    while True:
        try:
            #* Pedir valor de palpite do usuario
            input_usuario = int(input('Digite o valor do seu palpite: '))
            
            #* Verificar se o valor digitado esta dentro do intervalo
            if 1 <= input_usuario <= 100: #? comparacao encadeada
                return input_usuario
            else:
                print('O numero digitado esta fora do intervalo (1 a 100).')
        
        except ValueError:
            print('Erro: A entrada deve numerica. Apenas numeros sao aceitos.')