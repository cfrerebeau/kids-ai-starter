"""Talks to the real internet. Prints something different each time."""

import json
import urllib.request

# This is a public API. No key needed. It gives you a random useless fact.
URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

print("Asking the internet for a random fact...")
print()

# Send a request to the URL and read what comes back.
response = urllib.request.urlopen(URL, timeout=5)

# The reply is JSON text. Turn it into something Python can use (a dict).
data = json.loads(response.read())

# The fact text lives under the "text" key.
fact = data["text"]

print(f"   {fact}")
print()

# TODO(you): change the URL above to a different public API.
# Try: https://dog.ceo/api/breeds/image/random  (returns a dog image URL)
# Or:  https://api.adviceslip.com/advice         (returns random advice)
# You'll need to change which key the code reads out of the JSON.
