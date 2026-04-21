# Discovery Protocol

A modular interview procedure for eliciting and structuring company identity definitions. This is a **skill** — a framework-agnostic procedure that any agent or LLM can execute by reading this file. No Crafty-specific context required to run it.

---

## Protocol Rules

1. **One module at a time.** Complete and confirm each module before moving to the next.
2. **Draft-first rhythm.** Ask 1-2 seed questions, listen, synthesize, ask one targeted follow-up if a key area is still unclear — then draft. Do not exhaust the question bank before drafting.
3. **Vague answers are valid.** If the author is uncertain, help them think out loud. Do not demand precision before producing a draft.
4. **Confirm before writing.** Always show the draft of the identity section and get explicit confirmation before writing to a file.
5. **Challenge gently.** If a new answer contradicts an earlier one, surface it: "Earlier you said X — does that still hold, or should we update it?"
6. **Resumable.** On startup, check existing content. Do not re-interview sections that are already complete.

---

## Conversation Rhythm (applies to every module)

```
1. Open with 1-2 seed questions from the module's question bank
2. Author responds — vague or detailed, both are valid
3. Reflect back: "So what I'm hearing is [synthesis of their answer]..."
4. Ask one follow-up if a key area is still unclear
5. Draft the identity file section(s) for this module
6. Show draft: "Here's what I'd write — does this capture it?"
7. Author confirms or corrects
8. Write / update the file(s)
9. Announce the next module: "Next we'll cover [topic]. Ready to continue?"
```

---

## Module 1 — The Problem

**Goal:** Understand what is broken, for whom, and why this team is positioned to solve it.

**Seed questions (pick 1-2):**

- "What problem are you solving? Describe it as if I've never heard of your industry."
- "Who wakes up at night because of this problem? What does their day look like because it exists?"
- "Why hasn't this been solved already? What's the best existing option, and why does it fall short?"

**Follow-up probes:**

- "How long has this problem existed? What's changed recently that makes now the right moment?"
- "Why you / this team? What do you know or have access to that others don't?"

**Draft target:** `problem.md`

Sections to fill: Problem Statement, Who Experiences It, Current Alternatives, Why Now, Why Us.

---

## Module 2 — Vision & Positioning

**Goal:** Establish long-term direction and where the company sits relative to alternatives.

**Seed questions (pick 1-2):**

- "If this works perfectly in 7 years, what does the world look like? What's different because you existed?"
- "How would you describe what you do in one sentence to a stranger at a dinner party?"

**Follow-up probes:**

- "What category does this live in — how would a customer search for you?"
- "Who are you most different from? What's the one thing you do that they don't or can't?"
- "What's your unfair advantage — the thing that's hardest for someone else to replicate?"

**Draft targets:** `vision.md` + `positioning.md`

---

## Module 3 — The Customer

**Goal:** Define the ideal customer with enough specificity to disqualify bad fits.

**Seed questions (pick 1-2):**

- "Picture your single best possible customer. What kind of company or person are they? What's their role?"
- "What just happened in their life or business that made them start actively looking for a solution?"

**Follow-up probes:**

- "Who inside the organization feels the pain most? Who signs the check? Are they the same person?"
- "Who looks like a good customer but turns out not to be? What disqualifies them?"
- "What does this person believe that a skeptic in the same role wouldn't?"

**Draft target:** `icp.md`

Sections to fill: Demographics/Firmographics, Role/Buyer, Psychographics, Key Pains, Buying Triggers, Disqualifiers.

---

## Module 4 — The Business

**Goal:** Understand how value is delivered and how money flows.

**Seed questions (pick 1-2):**

- "Walk me through a transaction — from the moment a customer first hears about you to the moment money changes hands."
- "What do you have to be genuinely excellent at to keep the promise you're making? What's the hard operational part?"

**Follow-up probes:**

- "Is this one-time revenue or recurring? What determines the price?"
- "How do customers find you today, or how do you expect them to? If you could only bet on one channel, which one?"
- "What's the biggest cost you have to carry to serve a customer?"

**Draft targets:** `business_model.md` + `gtm.md`

---

## Module 5 — Culture

**Goal:** Capture how the team operates and what it stands for internally.

**Seed questions (pick 1-2):**

- "How do you want people on this team to make decisions when you're not in the room?"
- "What are you not willing to compromise on — even if it costs you a deal or slows you down?"

**Follow-up probes:**

- "What would a new hire notice in the first week about how things actually work here?"
- "What's a trade-off you'll consistently make — speed vs. quality, autonomy vs. alignment? What's your default?"
- "What behavior would make you fire someone immediately, even if their work was excellent?"

**Draft targets:** `principles.md` + `culture.md`

---

## Resumption Logic

On startup, inspect each identity file:

| State | Action |
| --- | --- |
| No `<fill>` remaining | Summarize content back: "Here's what's defined for [section]..." and ask "Does this still reflect your thinking?" |
| Some `<fill>` remaining | Treat filled parts as confirmed context. Resume from the first `<fill>` using targeted follow-up questions only. |
| All `<fill>` (empty) | Run the full module from the seed questions. |

If `company/identity/discovery-draft.md` exists, read it first — it records which modules were completed in a prior session.
