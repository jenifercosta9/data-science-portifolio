
# Análise Competitiva do Mercado de Delivery Brasileiro

[English](#english) | [Português](#português)

---

## English

### 1. Business Problem
The Brazilian food delivery market is dominated by iFood, which holds approximately 80% market share. However, new entrants — particularly Keeta, backed by Chinese giant Meituan — are beginning to challenge this dominance.

The goal of this project is to build a **competitive intelligence dashboard** that consolidates data from multiple public sources to analyze market share, user satisfaction, operational models, and strategic threats across the four main players: iFood, Rappi, 99Food, and Keeta.

### 2. Dataset
| Table | Content |
|---|---|
| `market_share` | Market share %, estimated revenue, growth projections |
| `reclame_aqui` | Complaint volume, satisfaction scores, resolution rates |
| `avaliacao_app` | App Store / Google Play ratings and download counts |
| `dados_operacionais` | Cities covered, couriers, partner restaurants, founding year |

### 3. Key Questions
- Who dominates the Brazilian delivery market and by how much?
- Which player delivers the best user experience?
- What is the real strategic threat posed by Keeta?
- What does the competitive landscape look like in 1-2 and 3-5 years?

### 4. Methodology
- Data collection from public sources · Data cleaning (Power Query) · MySQL database · DAX measures · 6-page Power BI dashboard

Tools: Python · MySQL · Power BI · Power Query · DAX

### 5. Key Insights
- iFood holds ~80% market share with 120M orders/month, 55M users, 1,500+ cities
- Keeta has the best Reclame Aqui score (7.9), backed by Meituan with R$ 5.6B investment
- Rappi has the worst scores across all platforms (5.7 / 3.8) — clear retention crisis
- 99Food relaunched in 2025 and is still an early-stage player in the delivery market
- iFood sued Keeta for alleged corporate espionage (May 2026)

### 6. Dashboard Structure
| Page | Content |
|---|---|
| Menu | Navigation hub |
| 01 - Market Overview | Market share, revenue, KPI cards |
| 02 - User Experience | Reclame Aqui and App Store ratings |
| 03 - Business Model | Orders, cities, couriers |
| 04 - Strategic Threat | Keeta vs iFood deep-dive |
| 05 - Strategic Verdict | Short and medium-term outlook |

### 7. Business Recommendations
- iFood must monitor Keeta's geographic expansion and subsidy aggressiveness
- Rappi needs urgent action on customer experience
- 99Food launched in 2025 and is still an early-stage competitor — too soon to assess impact, but worth monitoring
- Keeta's success depends on converting R$ 5.6B into operational scale fast enough

### 8. Next Steps
- Time-series tracking of satisfaction scores · Consumer sentiment analysis · Automated data refresh pipeline · Logistics performance metrics

### 9. Click here to view the dashboard: https://encurtador.com.br/MqhP

---

## Português

### 1. Problema de Negócio
O mercado brasileiro de delivery é dominado pelo iFood, que detém aproximadamente 80% do market share. O objetivo deste projeto é desenvolver um **dashboard de inteligência competitiva** que consolida dados de múltiplas fontes públicas para analisar os quatro principais players: iFood, Rappi, 99Food e Keeta.

### 2. Conjunto de Dados
| Tabela | Conteúdo |
|---|---|
| `market_share` | Market share %, receita estimada, projeções |
| `reclame_aqui` | Volume de reclamações, notas, taxas de resolução |
| `avaliacao_app` | Notas App Store / Google Play e downloads |
| `dados_operacionais` | Cidades, entregadores, restaurantes, ano de fundação |

### 3. Perguntas-Chave
- Quem domina o mercado de delivery brasileiro e por quanto?
- Qual player entrega a melhor experiência ao usuário?
- Qual é a real ameaça estratégica da Keeta?
- Como o cenário competitivo se desenha em 1-2 e 3-5 anos?

### 4. Metodologia
- Coleta de dados públicos · Power Query · MySQL · DAX · Dashboard de 6 páginas no Power BI

Ferramentas: Python · MySQL · Power BI · Power Query · DAX

### 5. Principais Insights
- iFood detém ~80% do mercado com 120M pedidos/mês, 55M usuários, 1.500+ cidades
- Keeta tem a melhor nota do Reclame Aqui (7.9), com R$ 5,6 bi da Meituan
- Rappi tem as piores notas em todas as plataformas (5.7 / 3.8) — crise de retenção
- 99Food foi relançado em 2025 e ainda é uma empresa iniciante no setor de delivery
- iFood moveu processo judicial contra a Keeta por espionagem corporativa (maio/2026)

### 6. Estrutura do Dashboard
| Página | Conteúdo |
|---|---|
| Menu | Hub de navegação |
| 01 - Market Overview | Market share, receita, cards KPI |
| 02 - Experiência do Usuário | Notas Reclame Aqui e App Store |
| 03 - Modelo de Negócio | Pedidos, cidades, entregadores |
| 04 - Ameaça Estratégica | Keeta vs iFood |
| 05 - Veredicto Estratégico | Curto e médio prazo |

### 7. Recomendações de Negócio
- iFood deve monitorar a expansão geográfica e subsídios da Keeta
- Rappi precisa agir urgentemente na experiência do cliente
- O 99Food foi lançado em 2025 e ainda é uma empresa iniciante no ramo de delivery — é cedo para avaliar seu impacto real, mas deve ser monitorado
- O sucesso da Keeta depende de converter R$ 5,6 bi em escala operacional rápida o suficiente

### 8. Próximos Passos
- Acompanhamento temporal das notas · Análise de sentimento · Pipeline automatizado · Métricas de logística

### 9. Clique aqui para visualizar o dashboard: https://encurtador.com.br/MqhP
