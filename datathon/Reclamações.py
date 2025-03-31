import pandas as pd
from textblob import TextBlob
from googletrans import Translator
from concurrent.futures import ThreadPoolExecutor

# Cache manual para evitar traduções repetidas
translation_cache = {}

def translate_text(text):
    if text in translation_cache:
        return translation_cache[text]
    translator = Translator()
    try:
        translated = translator.translate(text, dest='en').text
        translation_cache[text] = translated
        return translated
    except Exception:
        return text  # Retorna o texto original em caso de falha

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
            # Normalizar a polaridade para a escala de 0 a 1
            normalized_sentiment = blob.sentiment.polarity
            sentiments.append(normalized_sentiment)
        except Exception:
            sentiments.append(0.5)  # Em caso de erro, atribuir polaridade neutra
    return sum(sentiments) / len(sentiments) if sentiments else 0.5  # Média dos sentimentos

# Carregar o dataset
df_clientes = pd.read_csv("clientes.csv")

# Aplicar a análise de sentimento em paralelo
with ThreadPoolExecutor() as executor:
    df_clientes['sentimento'] = list(executor.map(analyze_sentiment, df_clientes['Detalhes_Reclamações']))

# Salvar os resultados em um novo arquivo Excel
df_clientes.to_csv('clientes.csv', index=False)

print("Análise de sentimento concluída e salva em 'clientes.csv'.")
