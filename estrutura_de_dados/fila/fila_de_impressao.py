
#* Importacoes
import time
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __repr__(self):
        if self.is_empty():
            return 'A fila esta vazia'
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return '<-'.join(nodes)
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail: #* a fila nao esta vazia
            self.tail.next = new_node
        self.tail = new_node #* atualiza o ultimo elemento
        
        if self.is_empty():
            self.head = new_node
     
    def dequeue(self):
        #* Verificar se a fila esta vazia
        if self.is_empty():
            print('A fila esta vazia.')
            return None
        
        #* Salvar valor do elemento a ser removido (primeiro elemento)
        data_to_return = self.head.data
        
        #* Remover elemento
        self.head = self.head.next
        
        #* Verificar se a fila ficou vazia apos a remocao
        if self.is_empty():
            self.tail = None

        #* Retornar Dados
        print(f'Valor removido: {data_to_return}')
        return data_to_return
    
class Printer:
    def __init__(self):
        self.job_queue = Queue()
        
    def add_job(self, document_name):
        '''
        adiciona um novo trabalho a fila de impressao
        '''
        print(f'[Impressora] documento {document_name} adicinado a fila')
        self.job_queue.enqueue(document_name)
        
    def run(self):
        '''
        processar elementos da fila
        '''
        print(f'[Impressora] Iniciando impressao dos documentos')
        while not self.job_queue.is_empty():
            #* Pegar primeiro elemento da fila
            current_document = self.job_queue.dequeue() 
            
            #* Simular tempo de impressao
            print(f'-- imprimindo: {current_document}...')
            time.sleep(random.randint(1,3))
            print(f'Impressao do documento {current_document} concluida!\n')
            
        print('[Impressora] Todos os documentos foram imprimidos')
        
if __name__ == '__main__':
    my_printer = Printer()
    
    #* Documentos chegam para impressão
    my_printer.add_job("Relatorio_Vendas_Q1.pdf")
    my_printer.add_job("Apresentacao_Marketing.pptx")
    my_printer.add_job("Contrato_Cliente_Final.docx")
    my_printer.add_job("Manual_Usuario_v2.pdf")
    
    my_printer.run()