"""
Reference knowledge base for RAG-based explanations.

GENRE_INFO and MOOD_INFO map each genre/mood value found in data/songs.csv
to a short reference blurb describing its typical musical characteristics.
Used by explanation_generator() to ground LLM explanations in more context
than just the raw score and reasons.
"""

GENRE_INFO = {
    "R&B": "R&B centers on smooth, soulful vocals over moderate energy grooves, often with romantic or sensual themes and a fair amount of acoustic warmth.",
    "acoustic": "Acoustic music relies on unamplified instrumentation, favoring low energy and very high acousticness over electronic production.",
    "ambient": "Ambient music is built for atmosphere over rhythm, with low energy, minimal danceability, and very high acousticness or texture.",
    "blues": "Blues carries a melancholic, expressive weight through guitar or piano-driven progressions, moderate acousticness, and modest energy.",
    "classical": "Classical music spans orchestral and chamber compositions, generally low energy and danceability with near-total acousticness.",
    "country": "Country blends storytelling vocals with acoustic and steel-guitar instrumentation, moderate energy, and a nostalgic or heartfelt tone.",
    "disco": "Disco is built for the dancefloor: high danceability, upbeat tempo, and joyful, high-valence energy with a polished production sheen.",
    "dubstep": "Dubstep features heavy bass drops and syncopated rhythms, with high energy, low valence, and minimal acousticness.",
    "electronic": "Electronic music covers a wide range of synthesized, production-driven styles, generally high energy and danceability with low acousticness.",
    "folk": "Folk emphasizes acoustic instrumentation and lyrical storytelling, with moderate energy and a nostalgic or peaceful character.",
    "funk": "Funk is groove-first: syncopated basslines, high danceability, and confident, playful energy.",
    "gospel": "Gospel combines uplifting vocal harmonies with moderate-to-high energy and a hopeful, joyful emotional core.",
    "grunge": "Grunge pairs distorted guitars with raw, unpolished vocals, high energy, and a moody or angry undertone.",
    "hip hop": "Hip hop emphasizes rhythmic vocal delivery over a strong beat, with high danceability and low acousticness.",
    "house": "House music is four-on-the-floor dance music: high tempo, high danceability, and euphoric or energetic energy.",
    "indie pop": "Indie pop favors melodic, guitar- or synth-driven songwriting with moderate-to-high energy and a dreamy or nostalgic tone.",
    "jazz": "Jazz is improvisational and harmonically rich, generally moderate energy with high acousticness and a relaxed or sophisticated feel.",
    "k-pop": "K-pop combines polished, high-energy production with strong danceability and confident, upbeat vocal performances.",
    "latin": "Latin music emphasizes rhythmic percussion and danceability, with energetic, joyful, or romantic emotional themes.",
    "lofi": "Lofi is low-energy, high-acousticness background music, designed for chill focus rather than danceability.",
    "metal": "Metal is defined by distorted guitars and aggressive delivery, with very high energy and tempo and very low acousticness.",
    "new age": "New age music prioritizes calm, meditative textures, with very low energy and danceability and near-total acousticness.",
    "pop": "Pop favors catchy, accessible songwriting with high energy, high valence, and strong danceability.",
    "punk": "Punk is fast, aggressive, and stripped-down, with very high energy and tempo and a rebellious or defiant tone.",
    "reggae": "Reggae carries an offbeat rhythmic groove with moderate energy and a relaxed, playful, or happy character.",
    "rock": "Rock centers on guitar-driven instrumentation with high energy and moderate-to-low acousticness, ranging from intense to angry in tone.",
    "ska": "Ska blends upbeat offbeat rhythms with horns and high energy, often playful or rebellious in tone.",
    "soul": "Soul pairs emotive vocals with moderate energy and moderate acousticness, often romantic or heartfelt in theme.",
    "synthwave": "Synthwave uses retro-styled synthesizers over moderate-to-high energy, often moody or nostalgic in tone with low acousticness.",
    "techno": "Techno is repetitive, hypnotic dance music with high tempo and energy and very low acousticness.",
    "trap": "Trap features heavy sub-bass and sparse hi-hat-driven beats, with moderate-to-high energy and low acousticness.",
}

MOOD_INFO = {
    "aggressive": "Aggressive tracks push high energy and intensity, typically with low valence.",
    "angry": "Angry tracks combine high energy with low valence, often carried by distorted or forceful instrumentation.",
    "calm": "Calm tracks favor low energy and a settled, even emotional tone.",
    "chill": "Chill tracks stay low-to-moderate in energy with a relaxed, easygoing feel.",
    "confident": "Confident tracks carry assertive energy with moderate-to-high valence.",
    "dark": "Dark tracks lean toward low valence with a brooding or tense atmosphere.",
    "defiant": "Defiant tracks combine high energy with a rebellious, pushback-oriented tone.",
    "dramatic": "Dramatic tracks build emotional intensity, often with wide dynamic range.",
    "dreamy": "Dreamy tracks favor a hazy, atmospheric quality with low-to-moderate energy.",
    "energetic": "Energetic tracks are high in energy and tempo, built to feel lively and driving.",
    "euphoric": "Euphoric tracks combine high energy with high valence for an uplifting, elated feel.",
    "focused": "Focused tracks stay low-key and steady, designed to support concentration rather than draw attention.",
    "groovy": "Groovy tracks emphasize rhythmic feel and danceability with confident, upbeat energy.",
    "happy": "Happy tracks carry high valence, an upbeat and positive emotional tone.",
    "heartfelt": "Heartfelt tracks emphasize sincere, emotionally direct expression, often at moderate energy.",
    "hopeful": "Hopeful tracks combine moderate-to-high valence with an optimistic, forward-looking feel.",
    "intense": "Intense tracks push high energy with a driving, urgent quality.",
    "joyful": "Joyful tracks carry high valence and an exuberant, celebratory tone.",
    "melancholic": "Melancholic tracks favor low valence with a wistful or sorrowful emotional tone.",
    "moody": "Moody tracks sit at low-to-moderate valence with an introspective or brooding feel.",
    "nostalgic": "Nostalgic tracks evoke a sentimental, reflective longing for the past.",
    "peaceful": "Peaceful tracks are low in energy with a settled, tranquil emotional tone.",
    "playful": "Playful tracks carry high valence with a light, fun, and energetic character.",
    "rebellious": "Rebellious tracks combine high energy with a defiant, anti-establishment attitude.",
    "relaxed": "Relaxed tracks favor low-to-moderate energy with an unhurried, easygoing quality.",
    "reverent": "Reverent tracks carry a solemn, respectful, and uplifting emotional tone.",
    "romantic": "Romantic tracks emphasize intimate, affectionate emotional themes at moderate energy.",
    "sensual": "Sensual tracks carry a smooth, intimate quality at moderate energy.",
    "sophisticated": "Sophisticated tracks favor a polished, refined emotional and stylistic tone.",
    "weary": "Weary tracks carry a low-energy, worn-down or resigned emotional quality.",
}

def retrieve_context(genre, mood):
    genre_text = GENRE_INFO.get(genre, f"No specific reference info for the '{genre}' genre.")
    mood_text = MOOD_INFO.get(mood, f"No specific reference info for the '{mood}' mood.")
    return genre_text, mood_text
