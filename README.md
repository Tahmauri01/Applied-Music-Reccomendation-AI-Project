# 🎵 Music Recommender AI

## Project Summary

This project takes user taste profile including their favorite genre, mood, energy, and acousticness of a song. With this data, they are recommended their top k songs from a database of 200 songs, each song having it's own score. The higher the score the higher the rank. This recommendation includes an AI summary of positive and negative factors that contributed to the songs score.

---

## How The System Works

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
python src/main.py
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

(prompt = f"{song['title']} scored {score:.2f} because: {reasons}. Give positive factors first, then negative factors, then give a summary. In your summary include your interpretation of {genre_text} and {mood_text}. Do not use emojis or ask user questions. Add a new line at the end of the summary.")


==================================================
Top 5 Recommendations
==================================================
# Gilded Orbit - Score Analysis: 0.61

## Positive Factors
- Matched mood taste
- Matched acoustic taste

## Negative Factors
- Did not match genre taste
- Song energy off by 0.27

## Summary

Gilded Orbit received a moderate score of 0.61, driven by its successful alignment with your mood and acoustic preferences. However, the track fell short in two key areas: it didn't match your genre expectations, and its energy level was notably lower than your preferences by 0.27 points.

The mismatch suggests that while Gilded Orbit captures the acoustic qualities and emotional tone you're seeking, it may lack the energetic drive you typically enjoy. Your taste profile appears to favor music that combines storytelling vocals with acoustic and steel-guitar instrumentation—creating that moderate to higher-energy sound with a nostalgic or heartfelt tone characteristic of country music. Additionally, you gravitate toward happy, upbeat tracks that carry high valence and a positive emotional resonance. Gilded Orbit likely delivered on the acoustic and mood fronts but came across as too subdued in energy and potentially didn't fit your preferred genre framework.

To better match your taste, consider tracks that maintain the emotional depth and acoustic elements you appreciate while incorporating more vigorous energy and a brighter, more uplifting emotional quality.
# Broken Horizon - Score Analysis: 0.57

## Positive Factors
- Matched genre taste

## Negative Factors
- Did not match mood taste
- Song energy off by 0.03
- Did not match acoustic taste

## Summary
Broken Horizon achieved a moderate compatibility score of 0.57, with its primary strength being an alignment with your preferred genre. However, the track fell short in several key areas that prevented a higher rating. The mood and acoustic qualities did not resonate with your taste preferences, and the song's energy level deviated slightly from your ideal range by 0.03.

Based on your listening profile, you gravitate toward Hip hop tracks that prioritize rhythmic vocal delivery and strong beat composition, favoring high danceability paired with minimal acoustic elements. Additionally, you prefer confident tracks that project assertive energy through moderate-to-high emotional positivity. Broken Horizon appears to have missed these target characteristics, particularly in how it balances its acoustic elements and emotional tone relative to your established preferences.
# Violet Static Score Analysis: 0.56

## Positive Factors
- Matched genre taste: The track aligns well with your Hip hop preferences, delivering the rhythmic vocal delivery and strong beat foundation characteristic of the genre.

## Negative Factors
- Did not match mood taste: The track fails to capture the introspective or brooding atmosphere you were seeking.
- Song energy off by 0.07: The track's energy level slightly misaligns with your preferences, falling just outside your ideal range.
- Did not match acoustic taste: The acoustic properties of the song do not fit your listening expectations.

## Summary
Your moderate score of 0.56 reflects a mixed compatibility with this track. While it successfully delivers on Hip hop's core elements—emphasizing rhythmic vocal delivery over a strong beat with high danceability and low acousticness—it misses the mark on other important dimensions. The track's mood lacks the low-to-moderate valence with that introspective or brooding feel you find compelling in moody music. Additionally, the slightly elevated energy level and acoustic characteristics create friction with your preferences, preventing this from being a strong match despite the genre alignment. This suggests the track captures the sonic foundation you enjoy but fails to deliver the emotional depth and mood-driven qualities that would elevate it into your sweet spot.
# Velvet Meadow Score Analysis: 0.56

## Positive Factors
- Matched genre taste: The track aligns well with your Hip hop preferences

## Negative Factors
- Did not match mood taste: The song's emotional character does not fit your moody preferences
- Song energy off by 0.07: The track's energy level slightly deviates from your ideal specification
- Did not match acoustic taste: The acoustic properties of the song diverge from your preferences

## Summary

Velvet Meadow received a moderate score primarily because while it successfully captures the Hip hop genre you enjoy—emphasizing rhythmic vocal delivery over a strong beat with high danceability and low acousticness—it fails to deliver on the moody atmosphere you're seeking. Moody tracks typically sit at low-to-moderate valence with an introspective or brooding feel, qualities that this song lacks. Additionally, the track's energy level falls slightly outside your preferred range by 0.07, and its acoustic characteristics don't align with what you're looking for. To improve compatibility, consider tracks that blend Hip hop's rhythmic intensity with a more introspective, low-valence mood while reducing acoustic elements.
# Copper Wildfire - Score Analysis (0.55)

## Positive Factors
- Matched genre taste

## Negative Factors
- Did not match mood taste
- Song energy off by 0.09
- Did not match acoustic taste

## Summary

Copper Wildfire received a moderate score of 0.55, with one clear strength but multiple areas of misalignment. The track successfully matched your genre preference, which provides a solid foundation. However, the song fell short in three critical areas: it failed to deliver the mood you were looking for, the energy level deviated by 0.09 from your preferences, and the acoustic qualities didn't align with your taste.

Based on your profile, Hip Hop in your musical taste emphasizes rhythmic vocal delivery as the primary focus, complemented by a strong beat foundation. The genre is characterized by high danceability, which keeps the momentum energetic and propulsive, while maintaining low acousticness to preserve that polished, produced sound. Confident tracks within this context carry assertive energy with moderate-to-high valence, meaning they project self-assurance and positivity through their sonic delivery.

Copper Wildfire likely succeeded in its genre classification but may have leaned too heavily into acoustic elements, featured insufficient energy intensity, or missed the confident, assertive mood you typically prefer in Hip Hop selections.


---

## Experiments You Tried

The weight of each preference was changed repeatedly to see which combination would best fit. 

---

## Limitations and Risks

System doesn't understand lyrics and also favors genre and mood over all other features.

---

## Reflection

Recommender use a scoring system to turn data into predictions. The recommender would have a dataset to refer to. The user then inputs their preferences. The recommender compares the preferences to each song to see how well it matches. The songs features are compared to the user's preferences and it is scored based on the weight of each feature, decided by the recommender, added together. After the song is scored, the songs are ordered by score, highest to lowest, the higher the score means the recommender thinks the user will like it more.

Bias/unfairness comes into systems like this because of the weight of each feature of a song judged. The weights are decided by the developer of the code, who may have genre has the most weighted feature, however, a user may prefer the acousticness over everything, which would make that recommender inaccurate to them.



