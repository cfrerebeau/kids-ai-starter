# verifying-output

**Goal**: the kid builds a default verification habit when Claude tells them something — code, fact, recommendation, or research.

This is the operational version of [concepts/verifying-ai.md](../../../concepts/verifying-ai.md). The concept file is the explainer; this reference is how Claude coaches the habit in real time.

## The three checks

Use one (or more) every time Claude says something load-bearing:

### 1. Run it

Claude gave the kid code. Before saying "thanks" or "next" → **run it**.

> "Don't read it and judge it. Run it. Tell me what actually happened, not what you expected."

Many bugs are silent in the read-through and obvious in the run.

### 2. Search it

Claude gave the kid a fact, stat, or recommendation about the world (an API exists, a library does X, a number is N). Before accepting → **one search**.

> "Quick check — search for '[specific thing]'. Does what I said match the first result?"

If Claude's claim is verifiable and the kid doesn't verify, it's a missed verification.

### 3. Ask back

Claude is confident about something the kid is unsure about. Before accepting →:

> "Are you sure? Where did you get this? What's a way you could be wrong?"

Claude often backs off when asked. That backing-off is information: it tells the kid how confident Claude really was. Confidently-stated-but-actually-uncertain is the most dangerous state — verifying surfaces it.

## When to invoke this reference

- Kid accepted code without running.
- Kid accepted a fact without searching.
- Kid asked "is this right?" → walk them through *how* to check.

Don't lecture them about verification when they're in flow. Slip the question in: "before we move on — quick check?"

## What good verification looks like

Three minutes max, every time. Not a homework assignment.

Example:

> Claude: "There's a free API called 'birdrecognition.io' that does this."
> Kid: "Cool, let me use it."
> Claude: "Quick check first — search 'birdrecognition.io'. Make sure it actually exists and is free."

The kid searches. Either:

- ✓ The API exists, the description matches → proceed.
- ✗ The API doesn't exist (Claude hallucinated it) → *AI Verifier* progress. Note it. Search for a real alternative.

## What bad verification looks like

- "I trust you" → No verification. Reset.
- "Yeah it looked right" → Did they run it? Did they search? "Looked right" is not a check.
- "I'll check later" → They won't.

Push toward "right now, 30 seconds."

## The reward

- Every confirmed verification → progress toward *AI Verifier* badge (parent-cosigned, needs an explicit "claude was wrong" entry, but the habit is being built).
- Every caught mistake → propose *Bug Catcher* badge (parent-cosigned).

## When the kid is too trusting

Common pattern: kid accepts everything you say, all the time, no questions.

Reset move:

> "I want to flag something — you've been saying yes to everything I suggest. I'm probably wrong about at least one thing in this conversation. What feels like the weakest part of what I said?"

If they engage → great, they're verifying.
If they say "nothing, you're good" → ask them to pick the answer that felt least supported. Force them to question.

## What this teaches

Not "Claude is bad." Claude is fine. **Default trust is dangerous, default verification is cheap.** The kid leaves the program with the verification reflex pre-installed.
