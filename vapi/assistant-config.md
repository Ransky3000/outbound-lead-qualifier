# Vapi Assistant Configuration

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
| `assistantId` | `YOUR_ASSISTANT_ID` | Vapi Dashboard → Assistants → Copy ID |
| `phoneNumberId` | `YOUR_PHONE_NUMBER_ID` | Vapi Dashboard → Phone Numbers → Copy ID |
| Vapi API Key | *(stored in n8n credentials, NOT here)* | Vapi Dashboard → API Keys |

## Structured Outputs

See [structured-outputs.md](./structured-outputs.md) for field definitions.

## Status

- [ ] Assistant created in Vapi dashboard
- [ ] System prompt configured
- [ ] Structured outputs added
- [ ] Phone number assigned
- [ ] First test call completed
