# Upload Guide: putting Hearth & Hall into a Claude project

> Safe for you to read. Do this on a desktop computer; it's much easier than a phone. Plan on about 30–45 minutes the first time.
>
> **Honest warning up front:** a few things in here haven't been tested yet, because they can only be tested inside a real Claude project. They're marked **(untested)**. The session-one checklist at the bottom is how we find out.

---

## Part 1 · Get the files onto your computer

1. Go to your GitHub repository **hearth-and-hall** in a web browser.
2. Near the top left there's a button showing the branch name (it probably says **main**). Click it and pick **claude/dnd-campaign-builder-r0p0iz**.
3. Click the green **Code** button, then **Download ZIP**.
4. Find the ZIP in your Downloads folder and unzip it (on Windows: right-click → **Extract All**).
5. Open the unzipped folder, then the **dist** folder inside it. That's everything you need:
   - **project-files**: all the text files for the project.
   - **images**: player-safe pictures (portraits, maps, battle maps). Safe to look at.
   - **images-sealed**: DM-only pictures. **Don't open these.**
   - **MANIFEST.md**: a list of every file and what it's for.

**Spoiler rule:** any file whose name starts with **`sealed__`** is DM-only. You'll see the names; just don't open them. Same for anything in **images-sealed**.

---

## Part 2 · Make the Claude project

1. Go to **claude.ai** and click **Projects** in the left sidebar, then **Create project** (or **New project**). Name it **Hearth & Hall**.
2. **Paste the instructions.** In the unzipped folder, open `play-kit/project-instructions.md` (it's also in `dist/project-files/` as `play-kit__project-instructions.md`). Select all the text, copy it, and paste it into the project's **instructions** box (it may be labeled "Set project instructions" or "Custom instructions"). Save.
   - This text is safe for you to read. It has two parts: **Part A, the rules** for how the DM runs the game, and **Part B, the living state** (where you are, everyone's stats, gear, the Long Wall).
   - **(untested)** If the box says the text is too long, tell me in this build chat. The fix is to trim Part B's tables and move the detail into the Character Sheet doc.
3. **Upload the project files.** In the project, find **Project knowledge** (or **Files**) and click **Add** / **Upload**. Select **every file** in `dist/project-files/` and upload them.
   - You don't need to upload `play-kit__UPLOAD-GUIDE.md` (this file), but it doesn't hurt.
   - **(untested)** If the project says it's full, start over with just the **minimum set** listed in `dist/MANIFEST.md`. You'll swap the next act's chapters in when the story gets there.
   - When the files are big, a project may search its files instead of reading all of them at once. That's why the DM spine exists: it keeps the must-happen story beats in one short file the DM reads every session.
4. **Images: try a few first.** Upload just three from `dist/images/`: `player__maps__emberford-city.jpg`, `art__portraits__pc-01-ash.jpg` and `art__battlemaps__ch01-the-willow.jpg`. Don't upload the rest until the session-one test shows what works.
5. **Keep the images on your phone too.** Copy the `dist/images` folder to your phone (Google Drive, iCloud or a USB cable). If the DM can't show pictures, it will tell you which file to open instead, by name.

---

## Part 3 · Session one: the test checklist

Start a new chat **inside the project** and say: **"Start session one. Run the session-one tests first."** The DM should create your five living docs, then work through these with you before the story starts. Tick them off:

| # | Test | What "working" looks like | If it fails |
|---|---|---|---|
| 1 | **Five Claude Docs** get made: Campaign Bible, Character Sheet, Sealed GM Notes, Party Knowledge, Story Log | You see four docs you can open, and the DM says it made the sealed one (don't open it) | The DM keeps them as artifacts or files and says so |
| 2 | **Dice:** "Roll Dexterity (Stealth) for Ash" | The DM tells you the roll and modifier, then **stops and waits** for your number. NPC rolls show the code result | Remind it: "You roll everything but Ash's d20s, with code." |
| 3 | **Show an image** (untested) | The Emberford map appears in the chat | The DM names the file and you open it on your phone |
| 4 | **Token map** (untested) | The DM draws a grid and tokens on the Willow battle map with code and shows it | The DM tracks positions in text: `Ash J10 · brute L11` |
| 5 | **Voice mode** (untested) | Switch to voice, ask "show me the map." The DM should say "Map moment: pop out of voice mode to see the map, then come back" | Tell me what happened |
| 6 | **Wrap-up:** play a few minutes, then say **"log this session"** | The DM updates the docs, then gives you **one block** with the full updated instructions (Part A + Part B), then the next start line and a one-line recap | Note which step failed |

Tell me (in this build chat) what passed and what didn't. I'll adjust the instructions.

---

## Part 4 · The every-session loop

1. **Play.** Open a new chat inside the project. Say something like "Let's play. Pick up where we left off." The DM reads the instructions (including Part B, the living state), the docs and the files, then opens with the start line.
2. **End.** Say **"log this session."**
3. **Copy** the big instructions block the DM gives you (both parts).
4. **Paste** it into the project's instructions box, **replacing** the old text. Save.
5. **Next time,** start a new chat in the project. Everything carries over: the instructions hold the snapshot, and the docs hold the detail.

**Why paste every time?** The DM always reads the project instructions first, before any file. Keeping Part B current means every new chat starts knowing your goals, HP, gear, coin, what you used up, who you met and where the Long Wall stands.

**How the pieces fit:**

| Piece | Holds | Changes |
|---|---|---|
| Instructions, Part A | How the DM runs the game | Rarely |
| Instructions, Part B | The snapshot: goals, compact sheets for everyone, gear, changes this session, relationships, the Long Wall | Every session |
| Character Sheet doc | Full detail for Ash, Gideon, Zeke, Moss and Bart | Every session |
| Campaign Bible doc | The world as Ash has seen it | Every session |
| Party Knowledge doc | What Ash knows and who he trusts, and why | Every session |
| Story Log doc | The story, one tab per session | Every session |
| Sealed GM Notes doc | The DM's secrets. **Don't open.** | Every session |
| Project files | The campaign itself (static) | Only when new chapters or art get added |

---

## Part 5 · Later: new art

When the story reaches new places, ask in the build chat for the next batch of art (Act I has about 55 more images, roughly $3–4 in batch mode). Upload the new player-safe images the same way.
