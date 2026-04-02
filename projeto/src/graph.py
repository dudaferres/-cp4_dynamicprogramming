class Graph:
    def __init__(self):
        self.adj = {}  # Dicionário de listas de adjacência

    def add_edge(self, origem: str, destino: str, custo: float, capacidade: int):

        # Se o nó de origem não existe, inicializa sua lista de adjacências
        if origem not in self.adj:
            self.adj[origem] = []

        # Adiciona a tupla (destino, custo, capacidade) à lista do nó de origem
        self.adj[origem].append((destino, custo, capacidade))

    def get_neighbors(self, node: str):
        # Retorna a lista de adjacências do nó, ou lista vazia se não existir
        return self.adj.get(node, [])