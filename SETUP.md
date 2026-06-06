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

## Step 7 — Clone the kid's new repo

1. On GitHub, on the kid's new repo, click the green **Code** button → copy the HTTPS URL.
2. In a terminal:
   ```
   git clone <the-url>
   cd <repo-name>
   code .
   ```
   `code .` opens the folder in VS Code.

   *On Mac, if `code .` says "command not found"*: open VS Code → Command Palette (`Cmd+Shift+P`) → type "Shell Command: Install 'code' command in PATH" → run it. Then retry.

## Step 8 — Hand off

The kid:
1. Opens VS Code (if not already).
2. **If you installed the extension (Path A)**: clicks the Claude icon in the sidebar to open the Claude panel. Says hi.
3. **If you installed the CLI (Path B)**: opens a terminal inside VS Code (`View → Terminal` or `` Ctrl+` `` / `` Cmd+` ``). Types `claude`.

After that they're off. `START_HERE.md` walks them through it.

---

## Done. Now read PARENTS.md.

`PARENTS.md` is the ongoing role: budget, safety, Sunday reviews, stalled-kid playbook. Setup is done — that's the rest.
