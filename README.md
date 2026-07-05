# Outbound Lead Qualifier

Automated outbound AI call system: when a lead submits a web form, an AI voice agent calls them, qualifies them through natural conversation, and logs structured results to an Airtable CRM — all without human intervention.

**Built for:** Portfolio demo (bitransky.vercel.app)
**Author:** Ransky — AI Automation Developer

## Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Orchestration | n8n | Workflow automation, HTTP requests, polling, data routing |
| Voice AI | Vapi (GPT-4o) | Outbound calling, AI conversation, structured data extraction |
| CRM | Airtable | Contacts + Service Requests (relational schema) |
| Frontend | Static HTML/CSS/JS | Lead intake form (in `frontend/`) |

## How It Works

```
Form Submitted (n8n Form/Webhook Trigger)
    │
    ▼
Standardize Data — normalizes phone number to E.164 (PH or US)
    │
    ▼
Upsert Contact (Airtable) — match/create by Phone
    │
    ▼
Incorrect Phone? ──Yes──▶ Wrong Number (Airtable: wrong_number)
    │ No
    ▼
Call Lead (Vapi POST /call)
    │
    ▼
Wait 60s ──▶ Get Call Details (Vapi GET /call/{id})
    │
    ▼
Ended? ──No──▶ Polling (Wait 10s) ──▶ [loop back to Get Call Details]
    │ Yes
    ▼
Voicemail? ──Yes──▶ Voicemail (Airtable: call_back)
    │ No
    ▼
Format Job Details ──▶ Completed (Airtable: complete, with structured outputs)
```

## Project Structure

```
├── workflows/         n8n workflow JSON export
├── vapi/              Vapi assistant config, test call scripts
├── prompts/           System prompt version history
├── docs/              API contracts, setup guide, MCP setup
├── frontend/          Lead intake form (HTML/CSS/JS)
```

## Setup

See [docs/setup-guide.md](docs/setup-guide.md) for step-by-step instructions.
