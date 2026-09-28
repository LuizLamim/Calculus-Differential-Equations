import sqlite3

def criar_banco():
    # Conecta ao banco de dados (se não existir, ele será criado automaticamente)
    conexao = sqlite3.connect("pessoas.db")
    cursor = conexao.cursor()
    
    # Cria a tabela se ela ainda não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)
    
    conexao.commit()
    conexao.close()

def inserir_pessoa(nome, idade):
    # Conecta ao banco de dados
    conexao = sqlite3.connect("pessoas.db")
    cursor = conexao.cursor()
    
    # Insere os dados usando parâmetros para evitar SQL Injection
    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
    
    conexao.commit()
    conexao.close()
    print(f"Sucesso! {nome}, de {idade} anos, foi cadastrado(a) no banco de dados.")