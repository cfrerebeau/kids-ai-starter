# Where Does Code Run?

## Two places

Code can run in two main places. They behave very differently. Knowing which is which is one of the most useful things you'll learn.

### 1. In your browser ("client-side")

When you open `tinker/hello.html`, your browser reads the HTML and the JavaScript inside it. The code runs **on your machine, inside the browser tab**.

- Fast — no internet round trip.
- Anyone using your app can see your code (right-click → "View source").
- **Not secure for secrets.** Never put an API key or password in browser-side code. Anyone can read it.
- Things you do here disappear when the tab closes (unless you do extra work).

### 2. On a server ("server-side")

When you run `python tinker/api_demo.py`, the code runs **on your computer as a script**. When you ship a Streamlit or Supabase app, the code runs on a server you don't see. Users hit it over the internet.

- Slower (network).
- **Secrets are safe** here — users can't see the code.
- You can keep data across users (in a database).

## Why this matters

Building a real app means knowing which work happens where. A login form goes through the server (so passwords stay private). A button animation runs in the browser (because it's just visuals). Putting a password check in the browser is a beginner mistake — and a real security problem.

## How to earn the badge — *Where Does Code Run?*

Build **one thing in a browser context** (HTML/JS, or a Streamlit widget rendering in the page) AND **one thing in a script/server context** (a Python script, or a Streamlit backend function). Show Claude both. Explain which runs where.
