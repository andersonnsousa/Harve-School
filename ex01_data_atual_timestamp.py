# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 1: Transformando Data
# =============================================================================
#  EXERCÍCIO 1 — Data atual em timestamp
#
# Objetivo: Recupere a data e hora atual e exiba no formato datetime.
#
# Dicas:
#   - Importe datetime e timedelta do módulo datetime
#   - Recupere a data atual e armazene em uma variável chamada 'data_atual'
#   - Imprima o resultado
# =============================================================================

# Seu código aqui:


# =============================================================================
#  RESOLUÇÃO 1
# =============================================================================

from datetime import datetime, timedelta

data_atual = datetime.now()
print(f'Data e hora atual: {data_atual}')
