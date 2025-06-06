class Usuario:
    def __init__(self, nome, numero_conta, valor_conta, credito_disponivel):
        self.nome = nome
        self.numero_conta = numero_conta
        self.valor_conta = valor_conta
        self.credito_disponivel = credito_disponivel
        self.proximo = None
        self.anterior = None # variavel para adicionar logica de anterior

    def __str__(self):
        return f"Nome: {self.nome}, Numero da Conta: {self.numero_conta}, Valor na Conta: {self.valor_conta}, Credito Disponivel: {self.credito_disponivel}"
    
class AdministrarBanco:
    def __init__(self):
        self.front = None
        self.rear = None

    def cadastrar_usuario(self, usuario):
        if not self.rear: # verifica se a fila esta vazia
            self.front = usuario
            self.rear = usuario
        else: # a fila possui usuarios
            self.rear.proximo = usuario # conecta o novo usuario com o fim da fila
            usuario.anterior = self.rear # o anterior do novo no é o antigo fim da fila
            self.rear = usuario # atualiza o fim da fila para ser o novo usuario

    def excluir_usuario(self):
        if not self.front:
            print("Nenhum usuario na fila para remover.")
            return

        removido = self.front
        self.front = self.front.proximo # move o front para ser o proximo elemento

        if not self.front: # fila nao ficou vazia
            self.front.anterior = None # remove a conexao com o usuario antigo

        else: # se a fila ficou vazia    
            self.rear = None # atualiza o rear para o none

        print(f"Usuario {removido.nome} com numero de conta {removido.numero_conta} removido.")
        return removido

    def listar_usuarios(self):
        atual = self.front
        while atual:
            print(atual)
            atual = atual.proximo

    def ordenar_usuarios_por_credito_crescente(self):
        if not self.front or not self.front.proximo:
            return

        trocou = True
        while trocou:
            trocou = False
            atual = self.front
            while atual.proximo:
                if atual.credito_disponivel > atual.proximo.credito_disponivel:
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    atual.numero_conta, atual.proximo.numero_conta = atual.proximo.numero_conta, atual.numero_conta
                    atual.valor_conta, atual.proximo.valor_conta = atual.proximo.valor_conta, atual.valor_conta
                    atual.credito_disponivel, atual.proximo.credito_disponivel = atual.proximo.credito_disponivel, atual.credito_disponivel
                    trocou = True
                atual = atual.proximo

    def ordenar_usuarios_por_credito_decrescente(self):
        self.ordenar_usuarios_por_credito_crescente()
        self.inverter_lista()

    def inverter_lista(self):
        anterior = None
        atual = self.front
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.front, self.rear = self.rear, self.front
def main():
    banco = AdministrarBanco()

    while True:
        print("\nGerenciamento de UsuÃ¡rios do Banco")
        print("1. Cadastrar usuÃ¡rio")
        print("2. Excluir usuÃ¡rio")
        print("3. Mostrar todos os usuÃ¡rios")
        print("4. Ordenar usuÃ¡rios por crÃ©dito (crescente)")
        print("5. Ordenar usuÃ¡rios por crÃ©dito (decrescente)")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            nome = input("Digite o nome do usuÃ¡rio: ")
            numero_conta = input("Digite o nÃºmero da conta: ")
            valor_conta = float(input("Digite o valor da conta: "))
            credito_disponivel = float(input("Digite o crÃ©dito disponÃ­vel: "))
            novo_usuario = Usuario(nome, numero_conta, valor_conta, credito_disponivel)
            banco.cadastrar_usuario(novo_usuario)
            print("UsuÃ¡rio cadastrado com sucesso.")
        elif escolha == 2:
            banco.excluir_usuario()
        elif escolha == 3:
            print("\nLista de todos os usuÃ¡rios do banco:")
            banco.listar_usuarios()
        elif escolha == 4:
            banco.ordenar_usuarios_por_credito_crescente()
            print("UsuÃ¡rios ordenados por crÃ©dito disponÃ­vel em ordem crescente.")
        elif escolha == 5:
            banco.ordenar_usuarios_por_credito_decrescente()
            print("UsuÃ¡rios ordenados por crÃ©dito disponÃ­vel em ordem decrescente.")
        elif escolha == 6:
            print("Saindo...")
            break
        else:
            print("OpÃ§Ã£o invÃ¡lida! Tente novamente.")

if __name__ == "__main__":
    main()