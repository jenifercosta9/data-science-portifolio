# E-commerce Customer Behavior Analysis

[English](#english) | [Português](#português)

---

## English

This project uses a publicly available dataset designed to simulate real-world e-commerce shopper behavior. Due to file size limitations, the dataset is not stored directly in this GitHub repository. Instructions on how to download the dataset are provided in the data/ folder.

### Dataset
The dataset contains simulated e-commerce user behavior, representing different stages of the purchasing journey.

It includes demographic, behavioral, and operational variables such as:

"Weekly purchase frequency"
"Cart abandonment rate"
"Return rate"
"Subscription type (Premium vs Non-Premium)"
"User segmentation indicators (e.g. high-value users)"

The dataset is balanced and suitable for exploratory analysis, hypothesis testing, and behavioral segmentation.

### 1. Business Problem

Many e-commerce platforms adopt Premium subscription models with the expectation that subscribed users will demonstrate higher engagement, stronger purchasing behavior, and greater overall value.

However, without data validation, these assumptions may lead to ineffective monetization strategies.

This project investigates whether holding a Premium subscription is associated with meaningful differences in customer behavior and value, specifically:

Operational behaviors (purchase frequency, cart abandonment, return rates)

Customer value segmentation (high-value vs non-high-value users)

The goal is to assess whether Premium subscription status is a reliable lever for customer differentiation and strategic decision-making.


---

### 2. Key Questions
- Question 1: Does having a Premium subscription influence operational user behavior (e.g. purchases, returns, cart abandonment)?
- Question 2: Are Premium users more likely to be classified as high-value customers?
- Question 3: Is subscription type a meaningful segmentation variable for behavioral differentiation? 

---

### 3. Methodology

The analysis followed a structured exploratory and hypothesis-driven approach:

Data cleaning and validation

Exploratory Data Analysis (EDA) using descriptive statistics and visualizations

Group comparisons between Premium and Non-Premium users

Statistical hypothesis testing (non-parametric tests) to assess behavioral differences

Segmentation analysis focusing on operational and value-based indicators

Python libraries used include Pandas, NumPy, Matplotlib, and SciPy.

---

### 4. Key Insights
No statistically significant differences were found between Premium and Non-Premium users regarding:

Weekly purchase frequency

Cart abandonment rate

Product return rate

Premium subscription status does not appear to influence short-term operational behaviors.

The proportion of high-value users is nearly identical between Premium and Non-Premium groups.

These findings suggest that Premium subscription alone is not a strong behavioral or value-based differentiator in this dataset.

---

### 5. Business Recommendations

Reevaluate the Premium subscription value proposition, as current benefits may not be driving behavioral change.

Consider personalization, loyalty programs, or experience-based incentives instead of subscription-based segmentation.

Use behavioral metrics rather than subscription status as the primary driver for customer segmentation.

Invest in experimentation (A/B testing) to validate whether changes in Premium benefits can influence user behavior.

---

### 6. Next Steps

Incorporate time-based analysis to capture long-term behavioral changes.

Explore customer lifecycle stages instead of static segmentation.

Apply clustering techniques to identify latent behavioral segments.

Test causal impacts through controlled experiments.

---

## Português

Este projeto utiliza um dataset de acesso público, desenvolvido para simular o comportamento real de consumidores em e-commerce.

Devido às limitações de tamanho de arquivos do GitHub, o dataset não está armazenado diretamente neste repositório.
As instruções para download do dataset estão disponíveis na pasta data/.


### 1. Problema de Negócio

Plataformas de e-commerce frequentemente adotam modelos de assinatura Premium com a expectativa de que usuários assinantes apresentem maior engajamento, melhores comportamentos de compra e maior valor para o negócio.

No entanto, sem validação analítica, essas premissas podem levar a decisões estratégicas ineficientes.

Este projeto investiga se a assinatura Premium está associada a diferenças relevantes no comportamento e no valor dos clientes, considerando:

Comportamentos operacionais (frequência de compras, abandono de carrinho e devoluções)

Segmentação por valor (usuários de alto valor vs demais usuários)

O objetivo é avaliar se o status Premium é, de fato, um fator confiável para diferenciação de clientes e apoio à tomada de decisão estratégica.

---

### 2. Conjunto de Dados
O conjunto de dados representa o comportamento simulado de usuários em um ambiente de e-commerce, cobrindo diferentes etapas da jornada de compra.

Inclui variáveis demográficas, comportamentais e operacionais, tais como:

Frequência semanal de compras

Taxa de abandono de carrinho

Taxa de devolução

Tipo de assinatura (Premium vs Não-Premium)

Indicadores de segmentação (ex.: usuários de alto valor)

O dataset é balanceado e adequado para análises exploratórias, testes de hipótese e segmentação comportamental.

---

### 3. Perguntas-Chave
- Pergunta 1: A assinatura Premium impacta comportamentos operacionais dos usuários? 
- Pergunta 2: Usuários Premium têm maior probabilidade de serem classificados como high-value users?
- Pergunta 3: O tipo de assinatura é uma variável relevante para segmentação comportamental?

---

### 4. Metodologia
A análise seguiu uma abordagem estruturada, combinando exploração de dados e validação estatística:

Limpeza e validação dos dados

Análise Exploratória de Dados (EDA)

Comparação entre grupos Premium e Não-Premium

Testes estatísticos para avaliar diferenças comportamentais

Análise de segmentação baseada em indicadores operacionais e de valor

As principais ferramentas utilizadas foram Python, Pandas, NumPy, Matplotlib e SciPy.

---

### 5. Principais Insights
Não foram identificadas diferenças estatisticamente significativas entre usuários Premium e Não-Premium em:

Frequência semanal de compras

Taxa de abandono de carrinho

Taxa de devolução

A assinatura Premium não demonstrou impacto relevante em comportamentos operacionais de curto prazo.

A proporção de usuários de alto valor é praticamente igual entre os dois grupos.

Esses resultados indicam que a assinatura Premium, isoladamente, não é um bom fator de diferenciação comportamental neste cenário.

---

### 6. Recomendações de Negócio
Reavaliar a proposta de valor da assinatura Premium.

Priorizar estratégias de personalização e fidelização baseadas em comportamento real.

Utilizar métricas comportamentais como principal critério de segmentação.

Implementar testes controlados para avaliar possíveis melhorias no modelo de assinatura.

---

### 7. Próximos Passos
Analisar o comportamento dos usuários ao longo do tempo.

Investigar estágios do ciclo de vida do cliente.

Aplicar técnicas de clusterização para identificar padrões ocultos.

Explorar análises causais por meio de experimentos.
