from datetime import datetime, timedelta

class Livro:
    def __init__(self, id, nome, data_devolucao=None):
        self.id = id
        self.nome = nome
        self.data_devolucao = data_devolucao
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Data de Devolucao: {self.data_devolucao}"

class Acervo:
    def __init__(self):
        self.head = None
        self.tail = None
        self.inicializar_acervo()

    def inicializar_acervo(self):
        livros_iniciais = [
            ("1", "Livro A"),
            ("2", "Livro B"),
            ("3", "Livro C"),
            ("4", "Livro D"),
            ("5", "Livro E"),
            ("6", "Livro F"),
            ("7", "Livro G"),
            ("8", "Livro H"),
            ("9", "Livro I"),
            ("10", "Livro J")
        ]

        anterior = None
        for id, nome in livros_iniciais:
            novo_livro = Livro(id, nome)
            if self.head is None:
                self.head = novo_livro
            else:
                anterior.proximo = novo_livro
                novo_livro.anterior = anterior
            anterior = novo_livro
        self.tail = anterior

    def adicionar_livro(self, id, nome):
        novo_livro = Livro(id, nome)
        if not self.head:
            self.head = novo_livro
            return
        self.tail.proximo = novo_livro
        novo_livro.anterior = self.tail
        self.tail = novo_livro

    def remover_livro(self, id):
        atual = self.head
        while atual and atual.id != id:
            atual = atual.proximo
        if atual is None:
            print("Livro nao encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        if atual == self.head:
            self.head = atual.proximo
        if atual == self.tail:
            self.tail = atual.anterior
        print(f"Livro com ID {id} removido.")

    def primeiro_livro(self):
        return self.head

    def exibir_acervo(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo

    def procurar_livro_por_id(self, id):
        head_atual = self.head
        tail_atual = self.tail
        
        while head_atual and tail_atual and head_atual != tail_atual and head_atual.proximo != tail_atual:
            if head_atual.id == id:
                print("Livro encontrado (a partir do head): ")
                print(head_atual)
                if head_atual.proximo:
                    print("Proximo livro na lista: ")
                    print(head_atual.proximo)
                else:
                    print("Este eh o ultimo livro na lista.")
                return
            if tail_atual.id == id:
                print("Livro encontrado (a partir do tail): ")
                print(tail_atual)
                if tail_atual.proximo:
                    print("Proximo livro na lista: ")
                    print(tail_atual.proximo)
                else:
                    print("Este nao eh o ultimo livro na lista.")
                return
            
            head_atual = head_atual.proximo
            tail_atual = tail_atual.anterior
        
        print("Livro nao encontrado.")

    def alugar_livro(self, id, dias_para_devolucao):
        atual = self.head
        while atual:
            if atual.id == id:
                data_devolucao = datetime.now() + timedelta(days=dias_para_devolucao)
                atual.data_devolucao = data_devolucao.strftime("%d/%m/%Y")
                print(f"Livro '{atual.nome}' alugado ate {atual.data_devolucao}")
                return
            atual = atual.proximo
        print("Livro nao encontrado.")

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}"

class Biblioteca:
    def __init__(self):
        self.usuarios_head = None
        self.usuarios_tail = None
        self.acervo = Acervo()
        self.inicializar_usuarios()

    def inicializar_usuarios(self):
        usuarios_iniciais = [
            ("1", "Daniel"),
            ("2", "Violeta"),
            ("3", "Francisco")
        ]

        anterior = None
        for id, nome in usuarios_iniciais:
            novo_usuario = Usuario(id, nome)
            if self.usuarios_head is None:
                self.usuarios_head = novo_usuario
            else:
                anterior.proximo = novo_usuario
                novo_usuario.anterior = anterior
            anterior = novo_usuario
        self.usuarios_tail = anterior

    def adicionar_usuario(self, id, nome):
        novo_usuario = Usuario(id, nome)
        if not self.usuarios_head:
            self.usuarios_head = novo_usuario
            self.usuarios_tail = novo_usuario
            return
        self.usuarios_tail.proximo = novo_usuario
        novo_usuario.anterior = self.usuarios_tail
        self.usuarios_tail = novo_usuario

    def remover_usuario(self, id):
        atual = self.usuarios_head
        while atual and atual.id != id:
            atual = atual.proximo
        if atual is None:
            print("Usuario nao encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        if atual == self.usuarios_head:
            self.usuarios_head = atual.proximo
        if atual == self.usuarios_tail:
            self.usuarios_tail = atual.anterior
        print(f"Usuario com ID {id} removido.")

    def listar_usuarios(self):
        atual = self.usuarios_head
        while atual:
            print(atual)
            atual = atual.proximo

    def procurar_usuario_por_id(self, id):
        atual = self.usuarios_head
        while atual:
            if atual.id == id:
                return atual
            atual = atual.proximo
        return None
    
    def ordenar_usuarios(self):
        if self.usuarios_head is None or self.usuarios_head.proximo is None:
            return

        trocou = True
        while trocou:
            trocou = False
            atual = self.usuarios_head
            while atual.proximo:
                if int(atual.id) > int(atual.proximo.id):
                    # Troca os valores entre os nÃ³s
                    atual.id, atual.proximo.id = atual.proximo.id, atual.id
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    trocou = True
                atual = atual.proximo


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nGerenciamento de Biblioteca")
        print("1. Listar todos os usuarios")
        print("2. Adicionar usuario")
        print("3. Remover usuario")
        print("4. Selecionar usuario e gerenciar acervo")
        print("5. Ordenar usuarios por ID")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            print("\nLista de todos os usuarios:")
            biblioteca.listar_usuarios()
        elif escolha == 2:
            id = input("Digite o ID do usuario: ")
            nome = input("Digite o nome do usuario: ")
            biblioteca.adicionar_usuario(id, nome)
            print("UsuÃ¡rio adicionado com sucesso.")
        elif escolha == 3:
            id = input("Digite o ID do usuario a ser removido: ")
            biblioteca.remover_usuario(id)
        elif escolha == 4:
            id = input("Digite o ID do usuario: ")
            usuario = biblioteca.procurar_usuario_por_id(id)
            if usuario:
                while True:
                    print("\nGerenciamento de Acervo")
                    print("1. Listar todos os livros")
                    print("2. Exibir primeiro livro da vitrine")
                    print("3. Adicionar livro")
                    print("4. Remover livro")
                    print("5. Procurar livro por ID")
                    print("6. Alugar livro")
                    print("7. Voltar")

                    escolha_acervo = int(input("Digite sua escolha: "))

                    if escolha_acervo == 1:
                        print("\nLista de todos os livros no acervo:")
                        biblioteca.acervo.exibir_acervo()
                    elif escolha_acervo == 2:
                        print("\nPrimeiro livro da vitrine (head da lista):")
                        print(biblioteca.acervo.primeiro_livro())
                    elif escolha_acervo == 3:
                        id_livro = input("Digite o ID do livro: ")
                        nome_livro = input("Digite o nome do livro: ")
                        biblioteca.acervo.adicionar_livro(id_livro, nome_livro)
                        print("Livro adicionado com sucesso.")
                    elif escolha_acervo == 4:
                        id_livro = input("Digite o ID do livro a ser removido: ")
                        biblioteca.acervo.remover_livro(id_livro)
                    elif escolha_acervo == 5:
                        id_livro = input("Digite o ID do livro a ser procurado: ")
                        biblioteca.acervo.procurar_livro_por_id(id_livro)
                    elif escolha_acervo == 6:
                        id_livro = input("Digite o ID do livro a ser alugado: ")
                        dias_para_devolucao = int(input("Digite o numero de dias para devolucao: "))
                        biblioteca.acervo.alugar_livro(id_livro, dias_para_devolucao)
                    elif escolha_acervo == 7:
                        break
                    else:
                        print("Opcao invalida! Tente novamente.")
            else:
                print("Usuario nao encontrado.")
        elif escolha == 5:
            biblioteca.ordenar_usuarios()
            print("Usuarios ordenados com sucesso.")
        elif escolha == 6:
            print("Saindo...")
            break
        else:
            print("Opcao invalida! Tente novamente.")

if __name__ == "__main__":
    main()
    
####################################
from datetime import datetime, timedelta

class Livro:
    def __init__(self, id_livro, nome, data_devolucao=None): # Renomeado 'id' para 'id_livro' para evitar conflito com a função built-in id()
        self.id_livro = id_livro
        self.nome = nome
        self.data_devolucao = data_devolucao
        # O atributo 'proximo' não é mais necessário

    def __str__(self):
        return f"ID: {self.id_livro}, Nome: {self.nome}, Data de DevoluÃ§Ã£o: {self.data_devolucao}"

class Acervo:
    def __init__(self):
        self.livros = [] # Usamos uma lista Python em vez de head/tail
        self.inicializar_acervo()

    def inicializar_acervo(self):
        livros_iniciais = [
            ("1", "Livro A"), ("2", "Livro B"), ("3", "Livro C"),
            ("4", "Livro D"), ("5", "Livro E"), ("6", "Livro F"),
            ("7", "Livro G"), ("8", "Livro H"), ("9", "Livro I"),
            ("10", "Livro J")
        ]
        for id_livro, nome in livros_iniciais:
            self.adicionar_livro(id_livro, nome)

    def adicionar_livro(self, id_livro, nome):
        # Verifica se já existe um livro com o mesmo ID
        for livro in self.livros:
            if livro.id_livro == id_livro:
                print(f"Erro: Livro com ID {id_livro} jÃ¡ existe.")
                return
        novo_livro = Livro(id_livro, nome)
        self.livros.append(novo_livro) # Simplesmente adiciona à lista
        print(f"Livro '{nome}' adicionado com sucesso.")

    def remover_livro(self, id_livro):
        livro_para_remover = None
        for livro in self.livros:
            if livro.id_livro == id_livro:
                livro_para_remover = livro
                break
        
        if livro_para_remover:
            self.livros.remove(livro_para_remover) # Método remove() da lista
            print(f"Livro com ID {id_livro} removido.")
        else:
            print("Livro nÃ£o encontrado para remoÃ§Ã£o.")

    def primeiro_livro(self):
        if self.livros: # Verifica se a lista não está vazia
            return self.livros[0] # Retorna o primeiro elemento
        return None

    def exibir_acervo(self):
        if not self.livros:
            print("Acervo vazio.")
            return
        for livro in self.livros: # Iteração direta sobre a lista
            print(livro)

    def procurar_livro_por_id(self, id_livro_procurado): # Renomeada a variável local para clareza
        for i, livro in enumerate(self.livros): # enumerate para ter o índice também
            if livro.id_livro == id_livro_procurado:
                print("Livro encontrado:")
                print(livro)
                if i + 1 < len(self.livros):
                    print("PrÃ³ximo livro na lista (baseado na ordem atual):")
                    print(self.livros[i+1])
                else:
                    print("Este Ã© o Ãºltimo livro da lista (baseado na ordem atual).")
                return livro # Retorna o objeto livro encontrado
        print("Livro nÃ£o encontrado.")
        return None

    def alugar_livro(self, id_livro, dias_para_devolucao):
        livro_encontrado = self.procurar_livro_por_id(id_livro) # Reutiliza a busca
        if livro_encontrado:
            if livro_encontrado.data_devolucao:
                print(f"Livro '{livro_encontrado.nome}' jÃ¡ estÃ¡ alugado atÃ© {livro_encontrado.data_devolucao}.")
                return

            data_devolucao = datetime.now() + timedelta(days=dias_para_devolucao)
            livro_encontrado.data_devolucao = data_devolucao.strftime("%d/%m/%Y")
            print(f"Livro '{livro_encontrado.nome}' alugado atÃ© {livro_encontrado.data_devolucao}")
        # A mensagem "Livro não encontrado" já é impressa por procurar_livro_por_id


class Usuario:
    def __init__(self, id_usuario, nome): # Renomeado 'id' para 'id_usuario'
        self.id_usuario = id_usuario
        self.nome = nome
        # O atributo 'proximo' não é mais necessário

    def __str__(self):
        return f"ID: {self.id_usuario}, Nome: {self.nome}"

class Biblioteca:
    def __init__(self):
        self.usuarios = [] # Lista Python para usuários
        self.acervo = Acervo() # A composição com Acervo permanece
        self.inicializar_usuarios()

    def inicializar_usuarios(self):
        usuarios_iniciais = [
            ("1", "Daniel"),
            ("2", "Violeta"),
            ("3", "Francisco")
        ]
        for id_usuario, nome in usuarios_iniciais:
            self.adicionar_usuario(id_usuario, nome)

    def adicionar_usuario(self, id_usuario, nome):
        # Verifica se já existe um usuário com o mesmo ID
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                print(f"Erro: UsuÃ¡rio com ID {id_usuario} jÃ¡ existe.")
                return
        novo_usuario = Usuario(id_usuario, nome)
        self.usuarios.append(novo_usuario)
        print(f"UsuÃ¡rio '{nome}' adicionado com sucesso.")


    def remover_usuario(self, id_usuario):
        usuario_para_remover = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_para_remover = usuario
                break
        
        if usuario_para_remover:
            self.usuarios.remove(usuario_para_remover)
            print(f"UsuÃ¡rio com ID {id_usuario} removido.")
        else:
            print("UsuÃ¡rio nÃ£o encontrado para remoÃ§Ã£o.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuÃ¡rio cadastrado.")
            return
        for usuario in self.usuarios:
            print(usuario)

    def procurar_usuario_por_id(self, id_usuario_procurado): # Renomeada a variável local
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario_procurado:
                return usuario
        return None

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nGerenciamento de Biblioteca")
        print("1. Listar todos os usuÃ¡rios")
        print("2. Adicionar usuÃ¡rio")
        print("3. Remover usuÃ¡rio")
        print("4. Selecionar usuÃ¡rio e gerenciar acervo")
        print("5. Sair")

        try:
            escolha = int(input("Digite sua escolha: "))
        except ValueError:
            print("Entrada invÃ¡lida. Por favor, digite um nÃºmero.")
            continue

        if escolha == 1:
            biblioteca.listar_usuarios()
        elif escolha == 2:
            id_usuario_novo = input("Digite o ID do usuÃ¡rio: ")
            nome_usuario_novo = input("Digite o nome do usuÃ¡rio: ")
            biblioteca.adicionar_usuario(id_usuario_novo, nome_usuario_novo)
            # Mensagem de sucesso já é impressa pelo método
        elif escolha == 3:
            id_usuario_remover = input("Digite o ID do usuÃ¡rio a ser removido: ")
            biblioteca.remover_usuario(id_usuario_remover)
        elif escolha == 4:
            id_usuario_selecionado = input("Digite o ID do usuÃ¡rio: ")
            usuario = biblioteca.procurar_usuario_por_id(id_usuario_selecionado)
            if usuario:
                print(f"\n--- Gerenciando acervo para o usuÃ¡rio: {usuario.nome} ---")
                while True:
                    print("\nGerenciamento de Acervo")
                    print("1. Listar livros")
                    print("2. Exibir primeiro livro")
                    print("3. Adicionar livro ao acervo")
                    print("4. Remover livro do acervo")
                    print("5. Procurar livro por ID")
                    print("6. Alugar livro")
                    print("7. Voltar ao menu principal")
                    
                    try:
                        escolha_acervo = int(input("Escolha uma opÃ§Ã£o do acervo: "))
                    except ValueError:
                        print("Entrada invÃ¡lida. Por favor, digite um nÃºmero.")
                        continue

                    if escolha_acervo == 1:
                        biblioteca.acervo.exibir_acervo()
                    elif escolha_acervo == 2:
                        primeiro = biblioteca.acervo.primeiro_livro()
                        if primeiro:
                            print(f"Primeiro livro do acervo: {primeiro}")
                        else:
                            print("Acervo vazio.")
                    elif escolha_acervo == 3:
                        id_livro_novo = input("ID do livro: ")
                        nome_livro_novo = input("Nome do livro: ")
                        biblioteca.acervo.adicionar_livro(id_livro_novo, nome_livro_novo)
                    elif escolha_acervo == 4:
                        id_livro_remover = input("ID do livro a remover: ")
                        biblioteca.acervo.remover_livro(id_livro_remover)
                    elif escolha_acervo == 5:
                        id_livro_procurar = input("ID do livro: ")
                        biblioteca.acervo.procurar_livro_por_id(id_livro_procurar)
                    elif escolha_acervo == 6:
                        id_livro_alugar = input("ID do livro para alugar: ")
                        # Verifica se o livro existe antes de pedir os dias
                        livro_obj = biblioteca.acervo.procurar_livro_por_id(id_livro_alugar)
                        if livro_obj:
                            if livro_obj.data_devolucao:
                                print(f"Livro '{livro_obj.nome}' jÃ¡ estÃ¡ alugado atÃ© {livro_obj.data_devolucao}.")
                            else:
                                try:
                                    dias = int(input("Dias para devoluÃ§Ã£o: "))
                                    if dias <=0:
                                        print("NÃºmero de dias deve ser positivo.")
                                    else:
                                        biblioteca.acervo.alugar_livro(id_livro_alugar, dias)
                                except ValueError:
                                    print("NÃºmero de dias invÃ¡lido.")
                        # A mensagem de "Livro não encontrado" já é tratada por procurar_livro_por_id e alugar_livro
                    elif escolha_acervo == 7:
                        break
                    else:
                        print("OpÃ§Ã£o invÃ¡lida!")
            else:
                print("UsuÃ¡rio nÃ£o encontrado.")
        elif escolha == 5:
            print("Saindo...")
            break
        else:
            print("OpÃ§Ã£o invÃ¡lida!")

if __name__ == "__main__":
    main()