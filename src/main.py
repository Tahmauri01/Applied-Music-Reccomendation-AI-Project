"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded Songs: {len(songs)}")

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    taste_profile = {
        "favorite_genre": "hip hop",
        "favorite_mood": "happy",
        "target_energy": 0.7,
        "likes_acoustic": True,
    }

    recommendations = recommend_songs(taste_profile, songs, k=5)

    print("\n" + "=" * 50)
    print("User Profile")
    print("=" * 50)
    print(f"Favorite Genre:  {taste_profile['favorite_genre']}")
    print(f"Favorite Mood:   {taste_profile['favorite_mood']}")
    print(f"Target Energy:   {taste_profile['target_energy']}")
    print(f"Likes Acoustic:  {taste_profile['likes_acoustic']}")

    print("\n" + "=" * 50)
    print(f"Top {len(recommendations)} Recommendations")
    print("=" * 50)

    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"\n{rank}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split(", "):
            print(f"     - {reason}")


if __name__ == "__main__":
    main()
