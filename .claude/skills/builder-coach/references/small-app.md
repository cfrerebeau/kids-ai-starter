# small-app

**Goal**: the kid builds a single-screen Streamlit app for *their* project. Not a tutorial app, not the example — their thing.

## Prerequisites

- Streamlit hello working.
- A defined persona (at least a draft — see `entrepreneur-coach`).
- A clear answer to "what is the one thing this app does?"

If any are missing, route back. Don't build a small-app for an undefined problem.

## Sequence

### Step 1 — Sharpen the scope

Before any code, ask:

> "If your app could only do ONE thing, what would it be?"

Force a one-sentence answer. If they say "well, also..." — push back. *One* thing. The other stuff can come later.

Write this sentence into `me.md` under "My project" → "What I'm building."

### Step 2 — Decide what's on the screen

Three things, max:

- One input (what the user types or selects).
- One output (what the user sees).
- Maybe one button.

Sketch it on paper if the kid will go for it. Or describe it in words. Don't write code until they can describe what's on the screen.

### Step 3 — Write it together

The kid types. You suggest. You leave TODOs. The pattern:

```python
import streamlit as st

st.title("App Name Here")

# TODO(you): change the input label
user_input = st.text_input("What goes here?")

if user_input:
    # TODO(you): make this do the one thing your app does
    result = process(user_input)
    st.write(result)


def process(text):
    # placeholder — kid replaces this
    return f"You said: {text}"
```

The `process()` function is where the kid spends their time. That's the actual project logic.

### Step 4 — Run it. Show one person.

Once it runs, the *next* quest is showing it to one human (a friend, a sibling, a parent). NOT a stranger yet. We're testing reactions, not shipping.

After they show it: route to `entrepreneur-coach` → `first-test.md` for what to ask the person.

## Concepts touched

Probably variables, possibly a function, possibly a conditional. Name each one once as it comes up. Link concept files.

## When to award XP

- 50 XP for "Real API connected and rendered" if they connect to an external API at this step.
- 75 XP for "Small app shipped to one friend" when a non-family human has actually used it.

## Sycophancy check

If the kid says "and I want it to also do X, Y, Z" — say "save those for v2. What's the smallest version of just the one thing?" Scope-cutting is the lesson here, not engineering elegance.
