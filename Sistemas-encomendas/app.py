import streamlit as st
from pedidos import contar_pedidos, contar_pendentes, contar_entregues
from pedidos import adicionar_pedido
from database import criar_tabela
from pedidos import listar_pedidos
import pandas as pd
from pedidos import listar_pedidos, marcar_entregue
from pedidos import excluir_pedido


# Inicializa a base caso ainda não exista.
criar_tabela()

st.title("📦 Sistemas de Encomendas")

# Menu principal lateral.
menu = st.sidebar.selectbox(
     "Menu",
     ["Dashboard", "Novo pedido", "Ver pedidos"] 

     )

# Tela de resumo com metricas gerais.
if menu == "Dashboard":
    st.subheader("Resumo")

    total = contar_pedidos()
    pendentes = contar_pendentes()
    entregues = contar_entregues()


    col1, col2, col3 = st.columns(3)
    col1.metric("pedidos", total )
    col2.metric("pendentes", pendentes )
    col3.metric("Entregues", entregues )

# Formulario para cadastrar um novo pedido.
if menu == "Novo pedido":
    st.subheader("Cadastrar pedido")

    cliente = st.text_input("Cliente")
    produto = st.text_input("Produto")
    quantidade = st.number_input("Quantidade", step=1, min_value=1)

    if st.button("Salvar"):
        adicionar_pedido(cliente, produto, quantidade)
        st.success("Pedido cadastrado!")

# Listagem com ações de entrega e exclusão.
if menu == "Ver pedidos":
    st.subheader("Lista de pedidos")
    pedidos = listar_pedidos()

    for pedido in pedidos:
        id_pedido = pedido[0]
        cliente = pedido[1]
        produto = pedido[2]
        quantidade = pedido[3]
        status = pedido[4]

        col1, col2, col3, col4, col5, col6 = st.columns(6)

        col1.write(id_pedido)
        col2.write(cliente)
        col3.write(produto)
        col4.write(quantidade)
        col5.write(status)

        # Mostra botão de entrega apenas quando esta pendente.
        if status == "pendente":
            if col6.button("Marcar como entregue", key=id_pedido):
                marcar_entregue(id_pedido)
                st.success("Pedido atualizado!")
                st.rerun()

        # Ação de exclusão por linha.
        if col6.button("Excluir pedido", key=f"excluir_{id_pedido}"):
            excluir_pedido(id_pedido)
            st.success("Pedido excluído!")
            st.rerun()
