# Importações necessárias
from functools import lru_cache  # Decorador para memoização automática, evitando recálculos
from src.decorators import measure_performance  # Decorador para medir desempenho da função


@lru_cache(maxsize=None)  # Cache ilimitado para armazenar resultados de subproblemas
def allocate_load_dp(capacidades: tuple, custos: tuple, carga: int) -> float:
    # Caso base: se a carga é zero, custo é zero
    if carga == 0:
        return 0

    # Caso base: se não há mais itens e ainda há carga, impossível (custo infinito)
    if not capacidades:
        return float('inf')

    # Pega o primeiro item: sua capacidade e custo
    capacidade = capacidades[0]
    custo = custos[0]

    # Inicializa o melhor custo como infinito
    melhor = float('inf')

    # Tenta alocar de 0 até o mínimo entre capacidade do item e carga restante
    for k in range(min(capacidade, carga) + 1):
        # Recursão: resolve para os itens restantes com carga reduzida
        sub = allocate_load_dp(capacidades[1:], custos[1:], carga - k)
        # Calcula o custo total: custo da recursão + custo da alocação atual
        melhor = min(melhor, sub + k * custo)

    # Retorna o melhor custo encontrado
    return melhor


@measure_performance  # Aplica medição de desempenho à função wrapper
def run_dp(capacidades, custos, carga):
    # Converte para tuplas se forem listas (para compatibilidade com lru_cache)
    if isinstance(capacidades, list):
        capacidades = tuple(capacidades)
    if isinstance(custos, list):
        custos = tuple(custos)

    # Chama a função DP com memoização
    return allocate_load_dp(capacidades, custos, carga)