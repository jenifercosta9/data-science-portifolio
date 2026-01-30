# E-commerce Customer Behavior Analysis  
## Análise de Comportamento de Clientes em E-commerce

[English](#english) | [Português](#português)

---

## English

**End-to-end Data Science project focused on customer behavior analysis to evaluate the business impact of a Premium subscription and assess the feasibility of churn prediction models.**

**Key takeaway:**  
*With the current data strategy, proactive churn prediction is not viable. The main opportunity lies in improving data collection, not in model complexity.*

**Dataset:**  
Simulated large-scale e-commerce dataset (1M+ customer records). Due to GitHub size limitations, raw data is not stored, but generation instructions are available in the `data/` folder.  
The dataset includes demographic, behavioral, and operational variables such as:
- Weekly purchase frequency  
- Cart abandonment rate  
- Return rate  
- Subscription type (Premium vs Non-Premium)  
- Customer segmentation indicators  

![Model with Leakage](images/model1_leakage.png)  
![Realistic Model](images/model2_realistic.png)

---

### 🎯 Business Problem

**Original objective:**  
Evaluate whether a Premium subscription positively impacts customer behavior and business value.

**Extended objective:**  
Assess whether the available behavioral data supports the development of a reliable churn prediction model.

---

### 📊 Key Results

| Model | ROC-AUC | Key Finding |
|------|--------|------------|
| **Model with Data Leakage** | **1.000** | `return_rate` dominated feature importance (95.5%), revealing severe data leakage |
| **Realistic Model** | **0.500** | Behavioral data alone is insufficient for proactive churn prediction |

**Critical Insight:**  
*A high-performing model can be misleading. Without granular engagement data, churn prediction becomes reactive rather than predictive.*

---

### 🔬 Methodology

1. **Exploratory Data Analysis (EDA)** and statistical hypothesis testing  
   - Mann-Whitney U Test (p-value = 0.3779)  
   - Result: No statistically significant difference between Premium and Non-Premium customers  

2. **Customer segmentation** based on income and spending behavior  

3. **Machine Learning pipeline**  
   - Churn prediction model development  
   - Feature importance analysis  
   - Data leakage detection  
   - Construction of a realistic baseline model  

**Tech Stack:**  
`pandas` • `NumPy` • `Matplotlib` • `SciPy` • `seaborn` • `scikit-learn` • `RandomForest`

---

### 💎 Key Insights

- No meaningful behavioral differences between Premium and Non-Premium customers  
- Premium subscription does not function as a clear value differentiator  
- **New insight:** Current data does not support predictive churn modeling  

---

### 🏆 Business Recommendations

1. **Reactive retention strategy**  
   - Trigger alerts when `return_rate` exceeds the 75th percentile  

2. **Targeted A/B testing**  
   - Test discounts or incentives for customers identified as high risk  

3. **Data strategy improvement**  
   - Track granular engagement metrics (page views, time on site, click behavior)  

4. **Product strategy review**  
   - Reassess the Premium subscription value proposition  

---

## Português

**Projeto completo de Data Science com foco em análise de comportamento de clientes para avaliar o impacto de uma assinatura Premium e a viabilidade de modelos de predição de churn.**

**Insight principal:**  
*Com a estratégia atual de dados, a predição proativa de churn não é viável. A maior alavanca está na coleta de dados, não na complexidade do modelo.*

**Dataset:**  
Base de dados simulada em larga escala (1M+ registros). Os dados brutos não estão armazenados no GitHub por limitação de tamanho, mas as instruções de geração estão disponíveis na pasta `data/`.  
As variáveis incluem informações demográficas, comportamentais e operacionais, como:
- Frequência semanal de compras  
- Taxa de abandono de carrinho  
- Taxa de devolução  
- Tipo de assinatura (Premium vs Não-Premium)  
- Indicadores de segmentação de clientes  

---

### 🎯 Problema de Negócio

**Objetivo original:**  
Avaliar se a assinatura Premium gera impacto positivo no comportamento do cliente e no valor para o negócio.

**Objetivo expandido:**  
Verificar se os dados comportamentais disponíveis permitem a construção de um modelo confiável de predição de churn.

---

### 📊 Resultados Principais

| Modelo | ROC-AUC | Descoberta |
|------|--------|------------|
| **Modelo com Vazamento de Dados** | **1.000** | `return_rate` concentrou 95.5% da importância, indicando vazamento |
| **Modelo Realista** | **0.500** | Os dados atuais não permitem predição proativa de churn |

**Insight crítico:**  
*Um modelo com métricas perfeitas pode esconder problemas graves. Sem dados granulares de engajamento, a predição de churn se torna reativa.*

---

### 🔬 Metodologia

1. **Análise Exploratória de Dados (EDA)** e testes estatísticos  
   - Teste de Mann-Whitney (p-valor = 0.3779)  
   - Resultado: nenhuma diferença estatisticamente significativa entre clientes Premium e Não-Premium  

2. **Segmentação de clientes** com base em renda e comportamento de gasto  

3. **Pipeline de Machine Learning**  
   - Construção do modelo de churn  
   - Análise de importância das variáveis  
   - Detecção de vazamento de dados  
   - Definição de um modelo baseline realista  

**Stack Tecnológica:**  
`pandas` • `NumPy` • `Matplotlib` • `SciPy` • `seaborn` • `scikit-learn` • `RandomForest`

---

### 💎 Insights Principais

- Não há diferenças comportamentais relevantes entre clientes Premium e Não-Premium  
- A assinatura Premium não se configura como diferencial claro de valor  
- **Novo insight:** Os dados atuais são insuficientes para modelos preditivos de churn  

---

### 🏆 Recomendações de Negócio

1. **Retenção reativa**  
   - Alertas quando a `return_rate` ultrapassar o percentil 75  

2. **Testes A/B direcionados**  
   - Ofertas e incentivos para clientes com maior risco de churn  

3. **Estratégia de dados**  
   - Coleta de métricas detalhadas de engajamento (tempo de navegação, cliques, páginas visitadas)  

4. **Reavaliação do produto Premium**  
   - Revisar a proposta de valor da assinatura  

---

## 🚀 Next Steps / Próximos Passos

- Time-series analysis / Análise temporal  
- Advanced clustering techniques / Técnicas avançadas de clusterização  
- Controlled A/B experiments / Experimentos A/B controlados

