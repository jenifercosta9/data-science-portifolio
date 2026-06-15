# CEAPS Recommendation System (Senator Expense Similarity)

[English](#english) | [Português](#português)

---

## English

### 1. Business Problem
The Brazilian Senate provides public data on parliamentary expenses through the CEAPS (Quota for Exercising Parliamentary Activity of Senators). However, this data is highly fragmented and difficult to interpret.

The goal of this project is to build a **recommendation system** that identifies similarity patterns between senators based on their expense behavior, enabling comparative analysis and transparency.

---

### 2. Dataset
The dataset was collected from the official CEAPS portal (Senate Federal open data).

It includes detailed records of parliamentary expenses such as:
- Travel costs  
- Office maintenance  
- Fuel  
- Accommodation  
- Other administrative expenses  

The data required extensive cleaning, standardization, and aggregation before modeling.

---

### 3. Key Questions
- Which senators have the most similar spending behavior?
- What types of expenses define similarity between senators?
- How does a senator's spending profile compare to their peer group?

---

### 4. Methodology
The project followed these steps:

- Data extraction from CEAPS open data portal  
- Data cleaning and preprocessing (handling missing values, normalization)  
- Feature engineering to aggregate expense categories per senator  
- Construction of a similarity matrix  
- Recommendation system based on similarity scores  
- Deployment using Streamlit

Tools used:
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Plotly  

---

### 5. Key Insights
- Senators can be grouped based on consistent spending patterns  
- Certain expense categories strongly influence similarity between senators  
- The model reveals behavioral clusters in public spending profiles  

---

### 6. Business Recommendations
- Improve transparency by grouping senators with similar expense behavior  
- Support audit processes by identifying unusual spending patterns  
- Provide citizens with an intuitive way to compare parliamentary expenses  

---

### 7. Next Steps
- Incorporate time-series analysis of expenses  
- Add clustering algorithms (K-Means, DBSCAN) for segmentation  
- Improve UI with filters by party, state, or year  
- Deploy API version for external integration  

---

## Português

### 1. Problema de Negócio
Os dados de despesas parlamentares do Senado Brasileiro (CEAPS) são públicos, porém pouco estruturados e difíceis de interpretar.

Este projeto tem como objetivo desenvolver um **sistema de recomendação** que identifica padrões de similaridade entre senadores com base em seus gastos, facilitando análises comparativas e promovendo transparência.

---

### 2. Conjunto de Dados
Os dados foram obtidos no portal oficial da CEAPS (dados abertos do Senado Federal).

Incluem registros detalhados de despesas parlamentares como:
- Passagens aéreas  
- Aluguel e manutenção de escritório  
- Combustível  
- Hospedagem  
- Outras despesas administrativas  

Foi necessário realizar limpeza, padronização e agregação dos dados antes da modelagem.

---

### 3. Perguntas-Chave
- Quais senadores possuem padrões de gastos mais semelhantes?
- Quais categorias de despesas influenciam essa similaridade?
- Como o perfil de um senador se compara ao seu grupo de pares?

---

### 4. Metodologia
O projeto seguiu as etapas:

- Extração de dados do portal CEAPS  
- Limpeza e tratamento dos dados  
- Engenharia de atributos por categoria de despesa  
- Construção de matriz de similaridade  
- Sistema de recomendação baseado em similaridade  
- Deploy com Streamlit  

Ferramentas utilizadas:
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Plotly  

---

### 5. Principais Insights
- É possível agrupar senadores por padrões consistentes de gastos  
- Algumas categorias de despesas têm maior impacto na similaridade  
- O modelo revela clusters de comportamento de gastos públicos  

---

### 6. Recomendações de Negócio
- Aumentar transparência ao agrupar senadores por comportamento de gastos  
- Apoiar auditorias com detecção de padrões fora da curva  
- Facilitar a análise cidadã das despesas parlamentares  

---

### 7. Próximos Passos
- Adicionar análise temporal dos gastos  
- Implementar clustering (K-Means, DBSCAN)  
- Melhorar interface com filtros por partido, estado e ano  
- Criar API para integração externa  

---

### 🔗 Live App
https://sistemaderecomendacaoceaps.streamlit.app/
