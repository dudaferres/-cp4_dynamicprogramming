# Importações necessárias
from functools import wraps  # Preserva metadados da função decorada (como __name__ e __doc__)
import time  # Para medição precisa de tempo de execução
import tracemalloc  # Para rastreamento de uso de memória


def measure_performance(func):
    @wraps(func)  # Preserva __name__, __doc__, etc., da função original
    def wrapper(*args, **kwargs):
        # Inicia o rastreamento de memória antes da execução
        tracemalloc.start()

        # Registra o tempo de início com alta precisão
        start = time.perf_counter()

        # Executa a função original com os argumentos fornecidos
        result = func(*args, **kwargs)

        # Registra o tempo de fim após a execução
        end = time.perf_counter()

        # Obtém o uso de memória: atual (current) e pico (peak)
        current, peak = tracemalloc.get_traced_memory()

        # Para o rastreamento de memória para liberar recursos
        tracemalloc.stop()

        # Imprime as métricas de desempenho no console
        print(f"\n[PERFORMANCE] {func.__name__}")  # Nome da função para identificação
        print(f"Tempo: {(end - start):.6f}s")  # Tempo em segundos com 6 casas decimais
        print(f"Memória atual: {current / 1024:.2f} KB")  # Memória atual em KB
        print(f"Memória pico: {peak / 1024:.2f} KB")  # Memória pico em KB

        # Retorna o resultado da função original
        return result

    # Retorna a função wrapper (que será usada no lugar da original)
    return wrapper