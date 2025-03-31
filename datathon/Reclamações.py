import pandas as pd
from textblob import TextBlob

# Sample DataFrame with complaints
df = pd.read_excel("Dataset_Datathon_IscteAvanade_Marco2025 1.xlsx", sheet_name="Clientes")

# Step 1: Strip leading/trailing spaces (if needed) and split by ';'
df['Detalhes_Reclamações'] = df['Detalhes_Reclamações'].str.strip().str.split(';')

# Step 2: Explode the lists into separate rows
df_separated = df.explode('Detalhes_Reclamações', ignore_index=True)

# Step 3: Clean the exploded DataFrame to remove NaN or empty string values (if any)
df_separated = df_separated[df_separated['Detalhes_Reclamações'].notnull() & (df_separated['Detalhes_Reclamações'] != '')]

# Function to analyze sentiment
def analyze_sentiment(text):
    if pd.isnull(text) or not isinstance(text, str):  # Check if text is NaN or not a string
        return 0  # Neutral sentiment for missing/invalid text
    print(f"Analyzing: {text}")  # Debug: Print the text being analyzed
    # Create a TextBlob object
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Apply sentiment analysis to each complaint in the DataFrame
df_separated['Sentiment'] = df_separated['Detalhes_Reclamações'].apply(analyze_sentiment)
print("\n")
# Display the DataFrame with the sentiment column
print(df_separated[['Detalhes_Reclamações', 'Sentiment']])

# Optionally, you can calculate the average sentiment of all complaints
average_sentiment = df_separated['Sentiment'].mean()
print("\nAverage Sentiment of Complaints: {:.2f}".format(average_sentiment))