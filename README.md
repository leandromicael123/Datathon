📊 Datathon – Sustainable Consumption Analytics
ISCTE x Avanade (2025)
Projeto desenvolvido no âmbito do Datathon ISCTE x Avanade 2025, com foco em análise quantitativa de padrões de consumo sustentável, processamento de feedback textual e modelação preditiva para apoio à decisão estratégica.

🎯 Objetivos do Desafio
A empresa pretende:

Identificar padrões de consumo de produtos sustentáveis

Analisar barreiras à adoção por parte dos clientes

Segmentar consumidores com base em dados comportamentais

Extrair insights a partir de feedback textual

Desenvolver estratégias data-driven que aumentem vendas sustentáveis sem comprometer a rentabilidade

🧠 Pipeline Analítico
O projeto segue um workflow típico de Data Science, composto pelas seguintes etapas:

1️⃣ Data Ingestion & Preprocessing
Tarefas realizadas:

Importação de datasets estruturados (clientes.csv, vendas.csv, reclamacoes.csv)

Tratamento de missing values

Normalização e transformação de variáveis

Criação de features derivadas

Geração de datasets intermédios (dfnovo.csv)

Outputs principais:

tabela_descritiva_clientes.csv

tabela_descritiva_vendas.csv

2️⃣ Exploratory Data Analysis (EDA)
Análises conduzidas:

Estatística descritiva

Matriz de correlação

Visualização de distribuições

Identificação de padrões de consumo

Relação entre reclamações e comportamento de compra

Ferramentas:

pandas, matplotlib, seaborn

R (análise estatística complementar)

3️⃣ Natural Language Processing – Sentiment Analysis
Script principal: Reclamacoes.py

Processamento realizado:

Tradução automática (PT → EN) com googletrans

Cálculo de polaridade com TextBlob

Score de sentimento ∈ [-1, 1]

Agregação de múltiplas reclamações por cliente

Processamento paralelo com ThreadPoolExecutor

Integração da variável de sentimento no dataset final

Objetivo técnico:  
Transformar texto não estruturado numa feature quantitativa utilizável em modelação e segmentação.

Output:

sentiment_analysis_results.xlsx

Dataset enriquecido com variável de sentimento

4️⃣ Modelação Preditiva
Notebook principal: Previsões.ipynb

Atividades:

Construção de modelos supervisionados

Seleção de variáveis relevantes

Avaliação de desempenho

Interpretação de resultados para apoio estratégico

Bibliotecas:

scikit-learn

NumPy

5️⃣ Data Visualization & Dashboard
Desenvolvimento de um dashboard analítico em Power BI (Dashboard.pbix):

KPIs estratégicos

Visualização de padrões de consumo

Segmentação de clientes

Integração de variáveis derivadas (incluindo sentimento)

🛠️ Tecnologias Utilizadas
Python
pandas

NumPy

scikit-learn

matplotlib

seaborn

TextBlob

googletrans

R
Análise estatística complementar

Business Intelligence
Power BI

💡 Competências Técnicas Demonstradas
Data Cleaning & Feature Engineering

Exploratory Data Analysis

Sentiment Analysis (NLP lexicon-based)

Parallel Processing em Python

Supervised Machine Learning

Business Analytics & KPI Development

Integração multi-ferramentas (Python + R + Power BI)

▶️ Execução
bash
```
git clone https://github.com/leandromicael123/Datathon.git
cd Datathon-main/datathon
pip install pandas numpy scikit-learn matplotlib seaborn textblob googletrans
jupyter notebook```
