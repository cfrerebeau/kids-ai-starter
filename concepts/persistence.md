# Persistence

## The problem

Run this:

```python
score = 0
score = score + 10
print(score)    # 10
```

Now run it again. What's the score? **10**. Not 20.

Every time the program runs, `score` starts at 0. Nothing the program does sticks around after it stops. The variable lives in the computer's memory, and that memory clears when the program exits.

This is the default. Code without persistence forgets everything.

## What persistence is

**Persistence is saving data somewhere that survives when the program stops.** A few ways:

- **A file** on disk: write to `data.txt`, read it next time.
- **A database**: a more organized way to save data, built for it. Examples: SQLite, Postgres, Supabase.
- **Browser localStorage**: a small slot of memory the browser keeps between visits. OK for tiny things, not for real apps.

Without one of these, every time the user closes your app, everything they did is gone.

## When you need it

- Your app remembers a user between visits → you need persistence.
- Multiple users see the same data → you need persistence (and probably a database).
- Anything saves automatically → persistence.

If you're building anything that should still be there tomorrow, the question isn't *if* you need persistence — it's *which kind*.

## How to earn the badge — *The Memory Place*

Build something that **saves data across runs**. Could be:

- A Python script that writes to a `.json` file and reads it back next time.
- A Streamlit app that uses a SQLite or Supabase table.
- A browser thing that uses `localStorage` (Claude will help).

Show Claude. Run it, close it, run it again. The data should still be there.
