# Outbound Lead Qualifier

Automated outbound AI call system: when a lead submits a web form, an AI voice agent (Layla) calls them, qualifies them through natural conversation, and logs structured results to an Airtable CRM — all without human intervention.

**Built for:** Portfolio demo (bitransky.vercel.app)
**Author:** Ransky — AI Automation Developer

## Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Orchestration | n8n (self-hosted on Hostinger) | Workflow automation, HTTP requests, polling, data routing |
| Voice AI | Vapi (GPT-4o) | Outbound calling, AI conversation, structured data extraction |
| Telephony (Outbound) | Vapi free US number | Caller ID for outbound calls |
| Telephony (Receiver) | Twilio ($15 trial credit) | Verified PH caller ID |
| CRM | Airtable | Contacts + Service Requests (relational schema) |
| Frontend | Static HTML/CSS/JS | HVAC intake form (in `frontend/`) |

## Workflow Architecture

```
Form Trigger
    │
    ▼
Code: Normalize Phone
    │
    ▼
IF: Invalid Phone? ──Yes──▶ Log Incorrect Phone (Airtable)
    │ No
    ▼
HTTP: Call Lead (Vapi POST /call)
    │
    ▼
Wait 60s
    │
    ▼
HTTP: Get Call Details (Vapi GET /call/{id})
    │
    ▼
IF: Status == "ended"? ──No──▶ Wait 10s ──▶ [Loop back]
    │ Yes
    ▼
IF: Voicemail? ──Yes──▶ Log "Call Back" (Airtable)
    │ No
    ▼
Log Complete Results (Airtable, with structured outputs)
```

## Project Structure

```
├── workflows/         n8n workflow JSON exports (versioned)
├── vapi/              Vapi assistant config, system prompt, call test data
├── prompts/           System prompt version history
├── docs/              Architecture, API contracts, setup guide, demo scripts
├── reference/         Nate Herk PDF, original template, research materials
├── frontend/          HVAC intake form (HTML/CSS/JS)
├── assets/            Screenshots, demo video, portfolio media
├── .mcp.json          MCP server config with API keys (gitignored)
├── .env               Local credential vault (gitignored)
└── .env.example       Credential template
```

## Key References

Read these before editing integration code:

- **API contracts** (Vapi endpoints, structured output UUIDs, Airtable schema): `docs/api-contracts.md`
- **Setup guide:** `docs/setup-guide.md`
- **MCP setup:** `docs/mcp-setup.md`

## Conventions

- Workflow versions: stored as JSON in `workflows/`, named with `-v1`, `-v2` suffix
- System prompts: active version in `vapi/`, history in `prompts/`
- No hardcoded secrets — API keys only in n8n credentials, `.env`, or `.mcp.json`
- Phone format: US numbers normalized to 10-digit, prefixed `+1` at call time
- Git: Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`)

## MCP Servers

MCP servers are configured in `.mcp.json` (project root, gitignored). Available integrations:

| Server | What It Does | Key Operations |
|--------|-------------|----------------|
| **n8n** | Manage n8n workflows on Hostinger | Search/create/update/execute workflows, manage credentials, search nodes |
| **n8n-docs** | Search n8n documentation | Semantic search over n8n docs and knowledge base |
| **Vapi** | Manage voice agents | Create/update assistants, make calls, manage phone numbers & tools |
| **Airtable** | Manage CRM data | CRUD on records, create tables/fields, search records |
| **GitHub** | Manage repository | Create PRs, push files, manage issues, search code |

**Prefer MCP tools over manual API calls:**
- Use n8n MCP to modify workflows instead of editing JSON
- Use Vapi MCP to update assistant config instead of raw HTTP
- Use Airtable MCP to inspect/modify CRM schema and data
- Use GitHub MCP for version control operations

## Current State

Project is at **M3 (Testing & Go-Live)**. All development complete:

- ✅ Vapi assistant configured (Layla — HVAC B2C voice agent)
- ✅ n8n workflow: form → call → poll → CRM logging
- ✅ Airtable CRM with relational schema (Contacts ↔ Service Requests)
- ✅ Frontend HVAC intake form
- 🔲 End-to-end live test pending (submit form → answer call → verify CRM entry)
