import random
import requests
import time
from translate import Translator


translator = Translator(to_lang="bn")

# URL to fetch the word list from
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"


response = requests.get(word_site)
WORDS = response.content.decode('utf-8').splitlines()


def show_word():
    word = random.choice(WORDS)

    # Translate the word to Bangla
    translation = translator.translate(word)

    print(f"Word: {word}")
    print(f"Meaning: {translation}")



while True:
    show_word()
    print("\nNext word in 3 seconds...\n")
    time.sleep(3)  # You can increase your delay time from here (3600 for 1 hour)
