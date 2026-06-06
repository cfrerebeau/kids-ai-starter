# Where Does Code Run?

## The two roles: client and server

Almost every real app on the internet has two parts that talk to each other.

- **Client** = the program in front of the user. For a website, that's their **browser** — Chrome, Safari, whatever they're using. Every person using your app has their own client. Their own browser, their own screen, their own tab.
- **Server** = one place, somewhere on the internet, that holds your app's code and data. Just *one*. Every client (every user) connects to the same server.

## The picture

```
       CLIENTS                              SERVER
   (each user's browser)               (one place, on the internet)

   User A  ─────── request ────────►
                                          [ your app code ]
            ◄────── response ────────     [ your data ]
                                            ↑
                                            │  every user
   User B  ─────── request ────────►        │  hits the same
                                            │  server
            ◄────── response ────────     [ same code ]
                                          [ same data ]
   User C  ─────── request ────────►
            ◄────── response ────────     [ same server ]
```

Every time a user clicks something, their browser sends a **request** to the server. The server reads it, does whatever your code says, and sends back a **response**. The browser shows the result.

## One server, many clients — why that matters

The asymmetry is the whole point.

- Each client only knows about itself. User A's browser has no idea User B exists.
- The server sees all of them. It's the only place that can know what's happening across users.

So if your app needs to **remember things between users** (User A submits something, User B sees it) — that has to live on the server. The browser alone can't do that. Each browser is alone.

## Why every real app needs both

- A **browser-only app** (just HTML + JavaScript): cool, fast, but can't share data between users. Once you close the tab, your work's gone.
- A **server-only app** (just Python on a server): does work, but has no way for a user to see or click anything. You'd have to read its output somewhere else.

Real apps mix the two: the browser provides what the user sees and clicks (the *UI*); the server provides what's the same across users (the *shared state*) and what needs to be safe (passwords, keys, anything secret).

## When the kid will care about this

- **First Streamlit app**: Streamlit runs *on a server*, but the user sees and clicks things *in their browser*. The two roles are at play even in your tiny first app.
- **First time saving data**: now you need the server to remember (database).
- **First time something has to be secret** (an API key, a password): it has to live on the server. Anything in the browser is visible to anyone who looks.

## How to earn the badge — *Where Does Code Run?*

Build **one thing that runs in a browser** (an HTML file the kid wrote, or a piece of JavaScript in `hello.html` the kid modified) AND **one thing that runs as a server-side script** (a Python file they wrote, or a Streamlit app). Show Claude both. **Explain in their own words which is which, and what would happen if you tried to do it the other way around** (e.g. "I couldn't put my API key in `hello.html` because then everyone could see it").

The badge isn't for owning both files — it's for being able to *explain the difference*.

## Going deeper (optional)

Some kids will want to actually **wire their own HTML up to their own Python**, not let Streamlit hide it. That's a real path — write a Python web server (FastAPI or Flask), write an HTML file with JavaScript that calls it (`fetch()`), and watch the two talk to each other.

It's more work than Streamlit but teaches the wiring directly. If the kid asks "how do I make MY html call MY python," that's the path. Tell Claude — there's room to go down that route.
