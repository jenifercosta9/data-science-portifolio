import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Executive Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dicionário de tradução completo
languages = {
    "Português": {
        "sidebar_header": "🔍 Filtros",
        "lang_label": "Idioma",
        "date_label": "Período",
        "region_label": "Região",
        "cat_label": "Categoria",
        "city_label": "Cidade (Top 20)",
        "all_opt": "Todas",
        "header_title": "📊 Executive Sales Dashboard - Iowa Liquor Sales",
        "kpi_rev": "💰 Receita Total",
        "kpi_profit": "📈 Lucro Total",
        "kpi_margin": "🎯 Margem Média",
        "kpi_sales": "🛒 Vendas",
        "kpi_ticket": "💳 Ticket Médio",
        "delta_total": "do total",
        "delta_margin": "margem",
        "chart_evol_title": "📅 Evolução da Receita ao Longo do Tempo",
        "chart_evol_y": "Receita Diária",
        "chart_cat_title": "🥧 Distribuição de Receita por Categoria",
        "chart_cat_sub": "Top 10 Categorias",
        "chart_prod_title": "🏆 Top 10 Produtos por Receita",
        "chart_prod_sub": "Produtos Mais Vendidos",
        "chart_reg_title": "🌍 Performance por Região",
        "chart_reg_sub": "Top 10 Regiões - Receita e Lucro",
        "chart_supp_title": "👥 Top 10 Fornecedores",
        "chart_supp_sub": "Receita por Fornecedor",
        "chart_city_title": "🏙️ Top 10 Cidades",
        "chart_city_sub": "Receita por Cidade",
        "tab_title": "📋 Análise Detalhada por Produto",
        "col_prod": "Produto",
        "col_rev": "Receita",
        "col_profit": "Lucro",
        "col_qty": "Qtd Vendida",
        "col_avg_margin": "Margem Média (%)",
        "col_avg_price": "Preço Médio",
        "footer_dev": "Desenvolvido para análise de vendas de bebidas em Iowa",
        "footer_data": "Dados: Iowa Liquor Sales | Período:"
    },
    "English": {
        "sidebar_header": "🔍 Filters",
        "lang_label": "Language",
        "date_label": "Date Range",
        "region_label": "Region",
        "cat_label": "Category",
        "city_label": "City (Top 20)",
        "all_opt": "All",
        "header_title": "📊 Executive Sales Dashboard - Iowa Liquor Sales",
        "kpi_rev": "💰 Total Revenue",
        "kpi_profit": "📈 Total Profit",
        "kpi_margin": "🎯 Average Margin",
        "kpi_sales": "🛒 Sales",
        "kpi_ticket": "💳 Avg Ticket",
        "delta_total": "of total",
        "delta_margin": "margin",
        "chart_evol_title": "📅 Revenue Evolution Over Time",
        "chart_evol_y": "Daily Revenue",
        "chart_cat_title": "🥧 Revenue Distribution by Category",
        "chart_cat_sub": "Top 10 Categories",
        "chart_prod_title": "🏆 Top 10 Products by Revenue",
        "chart_prod_sub": "Best Selling Products",
        "chart_reg_title": "🌍 Performance by Region",
        "chart_reg_sub": "Top 10 Regions - Revenue and Profit",
        "chart_supp_title": "👥 Top 10 Suppliers",
        "chart_supp_sub": "Revenue by Supplier",
        "chart_city_title": "🏙️ Top 10 Cities",
        "chart_city_sub": "Revenue by City",
        "tab_title": "📋 Detailed Product Analysis",
        "col_prod": "Product",
        "col_rev": "Revenue",
        "col_profit": "Profit",
        "col_qty": "Qty Sold",
        "col_avg_margin": "Avg Margin (%)",
        "col_avg_price": "Avg Price",
        "footer_dev": "Developed for Iowa Liquor Sales analysis",
        "footer_data": "Data: Iowa Liquor Sales | Period:"
    }
}

