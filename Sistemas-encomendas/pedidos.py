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