import requests

def translate_ollama(text):
    """
    Translates the given text to Indonesian using the Ollama API.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The translated text in Indonesian.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
        KeyError: If the response does not contain the expected 'response' key.

    Example:
        translated_text = translate_ollama("Hello, how are you?")
        print(translated_text)  # Output: "Halo, bagaimana kabarmu?"
    """
    url = "http://192.168.122.25:11434/api/generate"
    data = {
        "model": "mannix/llamax3-8b-alpaca",
        "prompt": f"Translate to Indo: \"{text}\"",
        "stream": False  # Set to True for streaming responses
    }

    response = requests.post(url, json=data)
    return response.json()['response']