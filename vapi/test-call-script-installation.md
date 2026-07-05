# Test Call Script — Installation Branch (Apex HVAC / Elliot)

Tests the `[New Installation]` path of the system prompt (v2), which is different from
the Repair/Maintenance path we already validated. Goal: confirm Elliot asks about scope
and system type, and offers an in-person estimate with a Comfort Advisor — instead of
booking a repair technician window.

## Variables to set before starting

| Variable | Value |
|---|---|
| `customer_name` | `Sam Whitfield` |
| `service_type` | `Installation` |
| `request_details` | `Looking to replace our old central AC system, it's original to the house and struggling` |
| `service_location` | `312 Birchwood Court, Austin, TX 78745` |

## Conversation script

**1. Opening — confirm who you are**
> "Yeah, this is Sam."

**2. Describe what you're looking for (scope)**
> "So our AC is original to the house, it's like twenty years old at this point, and it's
> just not keeping up anymore. We want to replace the whole system."

**3. System type / preference (if asked)**
> "I think we'd want to stick with central AC, but honestly I'm open to hearing what you
> recommend."

**4. Scope — how many systems/units**
> "It's just the one system for the house."

**5. Confirm service location (if asked)**
> "Yep, that's 312 Birchwood Court, Austin."

**6. Let Elliot offer the in-person estimate — accept a time**
> "Sure, sometime next week works. Mornings are usually better for me."

**7. Preferred time**
> "How about Tuesday morning?"

**8. Let Elliot wrap up naturally**
> Confirm any details it asks for, then let the assistant end the call rather than
> hanging up — so `endedReason` reads as a clean completion.

## What to listen for (this is the point of the test)

- Does Elliot correctly route to the **installation** flow instead of asking
  repair-style questions (symptoms, "is it completely down," dispatch fee)?
- Does it mention scheduling an **in-person estimate with a Comfort Advisor** —
  not a repair technician window?
- Does it **not** mention the $89 diagnostic fee (that's repair/maintenance-specific)?
- Does the natural-tone rewrite hold up — contractions, no address recited digit-by-digit,
  brief acknowledgments before next question?

## After the call

Tell Claude it's done — pull the call from Vapi's logs (or check the Structured Outputs
panel directly in the dashboard) to see how `scope_of_call` and `system_type` got
captured for an installation request, and confirm `call_status` still resolves correctly
now that `[Call Outcomes]` was removed from the spoken prompt.
