import anthropic
from knowledge_base import retrieve_context

client = anthropic.Anthropic()

USE_LLM = True



def explanation_generator(user_prefs, song, score, reasons):
    genre_text, mood_text = retrieve_context(song['genre'], song['mood'])
    prompt = f"{song['title']} scored {score:.2f} because: {reasons}. Give positive factors first, then negative factors, then give a summary. In your summary include your interpretation of {genre_text} and {mood_text}. Do not use emojis or ask user questions. Add a new line at the end of the summary."
    if not USE_LLM:
        return "[stub] " + prompt 
    else:
        response = client.messages.create(
            model = "claude-haiku-4-5",
            max_tokens = 350,
            messages = [{"role": "user", "content": prompt}]
        )

        text = next(block.text for block in response.content if block.type == "text")

        return text
