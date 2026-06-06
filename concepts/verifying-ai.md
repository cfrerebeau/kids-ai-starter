# Verifying AI

## The single most important habit

AI models — Claude included — sometimes confidently say things that are **wrong**. Not mostly wrong. Specifically wrong. A real-looking URL that doesn't exist. A function call with the wrong arguments. A "fact" that was true once and isn't anymore. A library that was renamed two years ago.

This isn't a bug you can wait for someone to fix. It's how language models work. They predict words that sound right. Sometimes the words that sound right are also true. Sometimes they're not.

## What verifying looks like

Three habits. Use them every time something feels load-bearing:

1. **Run it.** If Claude wrote code, run it before you say "thanks." Don't read it, judge it, accept it — run it. Tell Claude what actually happened, not what you expected.

2. **Search it.** If Claude gave you a fact or a stat, do one quick search. "Did this thing actually happen? Is this number right? Is this library still maintained?"

3. **Ask back.** "Are you sure?" / "Where did you get this?" / "What's a way this could be wrong?" Claude will often back off when asked — and you'll learn how confident it really was.

## What you learn from being burned

Every time you catch Claude in a mistake, you learn what mistakes look like. After a few catches, you start to **smell** when something's off, even before you check. That instinct is the goal.

## How to earn the badge — *AI Verifier*

Find a Claude output that was **wrong**. Anything — a fact, a URL that doesn't exist, code that fails, a confidently-stated thing that turns out to be made up. **Write it down** in `quests/completed.md` under a section called `AI mistakes I caught`. Note:

- What Claude said.
- How you found out it was wrong.

Your coach cosigns at Sunday review.
