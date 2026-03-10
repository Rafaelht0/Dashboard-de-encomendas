import streamlit as st
from pedidos import contar_pedidos, contar_pendentes, contar_entregues
from pedidos import adicionar_pedido
from database import criar_tabela

criar_tabela()

st.title("📦 Sistemas de Encomendas")

menu = st.sidebar.selectbox(
     "Menu",
     ["Dashboard", "Novo pedido"] 

     )

if menu == "Dashboard":
    st.subheader("Resumo")

    total = contar_pedidos()
    pendentes = contar_pendentes()
    entregues = contar_entregues()


    col1, col2, col3 = st.columns(3)
    col1.metric("pedidos", total )
    col2.metric("pendentes", pendentes )
    col3.metric("Entregues", entregues )

if menu == "Novo pedido":
    st.subheader("Cadastrar pedido")

    cliente = st.text_input("Cliente")
    produto = st.text_input("Produto")
    quantidade = st.number_input("Quantidade", step=1, min_value=1)

    if st.button("Salvar"):
        adicionar_pedido(cliente, produto, quantidade)
        st.success("Pedido cadastrado!")

