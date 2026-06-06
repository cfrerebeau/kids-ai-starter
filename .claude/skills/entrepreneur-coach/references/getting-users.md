# getting-users

**Goal**: a real stranger uses the kid's app. **Requires parent approval for the launch channel.**

## When this fires

The kid has:
- A working app (small-app at minimum, ideally with one real API connected).
- At least one friend/family user who's used it and given feedback.
- The kid wants more users — strangers, real distribution.

## The first move — get coach approval

🛑 **Parent-flag.** Tell the kid:

> "Before we share this anywhere outside family, show this to your coach. They have to approve where you share it. This is the safety part."

The kid shows `safety/README.md` and `safety/stranger-contact.md` to their coach. Coach approves a channel.

**Approved channels look like:**
- A specific Discord server the coach already knows.
- A subreddit the coach has read and is OK with.
- An extended-family group chat.
- A teacher's network or school newsletter.
- A parent's professional network (if relevant).

**Not approved by default:**
- Public TikTok / X / Instagram / Snapchat posts.
- Public Discord servers the coach hasn't checked.
- Random forums.
- Hacker News, Product Hunt (these are adult business platforms — fine in some cases, but coach decides).

## Step 1 — Set up a feedback form

Before any stranger uses the app, the kid creates a 3-question form (Google Forms, Tally, anything free):

1. Did this work for you? (Yes / No / Sort of)
2. What's the one thing you'd change?
3. Anything else? (optional)

Put the form link inside the app. This is how strangers give feedback. **No DMs. No direct messages. Always the form.**

## Step 2 — Make the app shareable

The app needs to be deployable. For Streamlit:

- **Streamlit Community Cloud** (free, easy): connect a GitHub repo, deploy. Public URL.
- 🛑 **Parent-flag**: GitHub account, Streamlit Cloud account.

Verify before sharing:
- The deployed URL works.
- The kid's full name, school, age, location are NOT in the app.
- No API keys are exposed in the code (use `.env` and Streamlit secrets).
- The feedback form link works.

## Step 3 — Write the post / share message

Have the kid write 2–4 sentences. NOT a pitch. A simple invitation.

Format:

> "I built a small thing that helps [persona-like person] do [opportunity]. It's rough but real. If you'd try it and tell me what you think, link's here: [URL]. Feedback form is in the app."

That's it. No emojis. No "🚀 launch 🎉". Quiet and real.

## Step 4 — Share. Then wait.

The coach posts (if the kid isn't on the platform) or supervises the kid posting. Then the kid waits.

This is the hard part — the waiting. Most stranger launches get zero users. Some get one. A few get many. Set expectations:

> "Most things people make get ignored. That's normal. One person is a win."

## Step 5 — Handle whatever comes

- **No one responds (most common)**: that's data. Was the channel wrong? Was the description unclear? Did the link work? Route back to `evolve-or-stick.md`.
- **One stranger replies via form**: read it together. Whatever they said, take it seriously. Award *Shipper* badge. Their feedback is the most valuable thing the kid will get in the whole program.
- **Someone messages the kid directly (DM)**: do NOT engage. The kid responds: "Hey thanks — please drop feedback here: [form link]." If they keep pushing → parent-flag.
- **Someone is mean**: screenshot it for the coach. Delete the message. Move on.
- **Someone wants to pay / promote / "collaborate"**: parent-flag, immediately.

## When to award XP and badges

- 100 XP for "Small app shipped to a stranger" — when one stranger has used it (verified via feedback form submission OR app analytics showing a non-known user).
- 150 XP for "3+ strangers actively using it" — three distinct strangers, evidence in completed.md.
- *Shipper* badge with the first stranger.

## What this teaches

Distribution is part of building. An app no one knows about is half-built. Learning to ship — quietly, with safety, with low expectations — is the skill most adults are still working on.

## Sycophancy check

If the kid says "great let's launch on TikTok" — pause. "TikTok is not approved. Your coach approves the channel. Let's talk to them first." Hold the line on this, no exceptions.