# Estilo customizado
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/processed/sales_data_processed.csv')
        df['data_venda'] = pd.to_datetime(df['data_venda'])
        return df
    except FileNotFoundError:
        st.error("⚠️ Arquivo não encontrado.")
        st.stop()

df = load_data()

# ============================================================
# SIDEBAR - FILTROS
# ============================================================
lang_choice = st.sidebar.selectbox("🌐 Language / Idioma", ["Português", "English"])
t = languages[lang_choice]

st.sidebar.header(t["sidebar_header"])

min_date, max_date = df['data_venda'].min().date(), df['data_venda'].max().date()
date_range = st.sidebar.date_input(t["date_label"], value=(min_date, max_date))

# CORREÇÃO DO ERRO DE STRING: convertendo para str antes do sorted
regioes = [t["all_opt"]] + sorted([str(r) for r in df['regiao'].dropna().unique()])
regiao_selecionada = st.sidebar.selectbox(t["region_label"], regioes)

categorias = [t["all_opt"]] + sorted([str(c) for c in df['categoria'].dropna().unique()])
categoria_selecionada = st.sidebar.selectbox(t["cat_label"], categorias)

top_cidades_list = df['cidade'].value_counts().head(20).index.tolist()
cidades = [t["all_opt"]] + sorted([str(cid) for cid in top_cidades_list])
cidade_selecionada = st.sidebar.selectbox(t["city_label"], cidades)

# Aplicação dos Filtros
df_filtered = df.copy()
if len(date_range) == 2:
    df_filtered = df_filtered[(df_filtered['data_venda'].dt.date >= date_range[0]) & (df_filtered['data_venda'].dt.date <= date_range[1])]

if regiao_selecionada != t["all_opt"]:
    df_filtered = df_filtered[df_filtered['regiao'] == regiao_selecionada]
if categoria_selecionada != t["all_opt"]:
    df_filtered = df_filtered[df_filtered['categoria'] == categoria_selecionada]
if cidade_selecionada != t["all_opt"]:
    df_filtered = df_filtered[df_filtered['cidade'] == cidade_selecionada]

# ============================================================
# HEADER
# ============================================================
st.markdown(f'<p class="main-header">{t["header_title"]}</p>', unsafe_allow_html=True)

# ============================================================
# KPIs PRINCIPAIS
# ============================================================
col1, col2, col3, col4, col5 = st.columns(5)
total_receita = df_filtered['receita'].sum()
total_lucro = df_filtered['lucro'].sum()
margem_media = df_filtered['margem_percentual'].mean()
num_vendas = len(df_filtered)
ticket_medio = total_receita / num_vendas if num_vendas > 0 else 0

col1.metric(t["kpi_rev"], f"${total_receita:,.0f}", f"{(total_receita/df['receita'].sum()*100):.1f}% {t['delta_total']}")
col2.metric(t["kpi_profit"], f"${total_lucro:,.0f}", f"{margem_media:.1f}% {t['delta_margin']}")
col3.metric(t["kpi_margin"], f"{margem_media:.1f}%")
col4.metric(t["kpi_sales"], f"{num_vendas:,}")
col5.metric(t["kpi_ticket"], f"${ticket_medio:,.0f}")

st.markdown("---")

# ============================================================
# LINHA 1: EVOLUÇÃO E DISTRIBUIÇÃO
# ============================================================
c1, c2 = st.columns(2)
with c1:
    st.subheader(t["chart_evol_title"])
    receita_diaria = df_filtered.groupby('data_venda')['receita'].sum().reset_index()
    fig1 = px.line(receita_diaria, x='data_venda', y='receita', title=t["chart_evol_y"],
                  labels={'data_venda': 'Data', 'receita': 'Revenue ($)'})
    fig1.update_traces(line_color='#1f77b4', line_width=2)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.subheader(t["chart_cat_title"])
    receita_cat = df_filtered.groupby('categoria')['receita'].sum().nlargest(10).reset_index()
    fig2 = px.pie(receita_cat, values='receita', names='categoria', title=t["chart_cat_sub"], hole=0.4, color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig2, use_container_width=True)

