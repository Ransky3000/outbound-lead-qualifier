# Test Call Script — Routine Maintenance, Low Urgency, International Address (Apex HVAC / Elliot)

Real live test (Call Lead is enabled) — this will place an actual call and incur cost.
Tests two things we haven't tried yet: the **Maintenance/Tune-up** framing (should feel
different from a repair call), and a **low-urgency tone** (should NOT come out sounding
urgent in the Urgency field afterward). Also uses an international (PH) address to check
how Elliot handles a non-US address naturally.

## Form data

| Field | Value |
|---|---|
| **Full Name** | Ranian |
| **Phone Number** | `+639473702512` (your real number, so you can answer) |
| **Email Address** | your real email |
| **Request Type** | Routine Maintenance / Tune-up |
| **Service Address** | `Blk 4 Lot 12, Villa Grande Subdivision, Cebu City, Philippines 6000` (swap for whatever address you actually want to test) |
| **How can we help you?** | `Want to get the aircon serviced/cleaned before it gets used heavily, no issues right now, just preventive maintenance` |

## Conversation script

**1. Confirm it's you**
> "Yeah, this is Ranian."

**2. Frame it as maintenance, not a problem**
> "Yeah so everything's actually working fine right now — I just want to get it cleaned
> and serviced before it gets heavy use, kind of a checkup."

**3. System type**
> "It's a split type unit."

**4. Unit quantity**
> "Just the one unit."

**5. Urgency — deliberately keep this low-key, this is the point of the test**
> "No rush at all, honestly. Whenever's convenient works, there's no problem right now,
> I just don't want to wait until something breaks."

**6. Confirm the address naturally**
> "Yep, that's the address — Villa Grande Subdivision in Cebu."

**7. Preferred time — keep it relaxed too**
> "Sometime next week is fine, I'm pretty flexible. Maybe afternoon if that's easier."

**8. Let Elliot end the call naturally**

## What to check afterward

- Does `scope_of_call` reflect a **maintenance/tune-up** job, not a repair?
- Does `urgency` come back genuinely low-key (e.g. "no immediate urgency, routine
  service requested") rather than defaulting to urgent language?
- Does Elliot handle the PH address naturally, without garbling it?
- Does the $89 fee framing still make sense for a maintenance visit, or did Elliot
  awkwardly force in repair-specific language?
