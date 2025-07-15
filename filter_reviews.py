import pandas as pd
import os
import re

# Step 1: Load the original user review dataset
input_path = "data/googleplaystore_user_reviews.csv"
df = pd.read_csv(input_path)

# Step 2: Drop rows with missing review text
df.dropna(subset=['Translated_Review'], inplace=True)

# Step 3: Clean review text for WordCloud and analysis
def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', str(text))  # remove special characters
    return text.lower().strip()

df['cleaned'] = df['Translated_Review'].apply(clean_text)

# Step 4: Make sure 'data/' directory exists
os.makedirs("data", exist_ok=True)

# Step 5: Save the cleaned data
output_path = "data/all_apps_reviews_cleaned.csv"
df.to_csv(output_path, index=False)

# Step 6: Confirmation Output
print(f"✅ Saved cleaned dataset to: {output_path}")
print(f"📊 Total reviews after cleaning: {len(df)}")
print("\n📝 Sample cleaned reviews:")
print(df[['App', 'Translated_Review', 'Sentiment', 'cleaned']].head())

