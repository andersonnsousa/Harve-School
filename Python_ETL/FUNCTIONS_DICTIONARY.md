# Dicionário de Funções (curto)

Este arquivo lista funções e métodos usados nos materiais de aula com uma breve descrição.

- `pandas.read_csv(path)`: carrega um CSV em um `DataFrame`.
- `pd.to_datetime(series)`: converte uma série para tipo `datetime` do pandas.
- `DataFrame.to_csv(path, index=False)`: exporta um `DataFrame` para CSV; `index=False` evita coluna de índice.
- `DataFrame.to_sql(name, con, if_exists, index=False)`: grava um `DataFrame` em uma tabela de banco via SQLAlchemy.
- `pd.read_sql(query, conn)`: executa uma query SQL e retorna um `DataFrame`.
- `create_engine(conn_string)`: cria o motor (engine) de conexão do SQLAlchemy.
- `engine.connect()`: abre a conexão com o banco (retorna `Connection`).
- `conn.commit()`: confirma (commit) mudanças em operações de escrita no banco.
- `conn.close()`: fecha a conexão com o banco, liberando recursos.
- `requests.get(url)`: faz requisição HTTP e retorna o objeto `Response`.
- `response.json()`: converte o corpo da resposta HTTP para dicionário Python (se JSON).
- `datetime.now()`: retorna data/hora atual (objeto `datetime`).
- `timedelta(days=n)`: cria um intervalo de tempo para somar/subtrair datas.
- `datetime.timestamp()`: converte `datetime` para timestamp (segundos desde epoch).
- `datetime.strftime(fmt)`: formata `datetime` como string com o formato `fmt`.
- `Series.str.extract(regex)`: extrai conteúdo de strings usando regex (útil p/ números em texto).
- `round(series.astype(float), 0)`: converte para float e arredonda valores (ex.: chuva).
- `input(prompt)`: lê entrada do usuário pelo terminal.
- `print(...)`: exibe texto/objetos no terminal — uso didático nos exercícios.

Se quiser que eu adicione outras funções específicas, diga quais e atualizo o dicionário.
