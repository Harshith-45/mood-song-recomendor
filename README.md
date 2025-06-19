# 🎵 Mood-Based Song Recommender

A simple web app that recommends songs based on the user’s mood, detected through a journal-like text input. Just write how you're feeling, and the app will match it with a playlist that fits your emotions.

---

## 💡 Features

- 💬 Input natural language like “I feel stressed but optimistic.”
- 🧠 Detects emotion using lightweight sentiment analysis
- 🎧 Returns 3 songs matching the mood from a curated library
- 🌐 Clean HTML/CSS frontend with music-themed design
- 🔥 No external APIs used – works entirely offline

---

## 🚀 How It Works

1. User submits a journal entry
2. Sentiment analysis is performed on the text
3. The app selects a mood: `happy`, `sad`, `chill`, `angry`, `romantic`, etc.
4. 3 songs are chosen from `songs.json` for that mood
5. The results are displayed with clickable YouTube links

---

## 📁 Project Structure

mood-song-recommender/
├── app.py # Flask backend
├── mood_model.py # Sentiment detection logic
├── songs.json # Song library by mood
├── static/
│ └── style.css # Music-themed CSS
├── templates/
│ └── index.html # UI for user input & results
└── README.md # You’re here

Install dependencies

pip install flask textblob
python -m textblob.download_corpora

Run the app

python app.py
Visit in browser

arduino
http://localhost:5000
