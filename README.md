# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

In my system each song contains the name, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The UserProfile object stores the users favorite genre, mood, preferred energy, and whether they like acoustics or not. The system computes a score by using this formula: "score = w1*(genre match) + w2*(mood match) + w3*(1 - |energy - target_energy|) + w4*(acoustic match)", where genre, mood, target energy, and acoustic match are taken from the UserProfile object. For the weights, genre/w1=0.4, mood/w2=0.3, energy/w3=0.2, acousticness/w4=0.1. The songs are chosen to be recommended by ranking each song based on how high their score is(max score of 1). The Recommender object then shows and explains the recommendation and rankings.

Bias - This system heavily favors genre and does not represent acoustics as much as others when some people would prefer acoustics over genre.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

==================================================
User Profile
==================================================
Favorite Genre:  hip hop
Favorite Mood:   happy
Target Energy:   0.7
Likes Acoustic:  True

==================================================
Top 5 Recommendations
==================================================

1. City Lights Anthem - Rhea Voss
   Score: 0.57
   Reasons:
     - Matched genre taste
     - Did not match mood taste
     - Did not match acoustic taste

2. Rooftop Lights - Indigo Parade
   Score: 0.49
   Reasons:
     - Did not match genre taste
     - Matched mood taste
     - Did not match acoustic taste

3. Sunrise City - Neon Echo
   Score: 0.48
   Reasons:
     - Did not match genre taste
     - Matched mood taste
     - Did not match acoustic taste

4. Dust Road Home - Callum Briar
   Score: 0.26
   Reasons:
     - Did not match genre taste
     - Did not match mood taste
     - Matched acoustic taste

5. Wildflower Trail - Given River
   Score: 0.25
   Reasons:
     - Did not match genre taste
     - Did not match mood taste
     - Matched acoustic taste


Loading songs from data/songs.csv...
Loaded Songs: 20

==================================================
User Profile
==================================================
Favorite Genre:  hip hop
Favorite Mood:   happy
Target Energy:   0.7
Likes Acoustic:  True

==================================================
Top 1 Recommendations
==================================================

1. City Lights Anthem - Rhea Voss
   Score: 0.43
   Reasons:
     - Matched genre taste
     - Did not match mood taste
     - Did not match acoustic taste

==================================================
User Profile
==================================================
Favorite Genre:  pop
Favorite Mood:   chill
Target Energy:   0.4
Likes Acoustic:  False

==================================================
Top 1 Recommendations
==================================================

1. Sunrise City - Neon Echo
   Score: 0.54
   Reasons:
     - Matched genre taste
     - Did not match mood taste
     - Matched acoustic taste

==================================================
User Profile
==================================================
Favorite Genre:  synthwave
Favorite Mood:   romantic
Target Energy:   0.2
Likes Acoustic:  True

==================================================
Top 1 Recommendations
==================================================

1. Night Drive Loop - Neon Echo
   Score: 0.45
   Reasons:
     - Matched genre taste
     - Did not match mood taste
     - Did not match acoustic taste

==================================================
User Profile
==================================================
Favorite Genre:  country
Favorite Mood:   playful
Target Energy:   0.9
Likes Acoustic:  True

==================================================
Top 1 Recommendations
==================================================

1. Dust Road Home - Callum Briar
   Score: 0.60
   Reasons:
     - Matched genre taste
     - Did not match mood taste
     - Matched acoustic taste

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

System doesn't understand lyrics and also favors genre and mood over all other features.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Recommender use a scoring system to turn data into predictions. The recommender would have a dataset to refer to. The user then inputs their preferences. The recommender compares the preferences to each song to see how well it matches. The songs features are compared to the user's preferences and it is scored based on the weight of each feature, decided by the recommender, added together. After the song is scored, the songs are ordered by score, highest to lowest, the higher the score means the recommender thinks the user will like it more.

Bias/unfairness comes into systems like this because of the weight of each feature of a song judged. The weights are decided by the developer of the code, who may have genre has the most weighted feature, however, a user may prefer the acousticness over everything, which would make that recommender inaccurate to them.