# ============================================================
# LINHA 2: PRODUTOS E REGIÃO
# ============================================================
c3, c4 = st.columns(2)
with c3:
    st.subheader(t["chart_prod_title"])
    top_p = df_filtered.groupby('produto')['receita'].sum().nlargest(10).reset_index()
    fig3 = px.bar(top_p, x='receita', y='produto', orientation='h', title=t["chart_prod_sub"],
                 color='receita', color_continuous_scale='Viridis',
                 labels={'receita': 'Revenue ($)', 'produto': t["col_prod"]})
    fig3.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    st.subheader(t["chart_reg_title"])
    perf_reg = df_filtered.groupby('regiao').agg({'receita':'sum', 'lucro':'sum'}).reset_index().nlargest(10, 'receita')
    fig4 = go.Figure(data=[
        go.Bar(name=t["col_rev"], x=perf_reg['regiao'], y=perf_reg['receita'], marker_color='lightblue'),
        go.Bar(name=t["col_profit"], x=perf_reg['regiao'], y=perf_reg['lucro'], marker_color='darkblue')
    ])
    fig4.update_layout(title=t["chart_reg_sub"], barmode='group', height=400)
    st.plotly_chart(fig4, use_container_width=True)

# ============================================================
# LINHA 3: FORNECEDOR E CIDADES
# ============================================================
c5, c6 = st.columns(2)
with c5:
    st.subheader(t["chart_supp_title"])
    top_f = df_filtered.groupby('fornecedor').agg({'receita':'sum', 'margem_percentual':'mean'}).reset_index().nlargest(10, 'receita')
    fig5 = px.bar(top_f, x='receita', y='fornecedor', orientation='h', title=t["chart_supp_sub"],
                 color='margem_percentual', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig5, use_container_width=True)

with c6:
    st.subheader(t["chart_city_title"])
    top_cid = df_filtered.groupby('cidade')['receita'].sum().nlargest(10).reset_index()
    fig6 = px.bar(top_cid, x='cidade', y='receita', title=t["chart_city_sub"],
                 color='receita', color_continuous_scale='Viridis',)
    st.plotly_chart(fig6, use_container_width=True)

# ============================================================
# LINHA 4: TABELA DETALHADA
# ============================================================
st.markdown("---")
st.subheader(t["tab_title"])
tabela = df_filtered.groupby('produto').agg({'receita':'sum', 'lucro':'sum', 'quantidade':'sum', 'margem_percentual':'mean', 'preco_unitario':'mean'}).round(2)
tabela = tabela.sort_values('receita', ascending=False).head(20)

# Tradução do cabeçalho da tabela e do índice
tabela.columns = [t["col_rev"], t["col_profit"], t["col_qty"], t["col_avg_margin"], t["col_avg_price"]]
tabela.index.name = t["col_prod"]

# Formatação visual (mantendo a lógica original)
tab_formatada = tabela.copy()
tab_formatada[t["col_rev"]] = tab_formatada[t["col_rev"]].apply(lambda x: f"${x:,.2f}")
tab_formatada[t["col_profit"]] = tab_formatada[t["col_profit"]].apply(lambda x: f"${x:,.2f}")
tab_formatada[t["col_qty"]] = tab_formatada[t["col_qty"]].apply(lambda x: f"{int(x):,}")
tab_formatada[t["col_avg_margin"]] = tab_formatada[t["col_avg_margin"]].apply(lambda x: f"{x:.1f}%")
tab_formatada[t["col_avg_price"]] = tab_formatada[t["col_avg_price"]].apply(lambda x: f"${x:.2f}")

st.dataframe(tab_formatada, use_container_width=True)

# RODAPÉ
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: #666;'>
    <p><b>Executive Sales Dashboard</b> | {t['footer_dev']}</p>
    <p>{t['footer_data']} {df_filtered['data_venda'].min().strftime('%d/%m/%Y')} - {df_filtered['data_venda'].max().strftime('%d/%m/%Y')}</p>
    </div>
    """, unsafe_allow_html=True)