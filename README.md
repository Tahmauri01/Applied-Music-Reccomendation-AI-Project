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

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



