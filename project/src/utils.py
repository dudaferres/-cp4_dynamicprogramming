# Importação necessária
import pandas as pd  # Biblioteca para manipulação de dados tabulares (DataFrames)

def load_data(path: str) -> pd.DataFrame:
    # Lê o arquivo CSV em um DataFrame
    df = pd.read_csv(path)

    # Remove linhas duplicadas para evitar processamento redundante
    df.drop_duplicates(inplace=True)

    # Preenche valores nulos com 0 (tratamento simples; pode ser ajustado)
    df.fillna(0, inplace=True)

    # Retorna o DataFrame limpo
    return df

def cost_function(row, w_custo=1, w_risco=10, w_perda=5) -> float:
    # Calcula o custo total somando os componentes ponderados
    return (
        row['custo_reais'] * w_custo +      # Contribuição do custo monetário
        row['risco_atraso'] * w_risco +     # Contribuição do risco de atraso
        row['perda_percentual'] * w_perda   # Contribuição da perda percentual
    )