from sqlalchemy import create_engine, text
import pandas as pd

# install.py — script auxiliar para demonstrar uso do SQLAlchemy + SQLite
# Resumo: cria um banco local (teste_local.db), cria/insere dados em uma
# tabela de exemplo e executa uma query de teste. Comentários são curtos
# por se tratar de material de aula.

# Cria engine apontando para um arquivo SQLite local (teste_local.db)
# Observação: o caminho é relativo ao diretório de execução do script.
engine = create_engine("sqlite:///teste_local.db")
conn = engine.connect()

# --- Cria a tabela 'fifanova' caso não exista ---
# Uso de text() para enviar SQL bruto via SQLAlchemy
conn.execute(text("""
    CREATE TABLE IF NOT EXISTS fifanova (
        Name TEXT,
        Nationality TEXT,
        Overall INTEGER,
        Potential INTEGER
    )
"""))

# --- Insere algumas linhas de exemplo ---
# Inserção direta com valores estáticos para facilitar a demonstração
conn.execute(text("""
    INSERT INTO fifanova VALUES 
    ('Messi', 'Argentina', 91, 91),
    ('Neymar', 'Brazil', 89, 89),
    ('Vinicius Jr', 'Brazil', 86, 92),
    ('Rodrygo', 'Brazil', 82, 88)
"""))

# Confirma as alterações no banco (commit)
conn.commit()

# --- Query de teste: seleciona jogadores com Potential > 88 ---
# pd.read_sql converte o resultado SQL em DataFrame pandas
query = text("SELECT * FROM fifanova WHERE Potential > 88")
df = pd.read_sql(query, conn)
print(df)

# Fecha a conexão para liberar recursos
conn.close()