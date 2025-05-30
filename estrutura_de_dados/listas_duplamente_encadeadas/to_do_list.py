from datetime import datetime

class Tarefa:
    def __init__(self, id_tarefa, descricao_tarefa, prioridade_tarefa):
        self.id_tarefa = id_tarefa
        self.descricao_tarefa = descricao_tarefa
        self.prioridade_tarefa = prioridade_tarefa
        self.status_tarefa = 'Pendente'
        self.data_criacao_tarefa = datetime.now()
        
    def __str__(self):
        return f'Informacoes da Tarefa {self.id_tarefa}:\nId: {self.id_tarefa}\nDescricao da tarefa: {self.descricao_tarefa}\nStatus da tarefa: {self.status_tarefa}\nPrioridade da tarefa: {self.prioridade_tarefa}\nData de criacao da tarefa: {self.data_criacao_tarefa.strftime('%d/%m/%y')}\n'
    
    def marcar_tarefa_concluida(self):
        self.status_tarefa = 'Concluida'
        
    def marcar_tarefa_pendente(self):
        self.status_tarefa = 'Pendente'

# exemplo_tarefa = Tarefa(1, 'Exemplo de tarefa', 'alta')
# print(exemplo_tarefa)
# exemplo_tarefa.marcar_tarefa_concluida()
# print(exemplo_tarefa)

class ListaDeTarefas:
    def __init__(self, nome_da_lista):
        self.nome_lista = nome_da_lista
        self.lista_de_tarefas = []
        
    def adicionar_tarefa(self, id, descricao, prioridade):
        for tarefa in self.lista_de_tarefas:
            if tarefa.id_tarefa == id:
                print(f'ERRO: Tarefa com o ID {id} ja existe')
                return False
        nova_tarefa = Tarefa(id, descricao, prioridade) # criacao da nova tarefa
        self.lista_de_tarefas.append(nova_tarefa) # adicao da nova tarefa a lista de tarefas
        print(f'Tarefa com id: {id} adicionada com sucesso')
        return True
    
    def remover_tarefa(self, id_tarefa):
        tarefa_a_remover = None
        for tarefa in self.lista_de_tarefas:
            if tarefa.id_tarefa == id_tarefa:
                tarefa_a_remover = tarefa
                break
        
        if tarefa_a_remover:
            self.lista_de_tarefas.remove(tarefa_a_remover)
            print(f'Tarefa com ID: {id_tarefa} removida com sucesso')
            return True
        else:
            print(f'Tarefa com ID: {id_tarefa} nao encontrada')
            return False
        
    def marcar_tarefa_como_concluida(self, id_tarefa):
        for tarefa in self.lista_de_tarefas:
            if tarefa.id_tarefa == id_tarefa:
                tarefa.marcar_tarefa_concluida()
                return True
        return False

    def marcar_tarefa_como_pendente(self, id_tarefa):
        for tarefa in self.lista_de_tarefas:
            if tarefa.id_tarefa == id_tarefa:
                tarefa.marcar_tarefa_pendente()
                return True
            else:
                print(f'ERRO: tarefa de ID: {id_tarefa} nao encontrada para marcar como pendente')
                return False
            
    def procurar_tarefa_por_id(self, id_tarefa):
        for tarefa in self.lista_de_tarefas:
            if tarefa.id_tarefa == id_tarefa:
                return tarefa
        return None
        
    def listar_tarefas(self, filtro_status, filtro_prioridade):
        #* verificar se a lista existe
        if not self.lista_de_tarefas:
            print(f'A lista {self.nome_lista} nao existe')
            return
        
        #* filtrar tarefas com base em status e prioridade
        print(f'\n=== Tarefas da Lista {self.nome_lista} ===')
        tarefas_filtradas = self.lista_de_tarefas

        if filtro_status:
            tarefas_filtradas = {tarefa for tarefa in tarefas_filtradas if tarefa.status_tarefa.lower() == filtro_status}
        if filtro_prioridade:
            tarefas_filtradas = {tarefa for tarefa in tarefas_filtradas if tarefa.prioridade_tarefa == filtro_prioridade}
        if not tarefas_filtradas:
            print('Nenhuma tarefa encontrada para os filtros aplicados')
        else:
            for tarefa in tarefas_filtradas:
                print('----------')
                print(f'{tarefa}')
                print('----------')
            
    def __str__(self):
        return f'Lista: {self.nome_lista}\n{len(self.lista_de_tarefas)} tarefas'
        
lista1 = ListaDeTarefas('Lista')
lista1.adicionar_tarefa(1, 'Exemplo de tarefa', 'alta')
lista1.adicionar_tarefa(2, 'tarefa 2', 'media')
lista1.imprimir_lista_de_tarefas()