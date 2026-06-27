# Outbound Lead Qualifier

An automated outbound AI call system that qualifies new leads in real-time. When a lead submits a form, an AI voice agent calls them, asks qualifying questions, and logs structured results to a spreadsheet — all without human intervention.

**Built for:** Portfolio demo (bitransky.vercel.app)
**Author:** Ransky — AI Automation Developer

## Tech Stack

| Layer | Tool |
|-------|------|
| Orchestration | n8n (self-hosted on Hostinger) |
| Voice AI + Telephony | Vapi |
| LLM | GPT-4o |
| Lead Source & Logging | Google Sheets |
| Demo Phone | Twilio (verified PH number) |

## How It Works

1. Lead submits a web form (n8n Form Trigger)
2. n8n normalizes the phone number
3. n8n calls the lead via Vapi API
4. AI agent qualifies the lead through conversation
5. Structured outputs are logged to Google Sheets

## Project Structure

```
├── ransky_agents/     Agent framework (roles, sprint log, architecture)
├── workflows/         n8n workflow JSON exports (versioned)
├── vapi/              Vapi assistant config, system prompt, structured outputs
├── prompts/           System prompt version history
├── docs/              Setup guide, demo recording script
├── reference/         Research materials (Nate Herk guide, original template)
├── assets/            Screenshots, demo video, portfolio media
```

## Setup

See [docs/setup-guide.md](docs/setup-guide.md) for step-by-step instructions.

## Agent Workflow

This project uses a multi-agent AI development workflow. See [ransky_agents/START_HERE.md](ransky_agents/START_HERE.md) for details.
