import pandas as pd
import numpy as np
from datetime import datetime
import os

def load_raw_data(filepath):
    """
    Carrega os dados brutos do BigQuery
    """
    print("📂 Carregando dados brutos...")
    df = pd.read_csv(filepath)
    print(f"✅ {len(df):,} registros carregados")
    return df

def clean_data(df):
    """
    Limpa e prepara os dados para análise
    """
    print("\n🧹 Limpando dados...")
    
    df_clean = df.copy()
    df_clean['data_venda'] = pd.to_datetime(df_clean['data_venda'])
    
    string_columns = ['loja', 'cidade', 'regiao', 'categoria', 'produto', 'fornecedor']
    for col in string_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].str.strip()
    
    initial_rows = len(df_clean)
    df_clean = df_clean.dropna(subset=['data_venda', 'receita', 'quantidade'])
    removed_rows = initial_rows - len(df_clean)
    
    if removed_rows > 0:
        print(f"   ⚠️  Removidos {removed_rows} registros com valores nulos")
    
    df_clean = df_clean[df_clean['receita'] > 0]
    df_clean = df_clean[df_clean['quantidade'] > 0]
    df_clean['margem_percentual'] = df_clean['margem_percentual'].clip(-100, 100)
    
    print(f"✅ Dados limpos: {len(df_clean):,} registros")
    
    return df_clean

def add_time_features(df):
    """
    Adiciona features temporais para análise
    """
    print("\n📅 Adicionando features temporais...")
    
    df['ano'] = df['data_venda'].dt.year
    df['mes'] = df['data_venda'].dt.month
    df['trimestre'] = df['data_venda'].dt.quarter
    df['dia_semana'] = df['data_venda'].dt.dayofweek
    df['nome_mes'] = df['data_venda'].dt.strftime('%Y-%m')
    df['semana_ano'] = df['data_venda'].dt.isocalendar().week
    
    dias = {0: 'Segunda', 1: 'Terça', 2: 'Quarta', 3: 'Quinta', 
            4: 'Sexta', 5: 'Sábado', 6: 'Domingo'}
    df['nome_dia_semana'] = df['dia_semana'].map(dias)
    
    print("✅ Features temporais adicionadas")
    
    return df

def add_business_metrics(df):
    """
    Adiciona métricas de negócio calculadas
    """
    print("\n💰 Calculando métricas de negócio...")
    
    df['ticket_medio'] = df['receita'] / df['quantidade']
    
    df['classificacao_margem'] = pd.cut(
        df['margem_percentual'],
        bins=[-np.inf, 0, 10, 20, 30, np.inf],
        labels=['Negativa', 'Baixa', 'Média', 'Boa', 'Excelente']
    )
    
    df['classificacao_venda'] = pd.cut(
        df['receita'],
        bins=[0, 100, 500, 1000, 5000, np.inf],
        labels=['Muito Baixa', 'Baixa', 'Média', 'Alta', 'Muito Alta']
    )
    
    print("✅ Métricas de negócio calculadas")
    
    return df

def generate_summary_stats(df):
    """
    Gera estatísticas resumidas dos dados
    """
    print("\n📊 Estatísticas Resumidas:")
    print("=" * 60)
    
    print(f"\n📅 Período dos Dados:")
    print(f"   Data inicial: {df['data_venda'].min().strftime('%d/%m/%Y')}")
    print(f"   Data final: {df['data_venda'].max().strftime('%d/%m/%Y')}")
    
    print(f"\n💰 Métricas Financeiras:")
    print(f"   Receita Total: R$ {df['receita'].sum():,.2f}")
    print(f"   Lucro Total: R$ {df['lucro'].sum():,.2f}")
    print(f"   Margem Média: {df['margem_percentual'].mean():.2f}%")
    print(f"   Ticket Médio: R$ {df['ticket_medio'].mean():.2f}")
    
    print(f"\n📦 Volume:")
    print(f"   Total de Vendas: {len(df):,}")
    print(f"   Quantidade Total Vendida: {df['quantidade'].sum():,} unidades")
    
    print(f"\n🏪 Dados Categóricos:")
    print(f"   Lojas Únicas: {df['loja'].nunique()}")
    print(f"   Cidades: {df['cidade'].nunique()}")
    print(f"   Regiões: {df['regiao'].nunique()}")
    print(f"   Categorias: {df['categoria'].nunique()}")
    print(f"   Produtos Únicos: {df['produto'].nunique()}")
    print(f"   Fornecedores: {df['fornecedor'].nunique()}")
    
    print("\n" + "=" * 60)

def save_processed_data(df, output_path):
    """
    Salva os dados processados
    """
    print(f"\n💾 Salvando dados processados em: {output_path}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    
    print(f"✅ Dados salvos com sucesso!")
    print(f"   Tamanho do arquivo: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")

def main():
    """
    Pipeline completo de processamento
    """
    print("\n" + "=" * 60)
    print("🚀 PIPELINE DE PROCESSAMENTO DE DADOS")
    print("=" * 60)
    
    raw_data_path = 'data/raw/IOWA_LIQUOR_SALES.csv'
    processed_data_path = 'data/processed/sales_data_processed.csv'
    
    df = load_raw_data(raw_data_path)
    df = clean_data(df)
    df = add_time_features(df)
    df = add_business_metrics(df)
    generate_summary_stats(df)
    save_processed_data(df, processed_data_path)
    
    print("\n✅ Pipeline concluído com sucesso!")
    print("=" * 60 + "\n")
    
    return df

if __name__ == "__main__":
    df_processed = main()
