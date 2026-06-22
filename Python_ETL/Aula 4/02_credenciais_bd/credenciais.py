# ============================================================
#  AULA 4 — BLOCO 2: Credenciais para Banco de Dados
# ============================================================
#
#  O QUE VAMOS APRENDER:
#  ✅ O que são credenciais de banco de dados
#  ✅ Como organizar em um dicionário Python
#  ✅ Como montar a string de conexão
#  ✅ Como conectar usando SQLAlchemy
#
# ============================================================

from sqlalchemy import create_engine, text

# ────────────────────────────────────────────────────────────
#  PASSO 1 — As 5 credenciais necessárias
# ────────────────────────────────────────────────────────────
#
#  Para acessar qualquer banco de dados precisamos de:
#
#  hostname → endereço do servidor  (onde o banco mora)
#  username → nome do usuário       (quem está entrando)
#  password → senha do usuário      (prova de identidade)
#  port     → porta de entrada      (MySQL sempre usa 3306)
#  database → nome do banco         (qual banco dentro do servidor)
#
#  Analogia:
#  hostname = endereço do prédio
#  port     = número do apartamento
#  database = qual cômodo você quer
#  username = seu nome
#  password = sua chave

credenciais = {
    "hostname": "localhost",        # endereço do servidor
    "username": "aluno",            # usuário
    "password": "harve123",         # senha
    "port":      3306,               # porta padrão do MySQL
    "database":  "moduloetl",       # nome do banco
}

# ────────────────────────────────────────────────────────────
#  PASSO 2 — Montando a String de Conexão
# ────────────────────────────────────────────────────────────
#
#  O SQLAlchemy precisa das credenciais num formato específico:
#
#  mysql+pymysql:// USUARIO : SENHA @ HOST : PORTA / BANCO
#  ──────────────── ──────── ─────── ────── ──────── ──────
#       driver        login   senha  servidor porta   banco
#
#  No nosso caso com SQLite (banco local, sem servidor):
#
#  sqlite:///nome_do_arquivo.db
#  ────────────────────────────
#  mais simples: sem usuário, senha ou porta
#  o arquivo é criado automaticamente na pasta

STRING_DE_CONEXAO = "sqlite:///harve_escola.db"


def get_mysql_connection_string(credentials):
    return (
        f"mysql+pymysql://{credentials['username']}:{credentials['password']}@"
        f"{credentials['hostname']}:{credentials['port']}/{credentials['database']}"
    )


def get_sqlite_connection_string(db_filename="harve_escola.db"):
    return f"sqlite:///{db_filename}"


# ────────────────────────────────────────────────────────────
#  PASSO 3 — Criando o engine e abrindo a conexão
# ────────────────────────────────────────────────────────────
#
#  O SQLAlchemy funciona em duas camadas:
#  - engine: prepara a comunicação com o tipo de banco
#  - connection: abre a conexão real com o banco
#
#  A função create_engine() não se conecta ainda, ela apenas cria
#  o motor que sabe falar com SQLite ou MySQL.
#
#  O método .connect() do engine abre a conexão de verdade.
#  É como ligar o carro depois de entrar nele.
#
#  Depois de usar a conexão, sempre precisamos fechá-la com close()
#  para liberar recursos e evitar que o banco fique preso.
#
#  No exemplo abaixo, só testamos a conexão com SELECT 1,
#  que não acessa dados reais — apenas confirma que o banco responde.
#

if __name__ == "__main__":
    print("=" * 50)
    print("  CREDENCIAIS CONFIGURADAS")
    print("=" * 50)
    for chave, valor in credenciais.items():
        # Oculta a senha no print por segurança
        exibir = "****" if chave == "password" else valor
        print(f"  {chave:10} → {exibir}")
    print()

    print("  STRING DE CONEXÃO:")
    print(f"  {STRING_DE_CONEXAO}")
    print()
    print("  💡 SQLite = banco local, arquivo no seu computador")
    print("     Não precisa de servidor, usuário ou senha")
    print()

    print("=" * 50)
    print("  TESTANDO CONEXÃO...")
    print("=" * 50)

    try:
        engine = create_engine(STRING_DE_CONEXAO)
        conn = engine.connect()
        conn.execute(text("SELECT 1"))

        print("  ✅ Engine criado com sucesso!")
        print("  ✅ Conexão estabelecida!")
        print("  ✅ Banco respondendo!")
        print()
        print("  📁 Arquivo criado: harve_escola.db")

    except Exception as erro:
        print(f"  ❌ Erro: {erro}")
        conn = None

    finally:
        if conn:
            conn.close()
            print()
            print("  🔒 Conexão fechada.")

    print()
    print("=" * 50)
    print("  RESUMO")
    print("=" * 50)
    print("  1. Credenciais  → 5 informações para acessar o banco")
    print("  2. String       → formato que o SQLAlchemy entende")
    print("  3. Engine       → motor de conexão")
    print("  4. connect()    → abre a conexão")
    print("  5. close()      → fecha a conexão (sempre!)")
