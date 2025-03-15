from openai import OpenAI

def translate_chatgpt(text):
    """
    Translates the given text to Indonesian using the OpenAI GPT-4 model.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The translated text in Indonesian.
    """
    # Function definition
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o",
        input=f"Translate to Indonesian (do not include \" in the translation): \"{text}\"",
    )
    return response.output_text