# Parents — Read This First

This is a starter kit that helps your kid (~12–16) build a real, publicly-shipped AI app, with Claude Code as the day-to-day coach. You are the sponsor, the weekly reviewer, and the safety layer.

Aim to spend ~30 minutes upfront (one-time setup, Section 0) and ~30 minutes/week after that.

---

## 0. One-time setup (do this before the kid touches anything)

This is the only heavy lift. After this, everything is in-flow.

### a. Create the kid's repo from this template

1. Go to https://github.com/cfrerebeau/kids-ai-starter (the source repo).
2. Click **"Use this template"** → **"Create a new repository"**.
3. Pick an owner: yourself, or the kid's GitHub account (if they have one — needs to be 13+; under 18 needs parental consent per GitHub ToS).
4. Name it whatever the kid wants. `my-first-app`, `bird-thing`, doesn't matter.
5. **Set visibility to Private.** This is important — the kid will commit progress here, and private keeps WIP off the public internet.
6. Click Create.

If the source repo doesn't have "Use this template" available, fork it instead, then go to Settings → Change visibility → Private.

### b. Install VS Code on the kid's machine

- Download from https://code.visualstudio.com/ (free, official).
- Install with default settings.

### c. Install Node.js (needed for Claude Code)

- Download the **LTS** version from https://nodejs.org/.
- Install with default settings.
- Verify: open a terminal and type `node --version` — you should see a version number.

### d. Install Claude Code

In a terminal:

```
npm install -g @anthropic-ai/claude-code
```

Verify with:

```
claude --version
```

(Alternative: official installer at https://claude.com/download — handles npm and PATH setup for you.)

### e. Sign Claude Code in

Run `claude` once yourself. It will prompt you to sign in. Two options:

- **Claude Pro or Max subscription** (recommended for daily kid usage — flat monthly fee, no token metering anxiety).
- **API key** from https://console.anthropic.com — pay per token. If you go this route, set a monthly budget alert (Section 3).

Sign in with whichever you choose. Then exit (`Ctrl+C` or type `exit`).

### f. Clone the kid's new repo and open in VS Code

1. On GitHub, on the kid's new repo, click the green **Code** button → copy the HTTPS URL.
2. In a terminal:
   ```
   git clone <the-url>
   cd <repo-name>
   code .
   ```
   `code .` opens the folder in VS Code.

### g. Hand it over

The kid opens VS Code (if not already), opens a terminal inside it (`View → Terminal` or `` Ctrl+` ``), and types `claude`. They take it from here — `START_HERE.md` tells them what to do.

---

## 1. What your kid will do

- Run a working example in minute 3 (no setup before).
- Pick a real problem they care about.
- Talk to real users about it — eventually including strangers, with your approval.
- Learn Python, the web, and databases by building.
- Learn to verify what AI tells them, and to push back when they think Claude is wrong.

## 2. What you're being asked to do (checklist)

- [ ] Read this file in full before the kid starts.
- [ ] Complete Section 0 (one-time setup: template repo, VS Code, Node, Claude Code).
- [ ] Install Python 3 on their machine if not installed (`python3 --version` to check).
- [ ] Set a monthly budget alert on the Anthropic console (suggested: $30/mo to start).
- [ ] Be available to install Streamlit when they get there (one terminal command, ~30s).
- [ ] Create a Supabase free-tier account with them when they reach that quest (week 3–5).
- [ ] **Approve the first time** they share their app to anyone outside the family.
- [ ] 30-min Sunday review of `quests/completed.md`.
- [ ] **Cosign** behavior badges marked `(parent-cosigned)` — uncheck if you disagree with Claude's assessment.
- [ ] Watch for stalled-kid signs (Section 7). Intervene if 2+ weeks of no movement.

## 3. Budget and cost control

- **Claude API credits**: realistic spend for an active kid is $10–40/month. Set a hard alert.
- **Other paid services** the kid may want once excited: domain (~$12/year), email sender, image/voice APIs, hosting upgrades.
- **Rule**: the kid cannot add a paid service without your signoff. CLAUDE.md enforces this (parent-flag).
- **Kill switch**: if spend spikes, go to console.anthropic.com → API Keys → revoke the key. Takes 30 seconds.

## 4. API keys and `.env` discipline

- The kid will need an API key eventually. It goes in a file called `.env`. Never in source code, never pasted into a chat.
- `.gitignore` excludes `.env` by default. Verify before any push to a public repo.
- If your kid pastes a real API key anywhere visible, **rotate it immediately** (console → revoke → create new).

## 5. Privacy

- `me.md` (the kid's profile) and `me.json` (their state) are **gitignored by default**. They contain name, age, interests, and progress — not safe for a public repo.
- If you decide to track them (e.g. for transparency with the kid), edit `.gitignore` and accept the risk. Recommendation: leave them gitignored.
- The kid's app itself should NOT include their full name, school, location, or age. CLAUDE.md enforces this, but verify before launch.

## 6. Strangers + safety

Goal #3 of the program is "a stranger uses it." This is the hard goal — and the riskiest.

- **Approved channels**: a Discord you trust, a subreddit you've checked, an extended-family group, a teacher's network, a parent-network. **Not** random TikTok/X posts.
- **No DMs with users.** Feedback goes through a form (a Google form, a Tally form, etc.). CLAUDE.md enforces this.
- **If a user asks to meet, message privately, or pressures the kid** — the kid is told to show you immediately.
- **First stranger launch requires your signoff.** Claude will raise a parent-flag.

## 7. The stalled-kid playbook

Signs your kid is stuck: 2 weeks with no quest movement; only chatting with Claude, not building; abandoned project file.

What to do, in order:
1. Ask: "What was the last thing that felt good?" Work backward to find where the energy died.
2. Lower the bar: ship anything, even a typo fix to the live app. Re-establish forward motion.
3. Offer a break: 2 weeks off is fine. Don't make this a chore.
4. Switch projects: explicitly OK. There's a *Restarter* badge for abandoning a bad idea deliberately.
5. Stop: also OK. They learned what they learned. The point was the learning, not the artifact.

## 8. If you have more than one kid

- Give each their own clone of the repo with their own `me.md` and `me.json`. **Do not share** — XP comparison breeds resentment.
- If one kid helps the other: the helper gets the satisfaction of teaching, but does NOT earn the other's badges. Teaching is its own win — name it out loud.

## 9. What NOT to do

- Don't write code for them.
- Don't answer Claude's questions for them.
- Don't suggest features. Claude does that (carefully); you don't need to.
- Don't intervene unless they ask, or you see a safety/stalled signal.

## 10. Emotional safety

This is a coach, not a therapist. If your kid expresses distress (frustration is fine; distress is different), step in. CLAUDE.md raises a parent-flag on certain phrases, but you are the actual layer.

## 11. Known limitations (be honest with yourself)

- Claude's "coach not autocomplete" rules are prompt-level. They will drift. The kid has off-switches ("just build it", "shut up mode") to take agency when the rules misfire. Trust those.
- Concept badges require an artifact in the kid's project — but a kid can copy-paste. Your Sunday review is the real verification layer.
- The "stranger uses it" badge may stay unclaimed for some kids. That's OK. The goal is the *attempt*, not always the outcome.

## 12. Sunday review (30 min)

Open `quests/completed.md`. You'll see:
- Quests completed since last review, with evidence.
- `[ ] PROPOSED:` entries for parent-cosign badges. Read what the kid did. Check the box if you agree.
- Any safety flags Claude raised that week.

Ask your kid one question: "What surprised you this week?" The answer is the real progress report.

---

That's it. Go tell your kid to open `START_HERE.md`.
