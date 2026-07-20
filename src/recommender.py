import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, 'r', newline='') as song_file:
        songreader = csv.DictReader(song_file)
        for row in songreader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loading songs from {csv_path}...")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    w1,w2,w3,w4 = .325,.3,.25,.125
    reasons = []

    fav_genre = (user_prefs.get('favorite_genre')).lower()
    fav_mood = (user_prefs.get('favorite_mood')).lower()

    if fav_genre == song.get('genre'):
        genre_match = 1
        reasons.append("Matched genre taste")
    else:
        genre_match = 0
        reasons.append("Did not match genre taste")

    if fav_mood == song.get('mood'):
        mood_match = 1
        reasons.append("Matched mood taste")
    else:
        mood_match = 0
        reasons.append("Did not match mood taste")

    if user_prefs.get('target_energy') > 1:
        target_energy = 1
    else:
        target_energy = abs(float(user_prefs.get('target_energy')))

    if user_prefs.get('likes_acoustic') == True and song.get('acousticness') >= .5:
        acoustic_match = 1
        reasons.append("Matched acoustic taste")
    elif user_prefs.get('likes_acoustic') == False and song.get('acousticness') < .5:
        acoustic_match = 1
        reasons.append("Matched acoustic taste")
    else:
        acoustic_match = 0
        reasons.append("Did not match acoustic taste")

    

    score = w1*(genre_match) + w2*(mood_match) + w3*(1 - abs(song['energy'] - target_energy)) + w4*(acoustic_match)

    
        



    # Expected return format: (score, reasons)
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    
    rec = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        rec.append((song, score, explanation))


    # Expected return format: (song_dict, score, explanation)
    rec.sort(key=score_sort, reverse=True)
    return rec[:abs(k)]

def score_sort(x):
    """Returns the score element of a (song, score, explanation) tuple, for use as a sort key."""
    return x[1]
