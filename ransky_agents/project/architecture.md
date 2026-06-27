# Architecture & Conventions

## Project Overview

**Outbound Lead Qualifier** — An automated outbound call system that qualifies new leads via AI voice agent. Built as a portfolio demo piece.

## Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| **Orchestration** | n8n (self-hosted on Hostinger) | Workflow automation, HTTP requests, polling, data routing |
| **Voice AI** | Vapi | Outbound calling, AI conversation, structured data extraction |
| **LLM** | GPT-4o (via Vapi) | Powers the AI agent's conversation |
| **Telephony (Outbound)** | Vapi free US number | Caller ID for outbound calls |
| **Telephony (Receiver)** | Twilio ($15 trial credit) | Verified PH caller ID (+XXXXXXXXXXXX) |
| **Lead Source / Logging** | Google Sheets | Input form data + output qualification results |

## Workflow Architecture

```
Form Trigger
    │
    ▼
Code: Normalize Phone
    │
    ▼
IF: Invalid Phone? ──Yes──▶ Log Incorrect Phone (Google Sheets)
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
Limit (1 item)
    │
    ▼
IF: Status == "ended"? ──No──▶ Wait 10s ──▶ [Loop back to Get Call Details]
    │ Yes
    ▼
IF: Voicemail? ──Yes──▶ Log Voicemail (Google Sheets, Status: "Call Back")
    │ No
    ▼
Log Results (Google Sheets, Status: "Complete", with structured outputs)
```

## Data Flow

### Input (Form Submission)
| Field | Type | Required |
|-------|------|----------|
| Name | text | ✅ |
| Phone Number | number | ✅ |
| Email | email | ✅ |
| Company Name | text | ✅ |
| Role | text | ✅ |
| Request | text | ✅ |
| Company Size | dropdown (1, 2-10, 11-50, 51-100, 101+) | ✅ |

### Output (Google Sheets)
| Column | Source |
|--------|--------|
| Date | `$now` |
| Name – Company Size | Form submission |
| Service Interest – Paid Intent | Vapi structured outputs |
| Status | Workflow logic (Complete / Call Back / Incorrect Phone) |

## Conventions

- **Workflow versions:** Stored in `workflows/` as JSON, named with `-v1`, `-v2`, etc.
- **System prompts:** Active version in `vapi/system-prompt.md`, history in `prompts/`
- **No hardcoded secrets:** API keys stored only in n8n credentials, never in repo files
- **Phone format:** All US numbers normalized to 10-digit format, prefixed with `+1` at call time
