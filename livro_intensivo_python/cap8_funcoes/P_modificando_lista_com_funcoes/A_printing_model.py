
#* Criar listas para armazenar valores nao impressos e impressos
design_nao_impressos = ['Agenda', 'Headset', 'Garrafa']
design_feitos = []

#* Loop para percorrer os designs nao impressoes e adicionar na lista vazia
while design_nao_impressos:
    # pegando o ultimo item da lista de nao impressos
    impressao_atual = design_nao_impressos.pop()
    print(f'Impressao atual: {impressao_atual}')
    
    # inserindo a impressao atual na lista de impressoes feitas
    design_feitos.append(impressao_atual)
    
for impressao in design_feitos:
    print('Impressao finalizada: ')
    print(impressao)