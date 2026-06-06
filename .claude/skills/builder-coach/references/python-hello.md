# python-hello

**Goal**: the kid writes a Python file *from scratch* (empty file, not a template) that runs. Earns *I Know What Code Does*.

## Sequence

1. Ask what they want their script to do. Anything. "Print my name 5 times." "Tell me a joke." "Add two numbers." Resist suggesting — let them pick something dumb if they want.
2. Have them create the file themselves: `touch my_first.py` or just create it in their editor. **You don't create it.**
3. Have them type the first line. Wait. Ask "ready for the next?"
4. After 3–5 lines, have them save and run it: `python my_first.py`.
5. They report back what happened.
6. If it broke: read the error together. Ask "what does that line literally say?" Then walk through.
7. If it worked: name what just happened in one sentence (e.g. "the computer just executed 4 instructions in order — that's code execution"). Link `concepts/code-execution.md`. Offer the badge.

## TODO discipline

If they ask you to write the file for them, leave a TODO so they have to type at least one line themselves before it runs. Example:

```python
# A simple script.

# TODO(you): change this to your name
name = ""

print("Hi,", name)
```

## When to award *I Know What Code Does*

Conditions:
- The kid wrote the file from an empty file (not by editing `tinker/hello.py`).
- They wrote every line themselves (you may have answered "how do I print" type questions, but the typing was theirs).
- It ran. Output appeared.

If yes: write to `quests/completed.md` and update `me.json.concept_badges` with the badge ID `code-execution`, the timestamp, and the path to their file as evidence.

## Sycophancy check

If they say "ok cool what's next" after running their script — pause. "Look at the output. Read it out loud. Does it match what you thought would happen?" Make them slow down once.

## Common pitfalls

- `python` vs `python3` — try both. If neither works, parent-flag (Python install).
- File saved with `.txt` extension by mistake — check.
- Indentation errors — explain that Python cares about whitespace.
