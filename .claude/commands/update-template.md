---
description: Pull the latest scaffolding (skills, concepts, safety, tinker, meta docs) from the kids-ai-starter template. Safe — does not touch your CLAUDE.md, your me.md / me.json, your current quest, or anything you built.
---

The kid (or their parent) is asking to pull updates from the source template repo.

**Source template:** `https://github.com/cfrerebeau/kids-ai-starter.git`

Walk them through this calmly, plain English. Run the commands yourself with the Bash tool. Tell them what each step did, one line.

## Steps

### 1. Refuse if working tree is dirty

Run `git status --short`. If anything is uncommitted or unstaged → tell them: "You have unsaved changes — commit them first, then run `/update-template` again." Stop here.

### 2. Add upstream remote if missing

Run `git remote get-url upstream` (it errors if missing — that's OK).
If missing, run: `git remote add upstream https://github.com/cfrerebeau/kids-ai-starter.git`.

### 3. Fetch

Run: `git fetch upstream`.

### 4. Summarize what's different

Run:
```
git diff --stat HEAD upstream/main -- .claude/ concepts/ safety/ tinker/ quests/README.md SETUP.md PARENTS.md README.md START_HERE.md LICENSE .vscode/settings.json
```

If the output is empty → tell the kid "Everything's up to date." Stop here.

Otherwise, summarize what changed in 3-5 plain-English bullets. Examples: *"New file in concepts/"*, *"safety/README.md updated"*, *"4 lines changed across the entrepreneur-coach skill."*

### 5. Mention CLAUDE.md separately (if changed)

Run:
```
git diff --stat HEAD upstream/main -- CLAUDE.md
```

If non-empty, tell the kid: *"CLAUDE.md also changed in the template — but that file is yours to customize, so I won't touch it. If you want to see what's different and merge by hand, run `git diff HEAD upstream/main -- CLAUDE.md`."*

### 6. Confirm

Ask: *"Want me to pull the scaffolding changes in? Your CLAUDE.md, profile, current quest, and project files won't be touched."*

If no → stop. If yes → continue.

### 7. Pull and commit

```
git checkout upstream/main -- .claude/ concepts/ safety/ tinker/ quests/README.md SETUP.md PARENTS.md README.md START_HERE.md LICENSE .vscode/settings.json
git add -A
git commit -m "Pull latest scaffolding from template"
```

### 8. Tell the kid what they got

One or two sentences. Don't read every file. Example: *"Pulled in the new entrepreneur-coach prompt tweaks and a new tinker example. Done."*

## Notes for you (Claude)

- Restraint applies: ask before the destructive checkout (Step 6).
- Do NOT update CLAUDE.md automatically. Ever.
- Do NOT update `quests/current.md` or `quests/completed.md` — those are the kid's live state. (They're already excluded from the checkout list above, but don't add them by mistake.)
- `me.md` and `me.json` are gitignored and won't be touched regardless.
- If a checkout fails because a file was deleted in the kid's repo, just continue — `git checkout upstream/main -- <path>` will restore it.
- If structural changes have happened (renamed/deleted files in the template), this command may leave orphan files. Tell the kid: *"There may be some old files from before the rename — your coach can clean those up if anything looks off."* Don't auto-delete.
