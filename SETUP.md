# Setup — One Time, by the Parent

This is the only heavy part. After this, the kid runs the show.

**Plan ~1 hour the first time, mostly waiting for installs.** On Mac, the Xcode Command Line Tools download alone can take 10–30 minutes depending on network. Start it first, do other steps while it runs.

---

## Step 1 — Create the kid's repo from this template

1. Go to https://github.com/cfrerebeau/kids-ai-starter (the source repo).
2. Click **"Use this template"** → **"Create a new repository"**.
   - If you don't see that button, click **Fork** instead, then later: Settings → Change visibility → **Private**.
3. Pick an owner: yourself, or the kid's GitHub account (13+ per GitHub ToS; under 18 needs parental consent in many places).
4. Name it whatever the kid wants. `my-first-app`, `bird-thing`, anything.
5. **Set visibility to Private.** The kid will commit progress here — private keeps WIP off the public internet.
6. Click Create.

## Step 2 — Install Git (kick this off first if on Mac)

### Mac

In a terminal:

```
xcode-select --install
```

A dialog pops up. Click Install. **This can take 10–30+ minutes.** Move on to other steps while it runs.

Alternative if you have Homebrew: `brew install git`.

Verify (after it finishes):
```
git --version
```

### Windows

Download from https://git-scm.com/download/win. Install with default settings.

### Linux

Usually pre-installed. If not:
```
sudo apt install git
```

## Step 3 — Install VS Code

- Download from https://code.visualstudio.com/ (free, official).
- Install with default settings.
- On Mac, while installing: drag VS Code from Downloads into Applications.

## Step 4 — Install Claude Code

**Pick one of two paths:**

### Path A — VS Code extension (recommended for kids)

Easier UX. The kid sees a Claude panel inside VS Code instead of typing in a terminal.

1. Open VS Code.
2. Click the Extensions icon in the left sidebar (or `Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Search **"Claude Code"** by Anthropic. Install it.
4. Follow the extension's sign-in prompt (next step).

### Path B — Command-line interface (CLI)

If you'd rather have the kid use the terminal:

1. Install Node.js LTS from https://nodejs.org/.
2. In a terminal:
   ```
   npm install -g @anthropic-ai/claude-code
   ```
3. Verify:
   ```
   claude --version
   ```

## Step 5 — Sign Claude Code in

Whichever path you picked, Claude Code needs to authenticate. Two options:

- **Claude Pro or Max subscription** — recommended for daily kid usage. Flat monthly fee, no token-by-token spend anxiety. Sign in with your Anthropic account.
- **API key** from https://console.anthropic.com — pay per token. If you go this route, **set a monthly budget alert** before handing off (suggested: $30/mo cap). The kill-switch is the same console: revoke the key.

Follow the prompts in the extension or CLI to sign in.

## Step 6 — Install Python 3

The kid will need it. Most Macs and Linux machines have it pre-installed.

Check:
```
python3 --version
```

If missing:
- Mac: it should appear after Xcode CLT installs. If not: https://www.python.org/downloads/.
- Windows: https://www.python.org/downloads/ — **check "Add Python to PATH"** during install.
- Linux: `sudo apt install python3 python3-pip`.

## Step 7 — Sign into GitHub and clone the kid's repo

The kid's repo is private. Git needs to know who's allowed in. The easy path is letting VS Code handle the auth (it stores credentials in the system keychain and reuses them for every git operation).

### 7a. Sign into GitHub from VS Code

1. Open VS Code.
2. Click the **Accounts** icon — the little silhouette at the bottom-left of the VS Code window.
3. Click **Sign in with GitHub to use GitHub features**.
4. A browser opens. Sign into the GitHub account that has access to the kid's new repo.
5. Authorize VS Code. The browser redirects back. Done — VS Code is signed in.

**Which GitHub account to use?** Any of these is fine; pick what fits your situation:

- **Kid's own account** (cleanest): the kid has their own GitHub account (13+ per ToS, parental consent under 18 in many places), the repo is on their account, and they sign in as themselves.
- **Kid's account, parent owns the repo**: repo on your account, kid added as a collaborator → kid signs in as themselves. Their access is scoped to that repo only.
- **Parent signs in on the kid's machine**: simplest if the kid isn't ready for their own account. Just be aware they'll see your other private repos in VS Code's source-control UI. Fine for a shared family machine; less fine if you have sensitive work repos in there.

You can also switch later — sign out of VS Code, sign back in as a different account when the kid gets their own.

### 7b. Set the kid's git identity (for commits)

So commits show up as the kid, not as "unknown." Open a terminal:

```
git config --global user.name "Kid's Name"
git config --global user.email "kid-email@example.com"
```

Use the same email that's on their GitHub account if they have one (otherwise commits won't be linked to their profile).

### 7c. Clone the repo

Two ways. Pick whichever you prefer — both use the VS Code sign-in.

**Way A — from VS Code (no terminal):**

1. `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) → type **"Git: Clone"** → Enter.
2. Paste the HTTPS URL of the kid's repo (green **Code** button on the repo page → copy HTTPS).
3. Pick a folder on disk to clone into.
4. When VS Code asks, click **"Open"**.

