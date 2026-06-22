import pandas as pd
from datetime import datetime

# testeDesafio1.py — pequeno script de teste para carregar os chamados
# Lê o CSV de chamados e converte a coluna de data para tipo datetime
# Comentários curtos (1-2 linhas) por ser material de aula

# Carrega arquivo CSV com dados de chamados (caminho relativo/absoluto usado no exercício)
df = pd.read_csv("/Aula 3/chamados.csv")

# Converte a coluna 'data_abertura' para tipo datetime para operações temporais
df["data_abertura"] = pd.to_datetime(df["data_abertura"])

