# creating-context

**Goal**: the kid realizes they can build their own CLAUDE.md, their own skills, and their own memory — that Claude's behavior is configurable by them, not fixed.

## When this fires

- Kid asks "can I make my own skill" or "can Claude remember X about my project".
- Kid is doing the same thing repeatedly and could automate it.
- Kid is annoyed that Claude keeps forgetting something specific to their project.
- Kid is ready for the "wait, I can SHAPE this?" realization.

## What "context" means here

When Claude responds, it's not pulling from a fixed brain. It's reading:
- The current conversation.
- Files Claude is asked to read.
- Files automatically loaded (CLAUDE.md, skill SKILL.md files).
- Memory (if configured).

**You can write any of these.** That's the unlock.

## The three places the kid can shape Claude's behavior

### 1. CLAUDE.md (project-level)

This file is in the repo root and loaded every session. It tells Claude:
- Who's using this (you can add your name, your style).
- Project-specific rules ("In this project, never use frameworks; always vanilla Python.")
- Coding conventions.

The kid can edit this. Encourage them to. After they've worked in the repo for a while, ask: "what's a thing Claude keeps doing that's not right for your project? Let's add a rule to CLAUDE.md."

Walk them through editing it. Show them the change takes effect next session.

### 2. Skills (`.claude/skills/`)

A skill is a reusable instruction set Claude loads when triggered. The skills in this repo (onboarding, builder-coach, etc.) were written by the program designer. The kid can write their own.

**When does a kid want their own skill?**
- When they have a workflow they do repeatedly. Example: "every time I add a feature, I want Claude to first ask me who the user is."
- When they want their project to have its own coach. Example: "I'm building a bird app — I want a `bird-helper` skill that knows about my data sources."

Walk them through creating one:

```
.claude/skills/<their-skill-name>/SKILL.md
```

Format: YAML frontmatter with `name` and `description` (the description is what triggers it). Then markdown body describing what to do.

After they make their first skill: celebrate. Award progress toward "Context Crafter" (could be tracked as a behavior badge — coach decides if it's substantial enough to cosign).

### 3. Memory (file-based, optional)

Memory is a directory Claude can read/write to remember things across sessions. In this repo, `me.md` and `me.json` serve as memory. Anywhere else, the kid can create their own memory directory and tell Claude to use it.

## The lesson

The kid's mental model shifts from:

> "Claude is fixed. I work around its limits."

To:

> "Claude is shaped by what I give it. If I want different behavior, I can write that."

This is one of the highest-leverage AI fluency skills there is. Most adults never learn it.

## The exercise — first time

If the kid expresses frustration like "ugh Claude keeps doing X" or "I wish Claude knew about Y" — that's the moment:

> "OK — that's exactly the kind of thing you can fix yourself. Want to add a line to CLAUDE.md so Claude does Y from now on?"

Walk them through. The change persists.

## What this teaches

Two things, both fundamental:

1. **AI is not a closed product. It's an interface to a language model, configured by context.** The kid who learns to shape that context goes faster than the kid who just talks to the default.
2. **Tools are programmable.** This is a general lesson — most things in computers can be shaped if you know they can. The kid leaves with this disposition.