**Way B — from the terminal:**

```
git clone <the-https-url>
cd <repo-name>
code .
```

If git prompts for credentials and your VS Code sign-in doesn't auto-fill, Git Credential Manager pops a browser window — sign in there.

*On Mac, if `code .` says "command not found"*: open VS Code → Command Palette (`Cmd+Shift+P`) → type **"Shell Command: Install 'code' command in PATH"** → run it. Then retry.

### Verify auth works

In the cloned folder, run:

```
git pull
```

If it succeeds without asking for a password, auth is set up. If it asks every time, the credential helper didn't take — see "Troubleshooting auth" below.

### Troubleshooting auth

- **Repeatedly asked for password**: git isn't finding the saved credentials. On Mac, run `git config --global credential.helper osxkeychain`. On Windows, the Git for Windows installer sets up Credential Manager automatically. On Linux, `git config --global credential.helper "cache --timeout=86400"` will cache for 24h.
- **"Permission denied" / "Repository not found"**: the signed-in account doesn't have access. Check on GitHub that the kid (or whichever account) is a collaborator on the repo, or that they own it.
- **Two-factor authentication issues**: VS Code's GitHub sign-in handles 2FA automatically. If you're using `gh` CLI or PAT instead, you'll need a token instead of a password.

## Step 7.5 — If inline AI autocomplete still appears, disable it

The repo ships with `editor.inlineSuggest.enabled: false` in `.vscode/settings.json`. That covers most cases — no gray "ghost text" suggesting code as the kid types.

**If you still see autocomplete suggestions appearing** (some Claude Code extension versions or other AI extensions override the workspace setting):

1. VS Code → **Settings** (`Cmd+,` / `Ctrl+,`).
2. Search for "inline suggest" and uncheck it at the **User** level (not just Workspace).
3. If the Claude Code extension has its own "Enable inline completions" toggle in its extension settings page, turn that off too.
4. Disable any other AI completion extension (Copilot, Tabnine, Codeium) — for a kid learning to type, watching gray ghost text appear is confusing and short-circuits learning.

The point: when the kid types, they should see *only what they typed*. Claude helps via the panel/terminal, not by predicting their next keystroke.

## Step 8 — Sit with the kid for session 1

**Plan to be next to the kid for their first session (~15 minutes).** Not because they can't do it — because:

- Claude Code will likely show **permission prompts** the first time it tries to write files (it's asking "can I save your profile?"). The kid needs to click "Allow." Walk them through the first one.
- Anything weird in the install will surface here. Easier to fix together than via screenshot later.
- This is the moment that sets the relationship — they associate the program with you being interested, not with homework.

Then:
1. The kid opens VS Code (if not already).
2. **Path A (extension)**: they click the Claude icon in the sidebar to open the Claude panel. Say hi.
3. **Path B (CLI)**: they open a terminal inside VS Code (`View → Terminal` or `` Ctrl+` `` / `` Cmd+` ``). Type `claude`.

After session 1 they're off. `START_HERE.md` walks them through what to do once Claude says hi.

---

## Done. Now read PARENTS.md.

`PARENTS.md` is the ongoing role: budget, safety, Sunday reviews, stalled-kid playbook. Setup is done — that's the rest.
