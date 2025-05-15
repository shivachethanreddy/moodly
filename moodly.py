
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')


analyzer = SentimentIntensityAnalyzer()

#  msg +YouTube songs links
mood_music = {
    "happy": {
        "message": "You're feeling happy! 🎉",
        "link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"  # Happy - Pharrell
    },
    "sad": {
        "message": "You're feeling sad 😢",
        "link": "https://www.youtube.com/watch?v=RgKAFK5djSk"  # See You Again
    },
    "angry": {
        "message": "You're feeling angry 😠",
        "link": "https://www.youtube.com/watch?v=hTWKbfoikeg"  # Nirvana
    },
    "neutral": {
        "message": "You're feeling neutral 😐",
        "link": "https://www.youtube.com/watch?v=JGwWNGJdvx8"  # Ed Sheeran
    }
}

st.title("🎵 Moodly: AI Mood-Based Music Recommender")

user_input = st.text_area("How are you feeling? (Type something)")

if st.button("Analyze Mood"):
    if user_input:
        scores = analyzer.polarity_scores(user_input)
        compound = scores['compound']

        if compound >= 0.5:
            mood = "happy"
        elif compound <= -0.5:
            mood = "angry"
        elif compound < 0:
            mood = "sad"
        else:
            mood = "neutral"

        st.subheader(mood_music[mood]["message"])
        st.markdown(f"[▶️ Listen to Music]({mood_music[mood]['link']})")
        st.markdown(f"**VADER Score:** {compound}")
    else:
        st.warning("Please type something to analyze your mood.")
