# Importações necessárias
import heapq  # Biblioteca para implementação de fila de prioridade (heap)
from src.decorators import measure_performance  # Decorador para medir o desempenho da função

@measure_performance  # Aplica o decorador para medir tempo de execução e uso de memória
def dijkstra(graph, start: str, end: str) -> tuple:
    # Inicializa a fila de prioridade com o nó de início: (custo acumulado, nó atual, caminho percorrido)
    # O custo inicial é 0, e o caminho começa vazio
    queue = [(0, start, [])]

    # Conjunto para rastrear nós já visitados, evitando reprocessamento
    visited = set()

    # Loop principal: continua enquanto houver nós na fila
    while queue:
        # Remove o nó com menor custo da fila (graças ao heap)
        cost, node, path = heapq.heappop(queue)

        # Se o nó já foi visitado, pula para o próximo (evita duplicatas)
        if node in visited:
            continue

        # Adiciona o nó atual ao caminho percorrido
        path = path + [node]

        # Marca o nó como visitado
        visited.add(node)

        # Se chegamos ao nó de destino, retorna o custo e o caminho
        if node == end:
            return cost, path

        # Explora os vizinhos do nó atual
        for neighbor, weight, _ in graph.get_neighbors(node):
            # Adiciona o vizinho à fila com o custo atualizado (custo acumulado + peso da aresta)
            # O caminho permanece o mesmo até agora
            heapq.heappush(queue, (cost + weight, neighbor, path))

    # Se a fila esvaziar sem encontrar o destino, retorna infinito e caminho vazio
    return float('inf'), []