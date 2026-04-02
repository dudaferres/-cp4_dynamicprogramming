# Importações necessárias para o funcionamento do programa
from src.graph import Graph  # Classe para representar o grafo
from src.utils import load_data, cost_function  # Funções utilitárias para carregar dados e calcular custos
from src.dijkstra import dijkstra  # Algoritmo de Dijkstra para encontrar o caminho mais curto
from src.greedy import greedy_route  # Algoritmo guloso para roteamento
from src.dynamic_programming import run_dp  # Algoritmo de programação dinâmica
import os  # Módulo para manipulação de caminhos de arquivos

# Definição de caminhos base para os dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório base do script
DATA_PATH = os.path.join(BASE_DIR, 'data', 'GS_FIAP_rotas_logisticas_DynProg_AM.csv')  # Caminho para o arquivo de dados CSV

def find_valid_pair(graph):
    """
    Encontra um par origem-destino com caminho válido no grafo.
    
    Itera sobre todos os pares possíveis de nós no grafo e verifica se existe um caminho
    entre eles usando o algoritmo de Dijkstra. Retorna o primeiro par válido encontrado.
    
    Args:
        graph (Graph): O grafo contendo os nós e arestas.
    
    Returns:
        tuple: Par (origem, destino) com caminho válido.
    
    Raises:
        Exception: Se nenhum caminho válido for encontrado.
    """
    for origem in graph.adj.keys():  # Itera sobre todos os nós de origem
        for destino in graph.adj.keys():  # Itera sobre todos os nós de destino
            if origem != destino:  # Garante que origem e destino sejam diferentes
                cost, path = dijkstra(graph, origem, destino)  # Calcula o caminho usando Dijkstra
                if path:  # Se um caminho foi encontrado
                    return origem, destino  # Retorna o par válido
    raise Exception("Nenhum caminho válido encontrado")  # Lança erro se nenhum par for encontrado

def run():
    """
    Função principal que executa o programa de roteamento logístico.
    
    Carrega os dados do CSV, permite ao usuário escolher um cenário, constrói o grafo,
    encontra um par origem-destino válido, executa os algoritmos (Dijkstra, Guloso, DP)
    e imprime os resultados.
    """
    df = load_data(DATA_PATH)  # Carrega os dados do arquivo CSV em um DataFrame

    scenario = input("Escolha o cenário (A, B, C): ").upper()  # Solicita ao usuário escolher um cenário

    if scenario not in ['A', 'B', 'C']:  # Valida a entrada do usuário
        raise ValueError("Cenário inválido!")

    df = df[df['scenario_id'] == scenario]  # Filtra o DataFrame para o cenário escolhido

    g = Graph()  # Cria uma instância do grafo

    # Adiciona arestas ao grafo com base nos dados filtrados
    for _, row in df.iterrows():  # Itera sobre cada linha do DataFrame
        custo = cost_function(row)  # Calcula o custo da aresta usando a função utilitária
        g.add_edge(row['origem'], row['destino'], custo, int(row['capacidade_ton']))  # Adiciona a aresta ao grafo

    origem, destino = find_valid_pair(g)  # Encontra um par origem-destino válido

    # Executa os algoritmos
    d_cost, d_path = dijkstra(g, origem, destino)  # Dijkstra para caminho mais curto
    g_res = greedy_route(g, origem, destino)  # Algoritmo guloso

    # Prepara dados para o algoritmo de programação dinâmica
    neighbors = g.get_neighbors(origem)  # Obtém os vizinhos do nó de origem
    capacidades = tuple(int(n[2]) for n in neighbors)  # Extrai as capacidades dos vizinhos
    custos = tuple(n[1] for n in neighbors)  # Extrai os custos dos vizinhos

    dp_cost = run_dp(capacidades, custos, 10)  # Executa o DP com capacidade máxima de 10

    # Imprime os resultados
    print("\n=== RESULTADOS ===")
    print("Cenário:", scenario)
    print("Origem:", origem)
    print("Destino:", destino)
    print("Dijkstra:", d_path, d_cost)
    print("Greedy:", g_res)
    print("DP:", dp_cost)

# Bloco principal: executa a função run se o script for chamado diretamente
if __name__ == '__main__':
    run()