# python-hello

**Goal**: the kid asks you (Claude) to write a small Python script for something they care about. You write it. They read it, modify one piece, run it, and explain what each line does. Earns *I Know What Code Does*.

**The model is: Claude writes, kid directs.** Do NOT make the kid type Python from a blank file. That's unrealistic this early. The kid is the brain; you're the typist.

## Sequence

1. **Ask what they want their script to do.** Anything small. "Print my favorite 5 songs." "Tell me how many days until summer." "Ask my name and say hi back." Resist suggesting — let them pick something dumb if they want, as long as it's *theirs*.

2. **Write the script for them.** Use the Write tool. ≤10 lines if possible. Pick variable names and structure that fit what they asked. Leave ONE meaningful TODO they'll fill in (e.g. `# TODO(you): change this list to YOUR top 5`).

3. **Walk them through it line by line.** Read each line out loud (in chat). Say what it does in plain English. Don't dump the explanation all at once — go line, ask "does that make sense?", continue.

4. **Have them fill in the TODO.** They make the change themselves. Their hands on the keyboard for that one bit.

5. **Have them run it.** `python their_script.py`. They tell you what came out.

6. **Have them change one MORE thing on their own** — without asking you. A number, a string, anything. Predict what'll happen. Run again. Were they right?

7. **Now ask them to explain it back.** Pick a random line. "What does this line do?" If they can explain → propose the *I Know What Code Does* badge.

## TODO discipline

Always one TODO. Never more than ~10 lines for the first script. The kid's brain bandwidth is limited; you're not building production software.

## When to award *I Know What Code Does*

Conditions:
- Claude wrote the script; the kid directed what it should do.
- The kid filled in the TODO and made at least one additional change on their own.
- They can explain what at least 3 lines of the script do, in their own words.

If yes: write to `quests/completed.md`, update `me.json.concept_badges` with the badge ID `code-execution`, timestamp, and the path to the script file as evidence.

## Sycophancy check

If they run the script and immediately say "cool what's next" — pause. Pick a random line. "Quick — what does this line do?" If they can't, that's the work. Stay here.

## Common pitfalls

- `python` vs `python3` — try both. If neither works, parent-flag (Python install).
- File saved with `.txt` extension by mistake — check.
- Indentation errors — explain that Python cares about whitespace.
- Kid wants to add a feature immediately — fine, but make them predict first what'll change. Run before believing.

## What this teaches

**That code is editable.** That you can read it, predict what it'll do, change one piece, and the rest still works. That understanding ≠ typing. The kid leaves with the confidence that they can work with code that someone else (or some AI) wrote — which is what 90% of programming actually is.
