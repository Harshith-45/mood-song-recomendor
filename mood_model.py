import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def detect_mood(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.5:
        return 'happy'
    elif compound <= -0.5:
        return 'sad'
    elif -0.5 < compound < 0.5:
        return 'chill'
    else:
        return 'neutral'
