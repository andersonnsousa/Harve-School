# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 4: Bootcamp (Desafio Final)
# =============================================================================
#  EXERCÍCIO 8 — Conversor Real → Dólar com input do usuário
#
# Objetivo: Usando a API financeira do HG Brasil, retorne a conversão de
#           hoje de real para dólar. Permita ao usuário digitar o valor
#           em reais via input() e imprima o valor convertido em dólar.
#
# API: https://api.hgbrasil.com/finance?key=3b9b39d6
#
# Navegação no JSON:
#   resposta['results']['currencies']['USD']['buy']  → taxa de compra do dólar
#
# Passos:
#   1. Faça a requisição na API HG Brasil
#   2. Extraia a taxa de compra do dólar (USD buy)
#   3. Peça ao usuário um valor em reais com input()
#   4. Calcule e imprima o valor equivalente em dólar
# =============================================================================

# Seu código aqui:


# =============================================================================
#  RESOLUÇÃO 8
# =============================================================================

import requests

# 1. Requisição à API
url = 'https://api.hgbrasil.com/finance?key=3b9b39d6'
resposta = requests.get(url).json()

# 2. Extrair taxa do dólar
taxa_dolar = resposta['results']['currencies']['USD']['buy']
print(f' Taxa de compra do dólar hoje: R$ {taxa_dolar}')

# 3. Input do usuário
valor_reais = float(input('\nDigite o valor em reais que deseja converter: R$ '))

# 4. Cálculo e resultado
# Para converter BRL → USD dividimos pelo valor do dólar
valor_dolares = valor_reais / taxa_dolar

print(f'\n R$ {valor_reais:.2f} equivale a US$ {valor_dolares:.2f}')
