# 🎵 Moodly - AI Mood-Based Music Recommender

Moodly is a fun AI-powered web app that detects your mood based on your text input and recommends a matching YouTube song. It uses VADER (Valence Aware Dictionary and sEntiment Reasoner) for accurate sentiment analysis.

---

## 🚀 Features

- Real-time sentiment analysis of your thoughts
- Mood detection: Happy, Sad, Angry, Neutral
- Matching YouTube music recommendations
- Built with Python and Streamlit

---

---

## 🧠 How It Works

1. User types something like: "I just got a new job!"
2. VADER analyzes the sentiment of the text.
3. Based on the compound score:
   - 😊 Positive → Happy
   - 😢 Negative → Sad
   - 😠 Strong Negative → Angry
   - 😐 Neutral → Neutral
4. Recommends a matching song from YouTube!

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/moodly.git
cd moodly
pip install -r requirements.txt
```

## 🚀 Run the app

```bash
streamlit run moodly.py
```

##📚 Libraries Used

->Streamlit

->NLTK

->VADER Sentiment Analyzer (nltk.sentiment.vader)




