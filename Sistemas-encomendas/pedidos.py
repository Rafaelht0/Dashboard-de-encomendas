from database import conectar

# Insere um novo pedido com status inicial pendente.
def adicionar_pedido(cliente, produto, quantidade):
    conn =  conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO pedidos (cliente, produto, quantidade, status) VALUES (?, ?, ?, 'pendente')""", (cliente, produto, quantidade))
    conn.commit()
    conn.close()

# Conta todos os pedidos registrados.
def contar_pedidos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos")
    total = cursor.fetchone()[0]
    conn.close()
    return total

# Conta apenas pedidos com status pendente.
def contar_pendentes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'pendente'")
    total = cursor.fetchone()[0]
    conn.close()
    return total

# Conta apenas pedidos com status entregue.
def contar_entregues():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'entregue'")
    total = cursor.fetchone()[0]
    conn.close()
    return total

# Lista todos os pedidos na tabela.
def listar_pedidos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos")

    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

# Atualiza o status de um pedido para entregue.
def marcar_entregue(id_pedido):
    conn =  conectar()
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE pedidos
                   SET status = 'entregue'
                   WHERE id = ?
                   """, (id_pedido,))
    
    conn.commit()
    conn.close()

# Remove um pedido pelo id.
def excluir_pedido(id_pedido):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                    DELETE FROM pedidos
                    WHERE id = ?
                    """, (id_pedido,))
        
    conn.commit()
    conn.close()
