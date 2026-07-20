# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Song Recommender 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The recommender is designed to match the user's preferences to the songs that the system has access to. It assumes that the user's information is accurate but also that they only really have one type of favorite in a category. This is for a classroom experience however this is able to be scaled to use by real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Each song has features that are used to identify it: id, title, artist, genre, mood,energy, tempo_bpm, valence, danceability, acousticness. The preferences taken from the user is the genre, mood, energy, and acousticness. The model turns this into a score by weighing each feature differently then comparing it to the user's preference. Genre is .325, mood is .3, energy is .25, and acousticness is .125. At the start the weights were different,  genre was 0.4, mood was 0.3, energy was 0.2, acousticness was 0.1.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are 20 songs in the catalog. There is a variety of genres and moods including pop happy, lofi chill, synthwave moody, reggae playful, and much more. At first there was only 10 songs in the catalog, however this was too small of a number to work with so it was changed to 20. Ths data is missing several combinations of music and genre, which can be easily added.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system worked well when the user has a genre and mood preference that closely matches a specific song. This is because genre and mood are weighed the most. I could always guess that the number one recommended song would share the same genre as the user's preference if that genre existed in the dataset.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Energy and acoustic are the two lowest weighted scores. This means that people who prefer these two attributes of a song are underrepresented. The system will not choose the correct songs they would like most of the time.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

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

I tested these four profiles. I looked to see if the genre and mood mostly matched what the user was looking for since those were the two with the highest ratings. I was surprised to see scores so low, however I realize that the test accounts are pretty diverse and mostly do not match a certain song.

For the actual output, energy matching with the mood mattered, since that is how the songs are usually created. That is why City Lights Anthem shows up for people who like high energy and high energy moods.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

More features I would like to add:
 - more than one user preference
 - real songs in the dataset
 - more features for user to prefer
 - UI implementation
 - better weight distribution
 - add more songs to dataset

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  


Learned recommenders use a point system to judge and rank which songs would be best for you based on if your preferences match the song. Something interesting I found was that there is no 100 percent correct point system, it is really up to the developer and what they want to recommender to judge preference. This also made me realize how complex music recommendation applications are since they take much more into account than just the four preferences used in this system.