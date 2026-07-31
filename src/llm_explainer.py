USE_LLM = False

def explanation_generator(user_prefs, song, score, reasons):
    if not USE_LLM:
        return f"[stub] {song['title']} scored {score:.2f} because: {reasons}"
    #Add real call later