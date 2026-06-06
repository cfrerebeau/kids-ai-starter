"""Talks to the real internet. Prints something different each time."""

import json
import urllib.request

# This is a public API. No key needed. It gives you a random useless fact.
URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"


def get_random_fact():
    with urllib.request.urlopen(URL, timeout=5) as response:
        data = json.loads(response.read())
    return data["text"]


def main():
    print("Asking the internet for a random fact...")
    print()
    fact = get_random_fact()
    print(f"   {fact}")
    print()
    # TODO(you): change the URL above to a different public API.
    # Try: https://dog.ceo/api/breeds/image/random  (returns a dog image URL)
    # Or:  https://api.adviceslip.com/advice         (returns random advice)
    # You'll need to change which key the code reads out of the JSON.


if __name__ == "__main__":
    main()
