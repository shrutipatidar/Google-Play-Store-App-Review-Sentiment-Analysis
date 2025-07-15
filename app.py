
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import seaborn as sns


# --- CONFIG ---
st.set_page_config(page_title="App Review Sentiment Analysis", layout="wide", page_icon="📱")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1611926653458-09294c0f13a4");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- LOAD DATA ---
df = pd.read_csv("data/all_apps_reviews_cleaned.csv")

# --- SIDEBAR ---
st.sidebar.title("🎛️ App Filters")
st.sidebar.markdown("---")

st.sidebar.subheader("📲 App Selector")
app_list = sorted(df['App'].dropna().unique())
selected_app = st.sidebar.selectbox("Choose an App", app_list)

st.sidebar.subheader("🧠 Sentiment Filter")
sentiments = st.sidebar.multiselect(
    "Select Sentiment Types", ["Positive", "Neutral", "Negative"],
    default=["Positive", "Neutral", "Negative"]
)

st.sidebar.subheader("🔎 Keyword Search")
keyword = st.sidebar.text_input("Search Reviews (optional)")

st.sidebar.markdown("---")
st.sidebar.subheader("🚩 Top 5 Apps with Most Negative Reviews")
negative_apps = (
    df.groupby('App')['Sentiment']
    .apply(lambda x: (x == 'Negative').sum() / len(x) * 100)
    .sort_values(ascending=False)
    .head(5)
)
st.sidebar.write(negative_apps.round(2).astype(str) + '%')

# --- FILTER DATA ---
filtered_df = df[df['App'] == selected_app]
filtered_df = filtered_df[filtered_df['Sentiment'].isin(sentiments)]
if keyword:
    filtered_df = filtered_df[filtered_df['Translated_Review'].str.contains(keyword, case=False, na=False)]

# --- HEADER ---
st.title("📊 Google Play Store App Review Sentiment Analysis")
st.markdown(f"### Analyzing *{selected_app}* — Total Reviews: {len(filtered_df)}")

# --- TABS FOR ORGANIZED UI ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Sentiment Overview", 
    "☁️ Word Analysis", 
    "📋 Sample Reviews", 
    "🌟 Insights"
])

# --- TAB 1: Sentiment Metrics + Pie ---
with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", len(filtered_df))
    pos_pct = round((filtered_df['Sentiment'] == 'Positive').sum() / len(filtered_df) * 100, 1) if len(filtered_df) > 0 else 0
    col2.metric("Positive Sentiment", f"{pos_pct}%")
    neg_pct = round((filtered_df['Sentiment'] == 'Negative').sum() / len(filtered_df) * 100, 1) if len(filtered_df) > 0 else 0
    col3.metric("Negative Sentiment", f"{neg_pct}%")

    st.subheader("🧁 Sentiment Distribution (Pie Chart)")
    sentiment_counts = filtered_df['Sentiment'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig1)

# --- TAB 2: WordCloud + Frequency Chart ---
with tab2:
    st.subheader("🔠 Most Frequent Words (Filtered Reviews)")
    words = " ".join(filtered_df['cleaned'].dropna()).split()
    common_words = Counter(words).most_common(10)

    if common_words:
        word_df = pd.DataFrame(common_words, columns=['Word', 'Count'])
        fig2 = plt.figure(figsize=(10, 4))
        sns.barplot(x='Count', y='Word', data=word_df, palette='Blues_d')
        st.pyplot(fig2)
    else:
        st.warning("⚠️ Not enough words to generate frequency chart.")

    st.subheader("☁️ Positive Review WordCloud")
    pos_text = " ".join(filtered_df[filtered_df['Sentiment'] == 'Positive']['cleaned'].dropna())
    if len(pos_text.strip()) >= 5:
        pos_wc = WordCloud(width=800, height=300, background_color="white").generate(pos_text)
        st.image(pos_wc.to_array())
    else:
        st.info("Not enough positive reviews to show a wordcloud.")

# --- TAB 3: Sample Reviews Table ---
with tab3:
    st.subheader("📋 Sample User Reviews")
    with st.expander("Show Top 20 Reviews"):
        st.dataframe(filtered_df[['Translated_Review', 'Sentiment']].head(20))

# --- TAB 4: Insights Section ---
with tab4:
    st.subheader("🌟 Top 5 Best Apps (100% Positive Reviews)")
    app_sentiment_group = df.groupby('App')['Sentiment']
    positive_apps = app_sentiment_group.apply(lambda x: (x == 'Positive').sum() / len(x))
    perfect_apps = positive_apps[positive_apps == 1.0]
    perfect_apps_df = df[df['App'].isin(perfect_apps.index)]
    perfect_counts = perfect_apps_df['App'].value_counts()
    top_5_perfect = perfect_counts[perfect_counts >= 5].head(5)

    if not top_5_perfect.empty:
        st.write("These apps have only positive reviews and at least 5 reviews:")
        st.table(top_5_perfect.rename("Number of Positive Reviews"))
    else:
        st.info("No apps found with 100% positive sentiment and at least 5 reviews.")

# --- FOOTER ---
st.markdown("---")
st.caption("Designed by Shruti Patidar")


