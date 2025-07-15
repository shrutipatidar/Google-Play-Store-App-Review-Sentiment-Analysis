# App Review Sentiment Analysis Dashboard

This project is a data visualization dashboard built using Streamlit. It performs sentiment analysis on user reviews from the Google Play Store and provides insights into how users perceive different apps. The application includes interactive filtering, sentiment visualizations, keyword analysis, and identification of high-performing and underperforming apps.

## Features

- Filter reviews by app name, sentiment category (Positive, Neutral, Negative), and custom keywords
- View sentiment distribution using pie charts
- Generate word clouds from positive reviews
- Analyze frequent keywords in review content
- Display sample user reviews
- Highlight top apps with the highest percentage of positive or negative reviews

## Technologies Used

- Python 3.10+
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- WordCloud
- TextBlob
- Git & GitHub (for version control)

## Installation Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/app-review-sentiment.git
cd app-review-sentiment

### 2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate     # On Windows

### OR

source venv/bin/activate  # On macOS/Linux

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.


## Deployment on Streamlit Cloud

You can host your project online using [Streamlit Community Cloud](https://streamlit.io/cloud). Follow these steps:

1. Push your project to a public GitHub repository.
2. Go to [https://share.streamlit.io](https://share.streamlit.io).
3. Sign in with your GitHub account.
4. Click "New App", select your repository, and choose `app.py` as the main file.
5. Click "Deploy".


## Dataset Sources

This project uses publicly available datasets from Kaggle:

* [googleplaystore.csv](https://www.kaggle.com/datasets/lava18/google-play-store-apps)
* [googleplaystore\_user\_reviews.csv](https://www.kaggle.com/datasets/lava18/google-play-store-apps)


## License

This project is released under the MIT License. You are free to use, modify, and distribute it.


## Author

Shruti Patidar

