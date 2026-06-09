# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 1: Transformando Data
# =============================================================================
#  EXERCÍCIO 3 — Convertendo datetime para timestamp em milissegundos
#
# Objetivo: Converta a data de 5 dias atrás para timestamp em milissegundos
#           (formato usado por APIs como Binance).
#
# Dicas:
#   - Calcule a data de 5 dias atrás com timedelta(5)
#   - Use strftime('%s') para obter os segundos como string
#   - Multiplique por 1000 (ou concatene '000') para obter milissegundos
#   - Converta o resultado para int
# =============================================================================

# Seu código aqui:


# =============================================================================
# RESOLUÇÃO 3
# =============================================================================

from datetime import datetime, timedelta

data_5_dias = datetime.now() - timedelta(5)
# Uso timestamp() para compatibilidade com Windows
timestamp_ms = int(data_5_dias.timestamp() * 1000)

print(f'Data (5 dias atrás):        {data_5_dias.strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Timestamp em milissegundos: {timestamp_ms}')
