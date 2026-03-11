import sqlite3

# Abre conexão com o banco local.
def conectar():
    return sqlite3.connect('encomendas.db')

# Garante que a tabela principal exista antes de usar o app.
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Cliente TEXT NOT NULL,
                   Produto TEXT NOT NULL,
                   Quantidade INTEGER,
                   status text
                   )
                   """)
    
    conn.commit()
    conn.close()
    
