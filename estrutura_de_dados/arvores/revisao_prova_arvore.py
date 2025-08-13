''''
EXERCICIO ARVORE BINARIA DE BUSCA - LIVROS
'''

class Livro:
    '''
    Classe para representar um objeto Livro.
    Possui código e titulo como propriedades
    '''
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        
    def __str__(self):
        return f'{self.codigo} | {self.titulo}'
    
class Node:
    '''
    Classe para representar um nó da árvore.
    Cada nó será responsável por armazenar um livro, além de possuir acessos aos filhos da esquerda e direita.
    '''
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None
        
class BinaryTree:
    #* Criar o construtor da arvore e definir sua raiz como None
    def __init__(self):
        self.root = None 
    
    #* ===== PROCESSO DE INSERÇÃO =====
    def insert(self, livro):
        #* Verificar se a arvore está vazia
        if self.root is None:
            novo_no = Node(livro) #* criar novo nó para ser inserido na arvore
            self.root = novo_no #* define a raiz da arvore como sendo o novo nó
            print('Novo no inserido na raiz')
        
        #* Caso a arvore não esteja vazia, chamar função recursiva
        else:
            self._insert(self.root, livro)
            
    def _insert(self, no_atual, livro):
        
        print('Iniciar processo de insercao recursiva')
        
        #* Caso 1: Verificar se valor do nó é menor que o do nó atual
        
        #* Verificar se o valor atual do no é menor que o valor do nó que será verificado, se sim ir para a esquerda
        if livro.codigo < no_atual.livro.codigo:
            #* Verificar se o no da esquerda está vazio
            if no_atual.esquerda is None:
                novo_no = Node(livro) #* criar novo nó
                no_atual.esquerda = novo_no #* inserir o novo nó na esquerda do nó atual
                print('-- valor inserido no nó da esquerda')
            #* Caso o nó da esquerda já possua elemento, chamar a função recursiva passando o no_atual.esquerda
            else:
                self._insert(no_atual.esquerda, livro)
                
        #* Caso 2: Verificar se o valor do nó é maior que o do nó atual
        else:
            #* Verificar se o nó da direita está vazio
            if no_atual.direita is None:
                novo_no = Node(livro) #* criar novo nó
                no_atual.direita = novo_no #* inserir o novo nó na esquerda do nó atual
                print('-- valor inserido no nó da direita')
            
            #* Caso nó da direita esteja com algum valor, chamar função recursiva para o no_atual.direita
            else:
                self._insert(no_atual.direita, livro)
                
    #* ===== PROCESSO DE PERCURSO =====
    
    #* Percurso 1 - In-Order
    def in_order_traverse(self):
        lista_livros = []
        self._in_order_traverse(self.root, lista_livros)
        return lista_livros
    
    def _in_order_traverse(self, no_atual, lista_livros):
        
        #* Verificar se o nó não existe
        if no_atual is None:
            return
        
        #* Passo 1 - ir para a esquerda
        self._in_order_traverse(no_atual.esquerda, lista_livros)
        
        #* Passo 2 - processar o nó atual
        lista_livros.append(no_atual.livro)
        
        #* Passo 3 - ir para a direita
        self._in_order_traverse(no_atual.direita, lista_livros)
    
    #* Percurso 2 - Pre-Order
    def pre_order_traverse(self):
        lista_livros = []
        self._pre_order_traverse(self.root, lista_livros)
        return lista_livros
    
    def _pre_order_traverse(self, no_atual, lista_livros):
        
        #* Verificar se o nó não existe
        if no_atual is None:
            return
        
        #* Passo 1 - processar o nó atual
        lista_livros.append(no_atual.livro)
        
        #* Passo 2 - ir para a esquerda
        self._pre_order_traverse(no_atual.esquerda, lista_livros)
        
        #* Passo 3 - ir para a direita
        self._pre_order_traverse(no_atual.direita, lista_livros)
        
    #* Percurso 3 - Post-Order 
    def post_order_traverse(self):
        lista_livros = []
        self._post_order_traverse(self.root, lista_livros)
        return lista_livros
    
    def _post_order_traverse(self, no_atual, lista_livros):
        
        #* Verificar se o nó não existe
        if no_atual is None:
            return
        
        #* Passo 1: ir para a esquerda
        self._post_order_traverse(no_atual.esquerda, lista_livros)
        
        #* Passo 2 - ir para a direita
        self._post_order_traverse(no_atual.direita, lista_livros)
        
        #* Passo 3 - processar o nó atual
        lista_livros.append(no_atual.livro)
        
    #* ===== PROCESSO DE BUSCA POR CODIGO =====
    def search_by_code(self, codigo):
        print('Processo Atual: Procurar Livro por Codigo')
        return self._search_by_code(self.root, codigo)
    
    def _search_by_code(self, no_atual, codigo):
        
        #* Verificar se o nó existe
        if no_atual is None:
            print('-- livro nao encontrado')
            return None
        
        #* Verificar se o código passado é igual ao código do livro atual
        if codigo == no_atual.livro.codigo:
            print('-- livro encontrado!')
            return no_atual.livro
        
        #* Procurar os livros atraves da arvore
        if codigo < no_atual.livro.codigo: #* se codigo passado for menor que o código do livro que está sendo comparado, ir para a esquerda
            return self._search_by_code(no_atual.esquerda, codigo)
        elif codigo > no_atual.livro.codigo: #* se codigo passado for maior que o código do livro que está sendo comparado, ir para a direita
            return self._search_by_code(no_atual.direita, codigo)
        
    #* ===== PROCESSO DE BUSCA POR LIVRO =====
    def search_by_title(self, titulo):
        print('Processo Atual: Procurar Livro por Titulo')
        #* Pegar uma lista de todos os livros
        livros = self.in_order_traverse()
        
        #* Iterar por todos os livros
        for livro in livros:
            livro_normalizado = livro.titulo.lower()
            if livro_normalizado == titulo:
                print('-- Livro encontrado')
                return livro
            
        print('-- Livro nao encontrado')
        return None
    
    #* ===== MÉTODO PÚBLICO DE REMOÇÃO =====
    def remove(self, codigo):
        #* A função pública apenas inicia a remoção a partir da raiz.
        #* Ela religa a raiz da árvore com o resultado da operação de remoção.
        self.root = self._remove(self.root, codigo)

    # --- MÉTODO PRIVADO E RECURSIVO DE REMOÇÃO ---
    def _remove(self, no_atual, codigo):
        #* CASO BASE: Se o nó atual é None, significa que não encontramos o código.
        #* Retornamos None pois não há nada a fazer.
        if no_atual is None:
            return None

        #* PASSO 1: Encontrar o nó a ser removido (navegação)
        if codigo < no_atual.livro.codigo:
            #* O código está na sub-árvore esquerda.
            #* Religamos a sub-árvore esquerda com o resultado da remoção nela.
            no_atual.esquerda = self._remove(no_atual.esquerda, codigo)
        elif codigo > no_atual.livro.codigo:
            #* O código está na sub-árvore direita.
            #* Religamos a sub-árvore direita com o resultado da remoção nela.
            no_atual.direita = self._remove(no_atual.direita, codigo)
        else:
            #* ENCONTRAMOS O NÓ! Agora, tratamos os 3 casos de remoção.
            
            #* CASO 1: O nó é uma folha (não tem filhos à esquerda NEM à direita)
            if no_atual.esquerda is None and no_atual.direita is None:
                #* Simplesmente removemos a referência a ele, retornando None.
                return None
            
            #* CASO 2: O nó tem apenas um filho (à direita OU à esquerda)
            #* Se não tem filho à esquerda, o único filho só pode ser o da direita.
            elif no_atual.esquerda is None:
                # Retornamos o filho da direita para substituir o nó atual.
                return no_atual.direita
            #* Se não tem filho à direita, o único filho só pode ser o da esquerda.
            elif no_atual.direita is None:
                #* Retornamos o filho da esquerda para substituir o nó atual.
                return no_atual.esquerda

            #* CASO 3: O nó tem dois filhos (o caso complexo)
            else:
                #* Estratégia: Encontrar o "sucessor em ordem" - o menor nó na sub-árvore da direita.
                sucessor = self._find_min(no_atual.direita)
                
                #* Copiar os dados do sucessor para o nó atual (efetivamente "substituindo" o valor).
                no_atual.livro = sucessor.livro
                
                #* Agora, remover o nó sucessor (que agora é um duplicado) da sub-árvore direita.
                #* Essa chamada recursiva cairá em um caso mais simples (Caso 1 ou 2).
                no_atual.direita = self._remove(no_atual.direita, sucessor.livro.codigo)

        #* Retorna o nó atual (com suas sub-árvores possivelmente modificadas).
        return no_atual

    #* ===== FUNÇÃO AJUDANTE PARA ENCONTRAR O MENOR NÓ EM UMA SUB-ÁRVORE =====
    def _find_min(self, no_atual):
        #* O menor nó está sempre o mais à esquerda possível.
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual
    
