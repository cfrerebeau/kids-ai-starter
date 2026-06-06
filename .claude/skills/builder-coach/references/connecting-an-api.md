# connecting-an-api

**Goal**: the kid's app pulls real-world data from a real API. Earns relevant XP and reinforces *AI Interrogator* / *AI Verifier* habits.

## Why this matters

Apps that don't reach the world are toys. Apps that reach the world via an API are real. This step takes the kid from "Streamlit can do colors" to "I can plug my app into actual data — bird sightings, train times, weather, news, anything."

## Sequence

### Step 1 — Pick an API together

Ask: "What real data would make your app feel real?" Examples by project type:

- Birds → eBird API, iNaturalist API, Macaulay Library (audio).
- Transport → SNCF Connect API, Citymapper, OpenStreetMap routes, GTFS feeds.
- Generic → dog.ceo (dog photos), open-meteo (weather), wikipedia REST.

Have **the kid** pick. Don't decide for them.

### Step 2 — Check the API together

Open the API docs together. Walk through:
- Does it need a key? (Often yes for serious APIs.)
- What URL do you hit?
- What does it return — JSON, XML, something else?
- Are there rate limits?

If a key is needed → parent-flag (account signup). Use `.env` for the key. Never paste keys into chat.

### Step 3 — Test the API in isolation

Before integrating into the app, have the kid write a tiny standalone script that just hits the API and prints the response:

```python
# TODO(you): change the URL to the real one for your API.
import urllib.request, json

URL = "https://api.example.com/something"

with urllib.request.urlopen(URL) as r:
    data = json.loads(r.read())

print(data)
```

Run it. Look at the data. **This is the moment to verify** — does what the API returned match what the docs said? AI sometimes misremembers API shapes. If you (Claude) told them what to expect, did you get it right? If not — *AI Verifier* progress.

### Step 4 — Plug into the app

Take the working API call and put it into the Streamlit app. Render something visible from the response.

## Concepts touched

- Where code runs (the API call runs server-side — name it). Link [concepts/where-code-runs.md](../../../concepts/where-code-runs.md).
- Functions (likely): wrap the API call in a function. Link [concepts/functions.md](../../../concepts/functions.md) — possible *Function Caller* badge.

## When to award XP

50 XP for "Real API connected and rendered" — there must be visible output in the app that comes from the API.

## Sycophancy check

If the kid says "cool it worked!" after seeing data — ask "is the data right? Pick one item and check against another source." Train verification reflex on real data.

## Parent-flags

- API requires signup → parent creates account.
- API requires payment → parent decides.
- API key handling → `.env` discipline (`safety/README.md` rule #4).
