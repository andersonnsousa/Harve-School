# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 3: Tratando Conteúdos DataFrame
# =============================================================================
#  EXERCÍCIO 6 — Arredondar a coluna chuva
#
# Objetivo: Arredonde a coluna 'chuva' do df_clima_pt retirando
#           a casa decimal (0 casas decimais).
#
# Dicas:
#   - Verifique o tipo atual da coluna com .dtype
#   - Use round(df['coluna'].astype(float), 0) para converter e arredondar
#   - Atualize a coluna no df_clima_pt
#   - Compare o antes e o depois
# =============================================================================

import requests
import pandas as pd

# Setup: carrega e renomeia o DataFrame
url_clima = 'https://api.hgbrasil.com/weather?key=3b9b39d6&city_name=Sao%20Paulo'
dados_clima = requests.get(url_clima).json()
previsoes = dados_clima['results']['forecast']
df_clima = pd.DataFrame(previsoes)

df_clima_pt = df_clima.copy()
df_clima_pt = df_clima.copy()
# Algumas respostas podem incluir colunas extras; garantir que temos as 10 esperadas
if df_clima_pt.shape[1] >= 10:
    df_clima_pt = df_clima_pt.iloc[:, :10]
else:
    raise ValueError(f'Esperava ao menos 10 colunas em df_clima, encontrou {df_clima_pt.shape[1]}')

df_clima_pt.columns = [
    'data', 'dia_semana', 'temp_max', 'temp_min',
    'nebulosidade', 'chuva', 'prob_chuva',
    'vel_vento', 'descricao', 'condicao'
]

# Seu código aqui:


# =============================================================================
#  RESOLUÇÃO 6
# =============================================================================

print('Tipo antes:', df_clima_pt['chuva'].dtype)
print('Valores antes:\n', df_clima_pt['chuva'].head())

df_clima_pt['chuva'] = round(df_clima_pt['chuva'].astype(float), 0)

print('\nTipo depois:', df_clima_pt['chuva'].dtype)
print('Valores depois:\n', df_clima_pt['chuva'].head())