#* ===== Bloco 2: Função Principal com o Menu Interativo =====

def main():
    """Função que executa o menu principal da aplicação."""
    biblioteca = BinaryTree()
    # Adicionando alguns livros para começar
    biblioteca.insert(Livro(150, "A Guerra dos Tronos"))
    biblioteca.insert(Livro(101, "O Senhor dos Anéis"))
    biblioteca.insert(Livro(210, "Duna"))
    biblioteca.insert(Livro(120, "O Hobbit"))
    
    while True:
        print("\n--- Biblioteca Digital ---")
        print("1. Inserir novo livro")
        print("2. Remover livro por código")
        print("3. Buscar livro")
        print("4. Mostrar todos os livros")
        print("5. Sair")
        
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: Por favor, digite um número.")
            continue

        if escolha == 1:
            try:
                codigo = int(input("Digite o código do livro: "))
                titulo = input("Digite o título do livro: ")
                biblioteca.insert(Livro(codigo, titulo))
                print("Livro inserido com sucesso!")
            except ValueError:
                print("Erro: O código deve ser um número inteiro.")

        elif escolha == 2:
            try:
                codigo = int(input("Digite o código do livro a ser removido: "))
                biblioteca.remove(codigo)
                print(f"Tentativa de remoção do livro com código {codigo} concluída.")
            except ValueError:
                print("Erro: O código deve ser um número inteiro.")

        elif escolha == 3:
            print("Buscar por: 1. Código | 2. Título")
            try:
                sub_escolha = int(input("Sua escolha: "))
                if sub_escolha == 1:
                    codigo = int(input("Digite o código: "))
                    livro = biblioteca.search_by_code(codigo)
                    if livro:
                        print(f"Livro encontrado: {livro}")
                    else:
                        print("Livro não encontrado.")
                elif sub_escolha == 2:
                    titulo = input("Digite o título: ")
                    livro = biblioteca.search_by_title(titulo)
                    if livro:
                        print(f"Livro encontrado: {livro}")
                    else:
                        print("Livro não encontrado.")
                else:
                    print("Opção de busca inválida.")
            except ValueError:
                print("Erro: Escolha ou código inválido.")

        elif escolha == 4:
            print("Mostrar em: 1. In-Ordem (por código) | 2. Pré-Ordem | 3. Pós-Ordem")
            try:
                sub_escolha = int(input("Sua escolha: "))
                livros = []
                if sub_escolha == 1:
                    livros = biblioteca.in_order_traverse()
                elif sub_escolha == 2:
                    livros = biblioteca.pre_order_traverse()
                elif sub_escolha == 3:
                    livros = biblioteca.post_order_traverse()
                else:
                    print("Opção de listagem inválida.")
                
                if not livros:
                    print("A biblioteca está vazia ou a opção foi inválida.")
                else:
                    for livro in livros:
                        print(livro)
            except ValueError:
                print("Erro: Opção inválida.")
        
        elif escolha == 5:
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# ===== Bloco 3: Execução do Programa =====
# Verifica se o script está sendo executado diretamente para chamar a função main.
if __name__ == "__main__":
    main()