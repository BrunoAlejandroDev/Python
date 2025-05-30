# --- Classe ItemMarketplace ---
class ItemMarketplace:
    """Representa um item no marketplace."""
    def __init__(self, nome: str, preco: float, descricao: str = ""):
        self.nome = nome
        self.preco = float(preco)
        self.descricao = descricao

    def __str__(self) -> str:
        return f"Item: {self.nome} | Preço: R${self.preco:.2f} | Descrição: {self.descricao if self.descricao else 'N/A'}"

    def __lt__(self, other) -> bool:
        """Permite a ordenação de itens pelo preço (e nome como desempate)."""
        if not isinstance(other, ItemMarketplace): # Boa prática manter isso
            return NotImplemented
        if self.preco == other.preco:
            return self.nome < other.nome 
        return self.preco < other.preco

    def __eq__(self, other) -> bool:
        """Verifica igualdade baseada no nome. Usado por list.remove() se passamos um objeto 'similar'."""
        if not isinstance(other, ItemMarketplace):
            return False
        return self.nome == other.nome # Simplificando para o exercício: itens são "iguais" se o nome for igual.

# --- Classe Marketplace ---
class Marketplace:
    """Representa o marketplace com uma coleção de itens."""
    def __init__(self):
        self.itens = [] # Lista de objetos ItemMarketplace

    def exibir_itens(self, titulo: str = "Itens no Marketplace:"):
        print(f"\n--- {titulo} ---")
        if not self.itens:
            print("Marketplace vazio.")
        else:
            for item in self.itens:
                print(item)
        print("--------------------")

    # A - Simples
    def inserir_inicio(self, novo_item: ItemMarketplace):
        """Insere um novo item no início do marketplace."""
        self.itens.insert(0, novo_item)
        print(f"Item '{novo_item.nome}' inserido no início.")

    def inserir_final(self, novo_item: ItemMarketplace):
        """Insere um novo item no final do marketplace."""
        self.itens.append(novo_item)
        print(f"Item '{novo_item.nome}' inserido no final.")

    def remover_por_nome(self, nome_item: str) -> bool:
        """Remove um item do marketplace pelo nome. Remove a primeira ocorrência."""
        item_para_remover = None
        for item in self.itens:
            if item.nome == nome_item:
                item_para_remover = item
                break 
        
        if item_para_remover:
            self.itens.remove(item_para_remover) # Remove o objeto específico encontrado
            print(f"Item '{nome_item}' removido.")
            return True
        else:
            print(f"Item '{nome_item}' não encontrado para remoção.")
            return False

    def verificar_disponibilidade(self, nome_item: str) -> bool:
        """Verifica se um item está disponível no marketplace pelo nome."""
        for item in self.itens:
            if item.nome == nome_item:
                print(f"Item '{nome_item}' está DISPONÍVEL.")
                return True
        print(f"Item '{nome_item}' NÃO está disponível.")
        return False

    # B - Intermediárias
    def contar_itens(self) -> int:
        """Conta quantos itens estão cadastrados no marketplace."""
        count = len(self.itens)
        print(f"Total de itens no marketplace: {count}")
        return count

    def inverter_ordem(self):
        """Inverte a ordem dos itens no marketplace."""
        self.itens.reverse()
        print("Ordem dos itens invertida.")

    def inserir_ordenado_por_preco(self, novo_item: ItemMarketplace):
        """
        Insere item no marketplace e depois reordena a lista inteira por preço.
        """
        self.itens.append(novo_item)
        self.itens.sort() # .sort() usa o __lt__ definido em ItemMarketplace
        print(f"Item '{novo_item.nome}' inserido. Marketplace ordenado por preço.")

    # C - Difícil
    @staticmethod
    def mesclar_marketplaces_ordenados(mp1, mp2):
        """
        Mescla dois marketplaces (cujas listas de itens já estão ordenadas por preço)
        em um único novo marketplace ordenado.
        """
        novo_mp = Marketplace()
        itens_mp1 = mp1.itens
        itens_mp2 = mp2.itens
        
        ptr1, ptr2 = 0, 0 # Ponteiros para as listas de mp1 e mp2
        len1, len2 = len(itens_mp1), len(itens_mp2)

        # Mescla enquanto ambas as listas têm elementos
        while ptr1 < len1 and ptr2 < len2:
            # A comparação usa o __lt__ definido em ItemMarketplace
            if itens_mp1[ptr1] < itens_mp2[ptr2]: 
                novo_mp.itens.append(itens_mp1[ptr1])
                ptr1 += 1
            else:
                novo_mp.itens.append(itens_mp2[ptr2])
                ptr2 += 1
        
        # Adiciona os elementos restantes da lista que não foi totalmente consumida
        novo_mp.itens.extend(itens_mp1[ptr1:]) # Adiciona o restante de mp1 (se houver)
        novo_mp.itens.extend(itens_mp2[ptr2:]) # Adiciona o restante de mp2 (se houver)
        
        print("Marketplaces mesclados com sucesso.")
        return novo_mp

