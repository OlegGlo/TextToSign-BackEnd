from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from api.gpt_to_text import get_lyrics_from_gpt  # Import your function here

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/get-lyrics', methods=['POST'])
def get_lyrics():
    
    data = request.json
    song_name = data['songName']
    artist_name = data['artist']
    lyrics = get_lyrics_from_gpt(song_name, artist_name)
    return jsonify({'lyrics': lyrics})

if __name__ == '__main__':
    app.run(debug=True)