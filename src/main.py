"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
from llm_explainer import explanation_generator


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded Songs: {len(songs)}")

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    taste_profile_1 = {
        "favorite_genre": "hip hop",
        "favorite_mood": "happy",
        "target_energy": 0.7,
        "likes_acoustic": True,
    }

    taste_profile_2 = {
        "favorite_genre": "pop",
        "favorite_mood": "chill",
        "target_energy": 0.4,
        "likes_acoustic": False,
    }

    taste_profile_3 = {
        "favorite_genre": "synthwave",
        "favorite_mood": "romantic",
        "target_energy": 0.2,
        "likes_acoustic": True,
    }

    taste_profile_4 = {
        "favorite_genre": "country",
        "favorite_mood": "playful",
        "target_energy": 0.9,
        "likes_acoustic": True,
    }

    recommendations = recommend_songs(taste_profile_1, songs, k=5)
    # recommendations = recommend_songs(taste_profile_2, songs, k=5)
    # recommendations = recommend_songs(taste_profile_3, songs, k=5)
    # recommendations = recommend_songs(taste_profile_4, songs, k=5)


    print("\n" + "=" * 50)
    print("User Profile")
    print("=" * 50)
    print(f"Favorite Genre:  {taste_profile_1['favorite_genre']}")
    print(f"Favorite Mood:   {taste_profile_1['favorite_mood']}")
    print(f"Target Energy:   {taste_profile_1['target_energy']}")
    print(f"Likes Acoustic:  {taste_profile_1['likes_acoustic']}")

    print("\n" + "=" * 50)
    print(f"Top {len(recommendations)} Recommendations")
    print("=" * 50)

    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        # print(f"\n{rank}. {song['title']} - {song['artist']}")
        # print(f"   Score: {score:.2f}")
        # print("   Reasons:")
        # for reason in explanation.split(", "):
        #     print(f"     - {reason}")


        ai_explanation = explanation_generator(taste_profile_1, song, score, explanation)
        print(ai_explanation)


if __name__ == "__main__":
    main()
