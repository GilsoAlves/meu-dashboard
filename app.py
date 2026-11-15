import streamlit as st
import pandas as pd


st.set_page_config(page_title="dashboard", layout="wide")

st.title("Meu primeiro Dasboard")

dados = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar","Abr", "Mai", "Jun" ],
    "Vendas" : [12000, 15000, 13000, 18000, 21000, 19000],
    "Meta" : [15000, 15000, 15000, 15000, 15000, 15000]
})

ordem = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
dados["Mês"] = pd.Categorical(dados["Mês"], categories=ordem, ordered=True)
dados = dados.sort_values("Mês")

def formatar(valor):
    return f"R$ {valor:,.of}".replace(",", ".")

total = int(dados["Vendas"].sum())
media = int(dados["Vendas"].mean())
melhor = dados.loc[dados["Vendas"].idxmax(), "Mês"]

col1, col2, col3 = st.columns(3)
col1.metric("Total Vendas", f"R$ {total:,.0f}".replace(",", "."))
col2.metric("Média Mensal", f"R$ {media:,.0f}".replace(",", "."))
col3.metric("Melhor Mês", melhor)

st.subheader("Vendas vs Meta")
st.bar_chart(dados.set_index("Mês"))

st.subheader("Tabela de dados")
st.dataframe(dados, use_container_width=True)


