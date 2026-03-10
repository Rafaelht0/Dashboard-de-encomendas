from database import conectar

def adicionar_pedido(cliente, produto, quantidade):
    conn =  conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO pedidos (cliente, produto, quantidade, status) VALUES (?, ?, ?, 'pendente')""", (cliente, produto, quantidade))
    conn.commit()
    conn.close()

def contar_pedidos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def contar_pendentes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'pendente'")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def contar_entregues():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'entregue'")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def listar_pedidos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos")

    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

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

def excluir_pedido(id_pedido):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                    DELETE FROM pedidos
                    WHERE id = ?
                    """, (id_pedido,))
        
    conn.commit()
    conn.close()