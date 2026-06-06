# streamlit-hello

**Goal**: get Streamlit installed and the kid sees their own tiny web app running in a browser. **Requires parent-assist for the install step.**

## Sequence

### Step 1 — Parent-assist for install

🛑 **Raise the parent-flag.** Tell the kid: "Show this screen to your coach. We need them to install one thing."

The coach runs:

```
pip install streamlit
```

(Or `pip3 install streamlit` if they have multiple Pythons.)

Verify it worked:

```
streamlit --version
```

Should print a version number.

### Step 2 — Run the included example

Have the kid run:

```
streamlit run tinker/streamlit_hello.py
```

A browser tab opens with a simple page. Ask: "What did you see?"

### Step 3 — Modify it

Have the kid open `tinker/streamlit_hello.py` and change something. Suggestions in priority order:

- Change the title.
- Add another `st.write("...")` line.
- Add `st.slider("Pick a number", 0, 100)`.
- Add an image with `st.image("https://...")` using a URL they like.

After saving, Streamlit hot-reloads the browser. They see the change live.

### Step 4 — Name the concept

This is the kid's first taste of a **web app**. Name what just happened: the Python script is running on their machine; Streamlit turned it into a webpage their browser can show. Link [concepts/where-code-runs.md](../../../concepts/where-code-runs.md).

## TODO discipline

If you generate code for them to add, leave one TODO they must fill in. Don't write a full app for them at this stage.

## When to award XP

50 XP for "Streamlit hello running locally" — when they have it running AND they made at least one modification that took effect.

## Common pitfalls

- `streamlit: command not found` → pip install didn't work. Parent-flag.
- Browser doesn't open automatically → tell them the URL (it's printed in the terminal — usually `http://localhost:8501`).
- Kid gets curious about deployment ("how do I put this online?") → defer to `small-app` step first. Don't jump ahead.

## Sycophancy check

If they say "cool, what's next" after seeing the example without modifying — push back. "Change the title to something that's *you*. Then we move on."
