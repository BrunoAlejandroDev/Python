
#* Refatorando o arquivo printing model para uso de funcoes

#* Funcao para realizar impressao
def realizar_impressao(impressao_nao_feita, impressao_feita):
    while impressao_nao_feita:
        impressao_atual = impressao_nao_feita.pop()
        
        print(f'Impressao atual: {impressao_atual}')
        impressao_feita.append(impressao_atual)
        
def mostrar_impressoes(impressoes_feitas):
    for impressao in impressoes_feitas:
        print(f'Impressao feita: {impressao}')
        
design_nao_feitos = ['Agenda', 'Headset', 'Garrafa']
design_concluidos = []

realizar_impressao(design_nao_feitos, design_concluidos)
print()
mostrar_impressoes(design_concluidos)