from flask import Flask, render_template, request, jsonify
from mood_model import detect_mood
import json

app = Flask(__name__)

with open('songs.json', 'r') as f:
    SONG_DB = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['journal']
    mood = detect_mood(user_input)
    songs = SONG_DB.get(mood, SONG_DB['neutral'])[:3] 
    return jsonify({'mood': mood, 'songs': songs})
if __name__ == '__main__':
    app.run(debug=True)
