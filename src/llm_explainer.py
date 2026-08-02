import anthropic

client = anthropic.Anthropic()

USE_LLM = True



def explanation_generator(user_prefs, song, score, reasons):
    prompt = f"{song['title']} scored {score:.2f} because: {reasons}. Give positive factors first, then negative factors, then give a summary. Do not use emojis, ask user questions."
    if not USE_LLM:
        return "[stub] " + prompt 
    else:
        response = client.messages.create(
            model = "claude-haiku-4-5",
            max_tokens = 300,
            messages = [{"role": "user", "content": prompt}]
        )

        text = next(block.text for block in response.content if block.type == "text")

        return text
