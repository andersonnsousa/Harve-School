# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 3: Tratando Conteúdos DataFrame
# =============================================================================
#  EXERCÍCIO 7 — Descobrir o dia com maior velocidade do vento
#
# Objetivo: Crie um código que descobre qual é o dia da semana em que
#           a velocidade do vento estará mais alta.
#
# Dicas:
#   - A coluna vel_vento pode vir como string, ex: '15 km/h'
#   - Use str.extract(r'(\d+\.?\d*)') para extrair apenas o número
#   - Converta para float com .astype(float)
#   - Use .idxmax() para encontrar o índice do maior valor
#   - Acesse o nome do dia com df.loc[idx, 'dia_semana']
# =============================================================================

import requests
import pandas as pd

# Setup: carrega e renomeia o DataFrame
url_clima = 'https://api.hgbrasil.com/weather?key=3b9b39d6&city_name=Sao%20Paulo'
dados_clima = requests.get(url_clima).json()
previsoes = dados_clima['results']['forecast']
df_clima = pd.DataFrame(previsoes)

df_clima_pt = df_clima.copy()

# Mapeamento para nomes em português (aplicar apenas às colunas presentes)
mapping = {
    'date': 'data',
    'weekday': 'dia_semana',
    'max': 'temp_max',
    'min': 'temp_min',
    'cloudiness': 'nebulosidade',
    'rain': 'chuva',
    'rain_probability': 'prob_chuva',
    'wind_speedy': 'vel_vento',
    'description': 'descricao',
    'condition': 'condicao'
}

# Preservar a ordem desejada e selecionar apenas colunas existentes
desired = list(mapping.keys())
present = [c for c in desired if c in df_clima_pt.columns]
if not present:
    raise ValueError('Nenhuma das colunas esperadas foi encontrada em df_clima')

df_clima_pt = df_clima_pt[present].copy()
df_clima_pt.columns = [mapping[c] for c in present]

# Seu código aqui:


# =============================================================================
#  RESOLUÇÃO 7
# =============================================================================

# A coluna vel_vento pode vir como string tipo '15 km/h'
# Extraímos só o número com str.extract
df_clima_pt['vel_vento_num'] = (
    df_clima_pt['vel_vento']
    .str.extract(r'(\d+\.?\d*)')
    .astype(float)
)

idx_max_vento  = df_clima_pt['vel_vento_num'].idxmax()
dia_max_vento  = df_clima_pt.loc[idx_max_vento, 'dia_semana']
data_max_vento = df_clima_pt.loc[idx_max_vento, 'data']
vel_max        = df_clima_pt.loc[idx_max_vento, 'vel_vento']

print(f'  Dia com maior vento: {dia_max_vento}')
print(f'  Data: {data_max_vento}')
print(f'  Velocidade: {vel_max}')
