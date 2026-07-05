# Test Call Script — Apex HVAC (Elliot)

Use this when running a manual "Talk" test in the Vapi dashboard. Goal: naturally surface
every structured-output field so we can map UUIDs to field names from the call log afterward.

## Variables to set before starting

| Variable | Value |
|---|---|
| `customer_name` | `Alex Rivera` |
| `service_type` | `Repair` |
| `request_details` | `AC unit blowing warm air, compressor makes a rattling noise` |
| `service_location` | `456 Oak Street, Austin, TX 78701` |

## Conversation script

Elliot will greet you and lead — respond naturally with these beats, in roughly this order.
Don't read it word-for-word; just hit each point so all 6 fields get captured.

**1. Opening — confirm who you are**
> "Yeah, hi, this is Alex."

**2. Describe the problem (scope_of_call)**
> "So my AC has been blowing warm air the last couple days, and there's this rattling noise
> coming from outside, I think it's the compressor."

**3. System type — mention it's a split system**
> "It's a split system unit, if that matters."

**4. Unit quantity**
> "It's just the one unit for the whole house."

**5. Urgency — make it sound pressing**
> "It's been out since Monday and it's been really hot, so honestly the sooner the better."

**6. Confirm service location (if asked)**
> "Yeah, that's 456 Oak Street, Austin, Texas."

**7. Preferred time**
> "Tomorrow morning would work great for me."

**8. Let Elliot wrap up naturally**
> Answer any closing questions (name/phone/email confirmation, diagnostic fee explanation),
> then let the assistant end the call normally — don't hang up abruptly. This matters so
> `call_status` / `endedReason` reads as a clean completion instead of `customer-ended`.

## After the call

Tell Claude the call is done — it'll pull the call from Vapi's logs via MCP, match the
structured-output UUIDs to what was said here, and use that mapping to fix the
`Format Job Details` node in the n8n workflow.
