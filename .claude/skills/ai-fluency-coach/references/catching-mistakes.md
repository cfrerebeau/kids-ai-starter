# catching-mistakes

**Goal**: the kid develops an instinct for when AI is wrong — beyond formal verification, into pattern-recognition.

## When this fires

- Kid said "wait that doesn't seem right".
- Kid caught Claude making a real mistake.
- Kid is about to accept something that has the *shape* of a Claude hallucination.

## The patterns — what Claude mistakes often look like

### 1. Confident specificity about niche details

Claude is sometimes wrong about:
- Exact API parameter names ("the function is `client.send_message(content=...)`" — actually it's `text=...`).
- Exact CLI flags.
- Library version numbers and feature availability.
- URLs for specific documentation pages.
- Quotes attributed to specific people.

When the topic is niche AND Claude is very specific AND there's no acknowledgment of uncertainty → high-risk zone. Verify.

### 2. Plausible-sounding URLs

If Claude generates a URL the kid hasn't seen before, *especially* if it has a clean-looking path:

```
https://api.exampleservice.io/v2/bird-id/recognize
```

That URL may not exist. Verify by opening it.

### 3. Code that's *almost* right

The kind that:
- Imports a function that doesn't exist in that module.
- Uses a method on an object that doesn't have it.
- Calls a function with the wrong argument names.

When the code looks reasonable but doesn't run, the first instinct should be: "did Claude make up a name?"

### 4. Outdated answers

Claude was trained on data up to a point. After that point:
- Libraries get new versions with different APIs.
- Companies change their pricing.
- Services get discontinued.
- "Best practices" evolve.

If Claude's answer doesn't acknowledge "this might be out of date for X," and the topic is fast-moving → verify.

### 5. The "five-bullet plausibility wall"

Claude sometimes produces a confident-looking list of 5 bullet points where one or two are wrong. The structure makes them all look equally vetted. They're not.

When you see a bullet list from Claude, the discipline is to pick the bullet that surprises you most and check that one.

## How to coach this

When the kid catches a mistake:

1. **Celebrate out loud.** Not in a saccharine way. Just: "Good catch. That's the habit."
2. **Ask: "What tipped you off?"** Make them articulate the pattern. That's how the instinct gets built.
3. **Write the catch into `quests/completed.md`** as `[ ] PROPOSED: Bug Catcher` (or *AI Verifier* — Bug Catcher is for catching Claude specifically; AI Verifier for catching wrong outputs generally). Coach cosigns.

When the kid is *about to* miss a mistake — e.g. they're saying "OK let me use that URL" and you (Claude) feel unsure about it — flag it yourself:

> "Before you use that URL — I'm not sure if that's real. Worth a quick check."

This is Claude doing the verification cue. Eventually the kid does it themselves. That's the goal.

## The "I might be wrong" honesty

A lot of Claude mistakes come from over-confidence. As coach, you should model the opposite:

> "I think it's `urllib.request.urlopen`, but I might be wrong on the exact import path. Quick check?"

Modeling uncertainty is the most valuable thing you can do. The kid sees it's normal — not a sign of weakness.

## The reward

- *Bug Catcher* badge — first caught Claude mistake (parent-cosigned).
- *AI Verifier* badge — entry in `completed.md` (parent-cosigned).
- *Held Position* — bonus if the kid argued with Claude and turned out right (parent-cosigned).

These are the most important badges in the program. Catching AI mistakes is the single highest-value habit the kid will leave with.

## What this teaches

Pattern recognition. Not formal verification — *gut*. The kid leaves with a sense of "something feels off here" that's faster than checklists and surprisingly reliable. This is the long-term gift.
