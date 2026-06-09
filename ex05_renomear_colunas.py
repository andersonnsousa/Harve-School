# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 2: Identificando Colunas
# =============================================================================
#  EXERCÍCIO 5 — Renomear colunas do DataFrame de previsão do tempo
#
# Objetivo: Traduza as colunas do DataFrame da previsão do tempo para português.
#
# Colunas originais (em ordem):
#   date, weekday, max, min, cloudiness, rain, rain_probability,
#   wind_speedy, description, condition
#
# Sugestão de nomes em português:
#   date             → 'data'
#   weekday          → 'dia_semana'
#   max              → 'temp_max'
#   min              → 'temp_min'
#   cloudiness       → 'nebulosidade'
#   rain             → 'chuva'
#   rain_probability → 'prob_chuva'
#   wind_speedy      → 'vel_vento'
#   description      → 'descricao'
#   condition        → 'condicao'
#
# Dicas:
#   - Crie uma cópia do df_clima com .copy() e chame de df_clima_pt
#   - Use df.columns = [lista de nomes] para renomear todas de uma vez
#   - Exiba o resultado com .head()
# =============================================================================

import requests
import pandas as pd

# Setup: carrega os dados do clima
url_clima = 'https://api.hgbrasil.com/weather?key=3b9b39d6&city_name=Sao%20Paulo'
resposta_clima = requests.get(url_clima)
dados_clima = resposta_clima.json()
previsoes = dados_clima['results']['forecast']
df_clima = pd.DataFrame(previsoes)

print('Colunas originais:', list(df_clima.columns))

# Seu código aqui:


# =============================================================================
#  RESOLUÇÃO 5
# =============================================================================

df_clima_pt = df_clima.copy()

# Mapeamento de nomes originais -> nomes em português
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

# Selecionar apenas as colunas esperadas que existem na resposta da API,
# preservando a ordem desejada
desired = list(mapping.keys())
present = [c for c in desired if c in df_clima_pt.columns]

if not present:
    raise ValueError('Nenhuma das colunas esperadas foi encontrada em df_clima')

df_clima_pt = df_clima_pt[present].copy()
df_clima_pt.columns = [mapping[c] for c in present]

print('Colunas renomeadas com sucesso!')
print(df_clima_pt.head())
