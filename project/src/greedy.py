# Importação necessária
from src.decorators import measure_performance  # Decorador para medir desempenho da função

@measure_performance  # Aplica medição de tempo e memória à execução
def greedy_route(graph, start: str, end: str) -> dict:
    # Inicializa o nó atual como o início
    current = start

    # Lista para armazenar o caminho percorrido
    path = [current]

    # Acumulador para o custo total
    total_cost = 0

    # Loop até chegar ao destino
    while current != end:
        # Obtém os vizinhos do nó atual
        neighbors = graph.get_neighbors(current)

        # Se não há vizinhos, caminho impossível (retorna inf e caminho vazio)
        if not neighbors:
            return {'cost': float('inf'), 'path': []}

        # Escolha gulosa: seleciona o vizinho com menor custo (x[1] é o custo na tupla)
        next_node = min(neighbors, key=lambda x: x[1])

        # Adiciona o custo da aresta escolhida ao total
        total_cost += next_node[1]

        # Move para o próximo nó
        current = next_node[0]

        # Adiciona o nó ao caminho
        path.append(current)

    # Retorna o resultado: custo total e caminho
    return {'cost': total_cost, 'path': path}