# --- Demonstração de Uso ---
def main():
    # Criando Itens
    print(">>> CONFIGURANDO ITENS INICIAIS <<<")
    item_a = ItemMarketplace("Banana", 2.50, "Caturra")
    item_b = ItemMarketplace("Maçã", 5.00, "Gala")
    item_c = ItemMarketplace("Pera", 6.50, "Williams")
    item_d = ItemMarketplace("Uva", 8.00, "Thompson")
    item_e = ItemMarketplace("Laranja", 3.00, "Pera")
    item_f = ItemMarketplace("Abacaxi", 7.00, "Pérola")
    item_g = ItemMarketplace("Morango", 5.00, "Caixa") # Mesmo preço da Maçã

    mp = Marketplace()
    mp.exibir_itens("Marketplace Inicial (Vazio)")

    print("\n>>> DEMONSTRANDO OPERAÇÕES SIMPLES (A) <<<")
    mp.inserir_final(item_b)
    mp.inserir_inicio(item_a)
    mp.inserir_final(item_c)
    mp.exibir_itens("Após inserções iniciais") # Banana, Maçã, Pera

    mp.verificar_disponibilidade("Maçã")
    mp.verificar_disponibilidade("Melancia")
    
    mp.remover_por_nome("Maçã") 
    mp.exibir_itens("Após remoção da Maçã") # Banana, Pera


    print("\n>>> DEMONSTRANDO OPERAÇÕES INTERMEDIÁRIAS (B) <<<")
    mp_b = Marketplace()
    print("\nCriando Marketplace B com inserção seguida de ordenação por preço:")
    # A lista será ordenada a cada inserção com este método
    mp_b.inserir_ordenado_por_preco(item_c) # Pera (6.50)
    mp_b.inserir_ordenado_por_preco(item_a) # Banana (2.50), Pera (6.50)
    mp_b.inserir_ordenado_por_preco(item_e) # Banana (2.50), Laranja (3.00), Pera (6.50)
    mp_b.inserir_ordenado_por_preco(item_b) # Banana, Laranja, Maçã (5.00), Pera
    mp_b.inserir_ordenado_por_preco(item_g) # Banana, Laranja, Maçã (5.00), Morango (5.00), Pera
    mp_b.exibir_itens("Marketplace B - Após inserções 'ordenadas' (append + sort)")

    mp_b.contar_itens()
    mp_b.inverter_ordem()
    mp_b.exibir_itens("Marketplace B - Após inverter ordem")
    
    # Para a mesclagem, precisamos que mp_b esteja ordenado.
    # Como invertemos, vamos reordená-lo explicitamente.
    mp_b.itens.sort() 
    mp_b.exibir_itens("Marketplace B - Reordenado por preço para a mesclagem")


    print("\n>>> DEMONSTRANDO OPERAÇÕES DIFÍCEIS (C) <<<")
    # Criando dois marketplaces já ordenados para mesclagem
    # Adicionaremos os itens e depois garantiremos a ordenação uma vez.
    mp1_para_mesclar = Marketplace()
    mp1_para_mesclar.itens.extend([
        ItemMarketplace("Item X1", 1.00),
        ItemMarketplace("Item X3", 3.00),
        ItemMarketplace("Item X5", 5.00)
    ])
    mp1_para_mesclar.itens.sort() # Garante que está ordenado
    mp1_para_mesclar.exibir_itens("Marketplace 1 para Mesclagem (ordenado)")

    mp2_para_mesclar = Marketplace()
    mp2_para_mesclar.itens.extend([
        ItemMarketplace("Item Y2", 2.00),
        ItemMarketplace("Item Y4", 4.00),
        ItemMarketplace("Item Y6", 6.00)
    ])
    mp2_para_mesclar.itens.sort() # Garante que está ordenado
    mp2_para_mesclar.exibir_itens("Marketplace 2 para Mesclagem (ordenado)")
    
    mp_mesclado = Marketplace.mesclar_marketplaces_ordenados(mp1_para_mesclar, mp2_para_mesclar)
    mp_mesclado.exibir_itens("Marketplace Mesclado (mp1 e mp2)")

    # Exemplo de mesclagem com o mp_b (que foi reordenado)
    mp_mesclado_com_mp_b = Marketplace.mesclar_marketplaces_ordenados(mp_b, mp1_para_mesclar)
    mp_mesclado_com_mp_b.exibir_itens("Marketplace Mesclado (mp_b e mp1)")

if __name__ == "__main__":
    main()