# Vapi Assistant Configuration — Elliot (Lead Qualifier)

## Assistant Settings

| Setting | Value | Notes |
|---------|-------|-------|
| **Name** | Elliot | Outbound lead qualifier persona |
| **Model Provider** | OpenAI | Via Vapi |
| **Model** | GPT-4o | Primary conversation model |
| **First Message** | *(Wait for user to speak first)* | More natural for outbound calls — let the person say "Hello?" first |
| **Voice** | Vapi built-in (TBD) | Select from Vapi voice library |

## Phone Number

| Setting | Value |
|---------|-------|
| **Type** | Vapi free US number |
| **Caller ID** | Assigned by Vapi (one of 10 free numbers) |
| **Demo Target** | +XXXXXXXXXXXX (verified via Twilio) |

## Key IDs (Fill After Setup)

| ID | Value | Where to Get It |
|----|-------|-----------------|
| `assistantId` | `cba6dea6-8eb4-43cb-90f3-5f0ab228a972` | Vapi Dashboard → Assistants → Copy ID |
| `phoneNumberId` | `2ac88210-0b54-48e7-b6e5-f78c12adde5c` | Vapi Dashboard → Phone Numbers → Copy ID |
| Vapi API Key | *(stored in n8n credentials, NOT here)* | Vapi Dashboard → API Keys |

## Structured Outputs

See [structured-outputs.md](./structured-outputs.md) for field definitions.

## Status

- [x] Assistant created in Vapi dashboard
- [x] System prompt configured
- [x] Structured outputs added
- [x] Phone number assigned
- [ ] First test call completed
