import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
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

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Song":
        return cls(
            id=int(row["id"]),
            title=row["title"],
            artist=row["artist"],
            genre=row["genre"],
            mood=row["mood"],
            energy=float(row["energy"]),
            tempo_bpm=float(row["tempo_bpm"]),
            valence=float(row["valence"]),
            danceability=float(row["danceability"]),
            acousticness=float(row["acousticness"]),
        )

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    @staticmethod
    def load_songs(csv_path: str) -> List[Song]:
        songs = []
        with open(csv_path, 'r', newline='') as song_file:
            songreader = csv.DictReader(song_file)
            for row in songreader:
                songs.append(Song.from_row(row))

        print(f"Loading songs from {csv_path}...")
        return songs

    def score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        w1, w2, w3, w4 = .325, .3, .25, .125
        reasons = []

        fav_genre = user.favorite_genre.lower()
        fav_mood = user.favorite_mood.lower()

        if fav_genre == song.genre:
            genre_match = 1
            reasons.append("Matched genre taste")
        else:
            genre_match = 0
            reasons.append("Did not match genre taste")

        if fav_mood == song.mood:
            mood_match = 1
            reasons.append("Matched mood taste")
        else:
            mood_match = 0
            reasons.append("Did not match mood taste")

        if user.target_energy > 1:
            target_energy = 1
        else:
            target_energy = abs(float(user.target_energy))
        if abs(target_energy - song.energy) <= .5:
            reasons.append(f"Song energy off by {abs(target_energy - song.energy):.2f}")
        else:
            reasons.append("Did not match target energy")

        if user.likes_acoustic == True and song.acousticness >= .5:
            acoustic_match = 1
            reasons.append("Matched acoustic taste")
        elif user.likes_acoustic == False and song.acousticness < .5:
            acoustic_match = 1
            reasons.append("Matched acoustic taste")
        else:
            acoustic_match = 0
            reasons.append("and did not match acoustic taste")

        score = w1*(genre_match) + w2*(mood_match) + w3*(1 - abs(song.energy - target_energy)) + w4*(acoustic_match)

        return (score, reasons)

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = [(song, self.score_song(user, song)[0]) for song in self.songs]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, _ in scored[:abs(k)]]
