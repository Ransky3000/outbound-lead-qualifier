# Project Context: Outbound AI Call System

## Who I Am
- Name: Ransky, AI Automation Developer/Consultant based in the Philippines
- Goal: Build an outbound AI call system demo for my portfolio using n8n + Vapi

## What We're Building
An automated outbound call system that:
1. Reads leads from a Google Sheet
2. n8n triggers the outbound call workflow
3. Vapi AI agent calls the lead's phone number
4. AI agent handles the conversation autonomously

## Tech Stack (Final Decision)
| Layer | Tool |
|---|---|
| Orchestration / Workflow | n8n |
| Voice AI Agent + Telephony | **Vapi** (all-in-one) |
| Phone Number | **Vapi free US number** (no Twilio needed) |
| Voice/TTS | Vapi built-in voices |
| Leads source | Google Sheets |

## Why Vapi (Not ElevenLabs)
ElevenLabs was the original plan but hit a wall:
- ElevenLabs phone number import only accepts purchased Twilio numbers
- Twilio PH numbers cost $15–120/month (too expensive for demo)
- Telnyx blocked PH signups (requires business email)
- Plivo blocked PH region entirely

Vapi solves everything:
- Provides 10 free US phone numbers out of the box
- No SIP trunk setup needed
- No Twilio account needed
- Free US number can call our verified PH number (+XXXXXXXXXXXX) for demo

## ElevenLabs Status
NOT needed anymore. Vapi handles voice + telephony + agent orchestration together.
ElevenLabs can optionally be added later as a premium TTS voice provider inside Vapi
if a client requires it — but not required for the demo.

## Twilio Status
- Trial account active ($15.50 credit remaining)
- Verified Caller ID: +XXXXXXXXXXXX already verified
- Only needed so Vapi's US number can call the PH number during demo
  (Twilio trial restricts outbound to verified numbers only — but we're receiving,
  not sending, so this doesn't apply to Vapi's outbound call)

## What's NOT Built Yet
- Vapi account not created yet
- Vapi AI agent not configured yet
- n8n workflow not built yet
- Agent system prompt / demo script not written yet

## Demo Goal
Record a screen + phone video showing:
1. Google Sheets with lead data visible
2. n8n workflow being triggered manually
3. Phone ringing (+XXXXXXXXXXXX) and AI agent conversation happening
4. Call logs / transcript as proof

This demo will be published on portfolio: bitransky.vercel.app

## Next Steps to Build
1. Create Vapi account at dashboard.vapi.ai
2. Get a free US phone number in Vapi
3. Create and configure the AI agent (name, voice, system prompt, first message)
4. Build the n8n workflow: Google Sheets → HTTP Request → Vapi /call endpoint
5. Test: trigger n8n → Vapi calls +XXXXXXXXXXXX → AI conversation
6. Record demo video

## Key Constraints
- Budget: minimal (free tiers only for now)
- Location: Philippines — Telnyx and Plivo both block PH signups
- Target demo audience: potential clients viewing portfolio (international/US market)
