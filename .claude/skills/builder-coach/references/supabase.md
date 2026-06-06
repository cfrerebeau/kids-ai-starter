# supabase

**Goal**: the kid's app saves data that survives between visits. **Requires parent-assist for account creation.**

## Prerequisites — verify before starting

Don't do this just because the kid asks. They should have:

- A small-app that works without persistence.
- A concrete answer to: "What's a piece of data that NEEDS to survive past closing the tab?" (A user's submission, a saved list, etc.)
- Evidence that at least one user has used the app and asked for data to persist, OR a self-evident persistence need (e.g. the app keeps a personal log).

If they don't have these → route back to `small-app` and ask "where does this break without persistence?"

## Sequence

### Step 1 — Parent-assist account creation

🛑 **Raise the parent-flag.** Coach needs to:

1. Create a free Supabase account at supabase.com.
2. Create a new project (free tier is fine).
3. Save the project URL and `anon` public key.

Note: the `anon` key is OK to use in client-side code. The `service_role` key is NOT — never share it, never put it in code that ships.

### Step 2 — Install the library

🛑 **Parent-assist:**

```
pip install supabase
```

### Step 3 — `.env` setup

In the project folder, create a `.env` file (gitignored by default):

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

Load it in Python:

```python
import os
from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
```

(They may need `pip install python-dotenv`.)

### Step 4 — Create a table

In Supabase web UI: Table Editor → New Table. Walk the kid through choosing column names. Start simple — `id`, `created_at`, and one or two data columns.

### Step 5 — Read + write from the app

```python
from supabase import create_client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# TODO(you): write a row that's specific to your project.
supabase.table("your_table").insert({"field": "value"}).execute()

# Read rows
rows = supabase.table("your_table").select("*").execute()
```

Wire this into the app. After saving a row, close the browser, reopen — the data is still there. That's persistence.

## Concepts touched

- Persistence — link [concepts/persistence.md](../../../concepts/persistence.md). Possible *The Memory Place* badge.
- Where code runs — the database is server-side. Name this.

## When to award XP

100 XP for "Supabase integrated (data persists)" when:
- A row is written from the app.
- The app reads it back after a restart.

## Sycophancy check

After it works: "Now break it. What happens if two people use the app at the same time? What happens if someone refreshes mid-save?" Get them thinking about edge cases.

## Cost watch

Free tier is generous but has limits (rows, bandwidth, storage). If the app starts looking popular, parent-flag for the conversation about upgrades.
