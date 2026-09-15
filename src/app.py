import streamlit as st
from recommender import Recommender, UserProfile
from llm_explainer import explanation_generator

st.set_page_config(page_title="Music Recommender")
st.title("Music Recommender")


@st.cache_resource
def get_recommender() -> Recommender:
    songs = Recommender.load_songs("data/songs.csv")
    return Recommender(songs)


recommender = get_recommender()

available_genres = sorted({song.genre for song in recommender.songs})
available_moods = sorted({song.mood for song in recommender.songs})

if "taste_profile" not in st.session_state:
    st.session_state.taste_profile = None
if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

with st.form("taste_profile_form"):
    favorite_genre = st.selectbox("Favorite genre", available_genres)
    favorite_mood = st.selectbox("Favorite mood", available_moods)
    target_energy = st.slider("Target energy", 0.0, 1.0, 0.5)
    likes_acoustic = st.checkbox("Do you like acoustic songs?")
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    st.session_state.taste_profile = UserProfile(
        favorite_genre=favorite_genre,
        favorite_mood=favorite_mood,
        target_energy=target_energy,
        likes_acoustic=likes_acoustic,
    )
    st.session_state.recommendations = recommender.recommend(
        st.session_state.taste_profile, k=5
    )

taste_profile = st.session_state.taste_profile
recommendations = st.session_state.recommendations

if taste_profile and recommendations:
    st.header("User Profile")
    st.write(f"**Favorite Genre:** {taste_profile.favorite_genre}")
    st.write(f"**Favorite Mood:** {taste_profile.favorite_mood}")
    st.write(f"**Target Energy:** {taste_profile.target_energy}")
    st.write(f"**Likes Acoustic:** {taste_profile.likes_acoustic}")

    st.header(f"Top {len(recommendations)} Recommendations")
    for rank, song in enumerate(recommendations, start=1):
        score, reasons = recommender.score_song(taste_profile, song)
        explanation = ", ".join(reasons)
        ai_explanation = explanation_generator(taste_profile, song, score, explanation)

        st.subheader(f"{rank}. {song.title} - {song.artist}")
        with st.expander("Summary"):
            st.write(ai_explanation)
