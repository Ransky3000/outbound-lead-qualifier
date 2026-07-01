# Vapi Assistant Configuration — Layla (HVAC Agent)

## Assistant Settings

| Setting | Value | Notes |
|---------|-------|-------|
| **Name** | Apex HVAC - Layla | Outbound receptionist/dispatcher persona |
| **Model Provider** | OpenAI | Via Vapi |
| **Model** | GPT-4o | Primary conversation model |
| **First Message** | *(Wait for user to speak first)* | Let the contact say "Hello?" first |
| **Voice** | Vapi built-in (TBD) / ElevenLabs | Choose a warm, professional voice |

## Phone Number

| Setting | Value |
|---------|-------|
| **Type** | Vapi free US number |
| **Caller ID** | Assigned by Vapi |

## Key IDs (Fill After Setup)

| ID | Value | Where to Get It |
|----|-------|-----------------|
| `assistantId` | `b95acc4e-94a4-475c-8073-67f5748551cb` | Vapi Dashboard → Assistants → Copy ID |
| `phoneNumberId` | *(Fill after assigning in Vapi dashboard)* | Vapi Dashboard → Phone Numbers → Copy ID |

## Structured Outputs

See [structured-outputs.md](./structured-outputs.md) for field definitions.

## Status

- [ ] Assistant created in Vapi dashboard
- [ ] System prompt configured
- [ ] Structured outputs added
- [ ] Phone number assigned
- [ ] First test call completed
