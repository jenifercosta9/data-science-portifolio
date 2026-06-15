import streamlit as st
import joblib
import plotly.express as px
import pandas as pd
import plotly.io as pio
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "recomendador_ceaps.sav"

modelo = joblib.load(model_path)

similaridade_df = modelo["similaridade"]
matriz_interacoes = modelo["matriz"]

# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(page_title="CEAPS Dashboard", layout="wide")
pio.templates.default = "plotly_dark"

st.title("📊 CEAPS — Sistema de Recomendação de Senadores")

# =========================
# INPUT
# =========================
senador = st.text_input("🔎 Digite o nome do senador")

# =========================
# SESSION STATE
# =========================
if "data" not in st.session_state:
    st.session_state.data = None


# =========================
# FUNÇÃO DO MODELO
# =========================
def recomendar_senadores(nome_senador, top_n=5):

    if nome_senador not in similaridade_df.index:
        raise KeyError(f"Senador '{nome_senador}' não encontrado.")

    serie = similaridade_df[nome_senador]

    similares = (
        serie.sort_values(ascending=False)
        .iloc[1:top_n+1]
    )

    senadores_similares = similares.index.tolist()

    despesas_media = (
        matriz_interacoes.loc[senadores_similares]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    return {
        "input": nome_senador,
        "similares": [
            {"senador": s, "similaridade": float(similares[s])}
            for s in senadores_similares
        ],
        "top_despesas": [
            {"tipo_despesa": d, "valor_medio": float(v)}
            for d, v in despesas_media.items()
        ]
    }

# =========================
# CHAMADA API
# =========================
if st.button("Analisar senador"):

    if not senador.strip():
        st.warning("Digite um nome válido")

    else:
        try:
            st.session_state.data = recomendar_senadores(senador)

        except KeyError as e:
            st.error(str(e))

# =========================
# EXIBIÇÃO
# =========================
if st.session_state.data is not None:

    data = st.session_state.data

    # =========================
    # DATAFRAMES (GARANTIDO)
    # =========================
    df_sim = pd.DataFrame(data["similares"]).rename(columns={"senador": "nome"})
    df_desp = pd.DataFrame(data["top_despesas"])

    # =========================
    # MÉTRICAS
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Senadores similares", len(df_sim))

    with col2:
        st.metric("Tipos de despesa", len(df_desp))

    with col3:
        st.metric("Maior similaridade", round(df_sim["similaridade"].max(), 2))

    st.markdown("---")

    # =========================
    # GRÁFICO 1 - SIMILARES
    # =========================
    st.subheader("🏆 Senadores mais similares")

    fig1 = px.bar(
        df_sim,
        x="similaridade",
        y="nome",
        orientation="h",
        color="similaridade",
        color_continuous_scale="Viridis"
    )

    fig1.update_layout(height=450)

    st.plotly_chart(fig1, use_container_width=True)

    # =========================
    # GRÁFICO 2 - PERFIL DO GRUPO
    # =========================
    st.subheader("📊 Senador vs Grupo Similar (Despesas)")

    df_group = df_desp.copy()
    df_group["perfil"] = "Grupo Similar"
    df_group["valor"] = df_group["valor_medio"]

    df_senador = df_desp.copy()
    df_senador["perfil"] = "Senador"
    df_senador["valor"] = df_senador["valor_medio"]

    df_comp = pd.concat([df_group, df_senador])

    fig2 = px.bar(
        df_comp.sort_values("valor", ascending=True),
        x="valor",
        y="tipo_despesa",
        color="perfil",
        barmode="group",
        orientation="h",
        color_discrete_sequence=["#FF4B4B", "#1F77B4"]
    )

    fig2.update_layout(height=550, margin=dict(l=180, r=20, t=30, b=20))

    st.plotly_chart(fig2, use_container_width=True)

    # =========================
    # GRÁFICO 3 - DIFERENÇA (CORRIGIDO E SEGURO)
    # =========================
    st.subheader("⚖️ Onde o senador se diferencia do grupo similar")

    df_diff = df_desp.copy()

    baseline = df_diff["valor_medio"].median()

    df_diff["desvio"] = (df_diff["valor_medio"] - baseline) / baseline

    fig3 = px.bar(
        df_diff.sort_values("desvio", ascending=True),
        x="desvio",
        y="tipo_despesa",
        orientation="h",
        text="desvio",
        color_discrete_sequence=["#00E5FF"]
    )

    fig3.update_traces(
        marker_line_color="white",
        marker_line_width=1.5,
        opacity=0.95
    )

    fig3.update_layout(
        height=500,
        margin=dict(l=200, r=20, t=30, b=20),
        xaxis_title="Desvio relativo ao padrão do grupo"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # =========================
    # DEBUG
    # =========================
    with st.expander("📋 Dados brutos da API"):
        st.json(data)
