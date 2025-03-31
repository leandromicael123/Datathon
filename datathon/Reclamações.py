import pandas as pd
from textblob import TextBlob
from googletrans import Translator
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

# Cache para evitar traduções repetidas
@lru_cache(maxsize=1000)
def translate_text(text):
    translator = Translator()
    return translator.translate(text, dest='en').text

# Função para analisar o sentimento de cada texto
def analyze_sentiment(text):
    if not isinstance(text, str):
        return 0  # Retorna 0 para valores não textuais
    texts = text.split(';')  # Dividir o texto por ';'
    sentiments = []
    for t in texts:
        try:
            translated_text = translate_text(t.strip())
            blob = TextBlob(translated_text)
            sentiments.append(blob.sentiment.polarity)  # Polaridade do sentimento
        except Exception:
            sentiments.append(0)  # Em caso de erro, atribuir polaridade neutra
    return sum(sentiments) / len(sentiments) if sentiments else 0  # Média dos sentimentos

# Carregar o dataset
df_clientes = pd.read_excel("analise.xlsx", sheet_name=1)

# Aplicar a análise de sentimento em paralelo
with ThreadPoolExecutor() as executor:
    df_clientes['sentiment'] = list(executor.map(analyze_sentiment, df_clientes['Detalhes_Reclamações']))

# Salvar os resultados em um novo arquivo Excel
df_clientes.to_excel('sentiment_analysis_results.xlsx', index=False)

print("Análise de sentimento concluída e salva em 'sentiment_analysis_results.xlsx'.")
