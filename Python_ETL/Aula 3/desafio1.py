import pandas as pd
from datetime import datetime

# desafio1.py — exemplo de análise simples de chamados (material de aula)
# Objetivo: identificar chamados abertos há mais de 3 dias e destacar urgências

# 1) Carrega os chamados do CSV e normaliza a coluna de datas
df = pd.read_csv("/Aula 3/chamados.csv")
df["data_abertura"] = pd.to_datetime(df["data_abertura"])

# 2) Filtra apenas os chamados com status 'aberto'
abertos = df[df["status"] == "aberto"].copy()

# 3) Calcula quantos dias cada chamado está aberto (coluna inteira de dias)
abertos["dias_aberto"] = (datetime.now() - abertos["data_abertura"]).dt.days

# 4) Seleciona chamados com mais de 3 dias em aberto
atrasados = abertos[abertos["dias_aberto"] > 3]

print(f"Chamados em aberto há mais de 3 dias: {len(atrasados)}\n")

# 5) Imprime cada chamado atrasado, marcando nível por prioridade
for _, row in atrasados.iterrows():
    if row["prioridade"] == "alta":
        nivel = "URGENTE"
    else:
        nivel = "atenção"

    print(f"[{nivel}] ID {int(row['id'])} | {row['cliente']} | {int(row['dias_aberto'])} dias | prioridade: {row['prioridade']}")

# 6) Mostra o chamado mais antigo e o total de abertos
mais_antigo = abertos.loc[abertos["dias_aberto"].idxmax()]
print(f"\nChamado mais antigo: ID {int(mais_antigo['id'])} — {mais_antigo['cliente']} ({int(mais_antigo['dias_aberto'])} dias)")
print(f"Total de chamados abertos: {len(abertos)}")