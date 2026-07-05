# Test Call Script — Live Demo Recording (Apex HVAC / Elliot)

This is the actual call to use for the video's live-demo take (Section 1 of
`Demo recording plan/demo-narration-script.md`). Same real Contact (Ranian, matching
the existing Airtable record), but a new scenario: **Installation**, a **different
address**, and urgency deliberately played as "not urgent, but nice if soon" — soft
preference, not pressure.

⚠️ **This is a real submission** — if `Call Lead` is currently enabled in n8n, this will
place an actual call and write to Airtable for real. Confirm that's what you want before
submitting (recheck the node's enabled/disabled state if you're not sure).

## Form data

| Field | Value |
|---|---|
| **Full Name** | Ranian |
| **Phone Number** | `+639473702512` (your real number — same as the existing Contact) |
| **Email Address** | your real email (same as existing Contact, so it upserts cleanly) |
| **Request Type** | New System Installation Quote |
| **Service Address** | `4/22 Penkivil Street, Bondi NSW 2026, Australia` (new — different from the "Purok 5 Fatima" address already on file, since this is a different job. Real Bondi street, and `unit/street number` is genuinely how Australians write an apartment address, e.g. inner-Sydney suburbs like Bondi are dense with units) |
| **How can we help you?** | `Want to get an AC unit installed in a room that doesn't have one yet, no rush, just exploring options` |

## Conversation script

Cross-checked against the live system prompt (`prompts/system-prompt-v2.md`) — see the
⚠️ note before Step 6 for a real gap found in the prompt itself, not just this script.

**1. Answer whether now's a good time** (Elliot's opening asks this directly, e.g. "is
now an okay time to chat for a sec?" — not literally "is this you?")
> "Yeah, sure, go ahead."

**2. Frame it as a new installation, not a repair**
> "So actually there's one room in the house that doesn't have AC at all, and I want
> to get one put in."

**3. System type preference (if asked)**
> "I think a split system would work best for that room, but I'm open to what you
> guys recommend."

**4. Scope — how many units**
> "Just the one unit for that room."

**5. Confirm the address naturally**
> "Yep, that's Penkivil Street, unit 4."

**6. Urgency — the important part of this test, play it soft**
> "Honestly there's no rush on this, nothing's broken or anything. But if there's a
> slot available soon, that'd be nice, I'm just not in a hurry about it."

⚠️ **Possible curveball, be ready for it:** the system prompt's "Conversation Flow &
Required Topics" section lists the $89 dispatch fee as something Elliot mentions, and
that bullet isn't actually gated to Repair/Maintenance the way the "Core Goals" section
is — so Elliot might bring up the fee even though this is an Installation call, which
shouldn't have one. If that happens, don't break character trying to correct him — just
roll with it naturally:
> "Oh, okay, that's fine, good to know."

**7. Accept the in-person estimate / scheduling — pick one of the two windows Elliot
offers, don't stay vague**
> "Yeah, let's do the morning one." *(or whichever of the two slots he actually offers —
> the point is picking one, not leaving it open-ended)*

**8. Let Elliot wrap up, then close naturally**
> "Sounds good, thanks, bye."

**General note:** Elliot may ask a small clarifying follow-up that isn't listed above
(the prompt's error handling explicitly allows for this) — that's fine, just answer
naturally in character as Ranian rather than trying to force the conversation back onto
the script.

## What to check afterward

- Does `scope_of_call` read as an **installation** request, not a repair?
- Does `urgency` come back genuinely soft — something like "no immediate urgency, but
  would appreciate a slot soon if available" — rather than flattening to either extreme
  ("urgent" or "no urgency at all")?
- Does the new Service Request record show the **new address** (Penkivil Street, Bondi
  NSW), while the Contact record's address (whatever's currently on file) stays
  untouched — this is exactly the per-request Service Location behavior fixed earlier
  this session?
- Does Elliot correctly skip the $89 diagnostic fee line, since that's repair/maintenance
  specific, and instead offer the in-person Comfort Advisor estimate?
