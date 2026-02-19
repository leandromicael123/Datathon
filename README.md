# 📊 Datathon – Sustainable Consumption Analytics

**ISCTE × Avanade (2025)**

Quantitative analysis of sustainable consumption patterns, textual feedback processing, and predictive modeling for strategic decision support.

## 🎯 Objectives

- Identify sustainable product consumption patterns
- Analyze customer adoption barriers
- Segment consumers based on behavioral data
- Extract insights from textual feedback
- Develop data-driven strategies to increase sustainable sales

## 🧠 Analytics Pipeline

### 1️⃣ Data Ingestion & Preprocessing
- Import structured datasets (customers, sales, complaints)
- Handle missing values and normalize variables
- Feature engineering and intermediary dataset generation
- **Outputs:** descriptive tables (CSV)

### 2️⃣ Exploratory Data Analysis (EDA)
- Descriptive statistics, correlation matrix, distribution analysis
- **Tools:** pandas, matplotlib, seaborn, R

### 3️⃣ Natural Language Processing
**Script:** `Reclamacoes.py`
- Automatic translation (PT → EN)
- Sentiment scoring [-1, 1] with TextBlob
- Parallel processing with ThreadPoolExecutor
- **Output:** `sentiment_analysis_results.xlsx`

### 4️⃣ Predictive Modeling
**Notebook:** `Previsões.ipynb`
- Supervised learning models with scikit-learn
- Variable selection and performance evaluation

### 5️⃣ Data Visualization
**Dashboard:** Power BI (Dashboard.pbix)
- KPIs, consumption patterns, customer segmentation

## 🛠️ Tech Stack

**Python:** pandas, NumPy, scikit-learn, matplotlib, seaborn, TextBlob, googletrans  
**R:** Statistical analysis  
**BI:** Power BI  

## 🚀 Quick Start

```bash
git clone https://github.com/leandromicael123/Datathon.git
cd Datathon-main/datathon
pip install pandas numpy scikit-learn matplotlib seaborn textblob googletrans
jupyter notebook
```

## 💡 Key Competencies

Data cleaning • Feature engineering • EDA • NLP • Parallel processing • Machine learning • Business analytics

