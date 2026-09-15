"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import Recommender, UserProfile
from llm_explainer import explanation_generator


def main() -> None:
    songs = Recommender.load_songs("data/songs.csv")
    print(f"Loaded Songs: {len(songs)}")
    recommender = Recommender(songs)

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # taste_profile_1 = UserProfile(
    #     favorite_genre="hip hop",
    #     favorite_mood="happy",
    #     target_energy=0.7,
    #     likes_acoustic=True,
    # )

    # taste_profile_2 = UserProfile(
    #     favorite_genre="pop",
    #     favorite_mood="chill",
    #     target_energy=0.4,
    #     likes_acoustic=False,
    # )

    # taste_profile_3 = UserProfile(
    #     favorite_genre="synthwave",
    #     favorite_mood="romantic",
    #     target_energy=0.2,
    #     likes_acoustic=True,
    # )

    # taste_profile_4 = UserProfile(
    #     favorite_genre="country",
    #     favorite_mood="playful",
    #     target_energy=0.9,
    #     likes_acoustic=True,
    # )

    favorite_genre = input("Favorite genre: ")
    favorite_mood = input("Favorite mood: ")
    target_energy = float(input("Target energy (0.0 - 1.0): "))
    likes_acoustic = input("Do you like acoustic songs? (y/n): ").strip().lower().startswith("y")

    taste_profile = UserProfile(
        favorite_genre=favorite_genre,
        favorite_mood=favorite_mood,
        target_energy=target_energy,
        likes_acoustic=likes_acoustic,
    )

    recommendations = recommender.recommend(taste_profile, k=5)

    print("\n" + "=" * 50)
    print("User Profile")
    print("=" * 50)
    print(f"Favorite Genre:  {taste_profile.favorite_genre}")
    print(f"Favorite Mood:   {taste_profile.favorite_mood}")
    print(f"Target Energy:   {taste_profile.target_energy}")
    print(f"Likes Acoustic:  {taste_profile.likes_acoustic}")

    print("\n" + "=" * 50)
    print(f"Top {len(recommendations)} Recommendations")
    print("=" * 50)

    for rank, song in enumerate(recommendations, start=1):
        score, reasons = recommender.score_song(taste_profile, song)
        explanation = ", ".join(reasons)
        # print(f"\n{rank}. {song.title} - {song.artist}")
        # print(f"   Score: {score:.2f}")
        # print("   Reasons:")
        # for reason in reasons:
        #     print(f"     - {reason}")


        ai_explanation = explanation_generator(taste_profile, song, score, explanation)
        print(ai_explanation)


if __name__ == "__main__":
    main()
