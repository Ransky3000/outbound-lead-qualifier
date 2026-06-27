# API & Data Contracts

> **Single source of truth** for all API endpoints and data schemas used in this project.
> NEVER guess these — always read this file.

---

## Vapi API

**Base URL:** `https://api.vapi.ai`
**Auth:** HTTP Bearer Auth (Vapi private API key)

### POST `/call` — Create Outbound Call

**Request Body:**
```json
{
  "assistantId": "<YOUR_ASSISTANT_ID>",
  "phoneNumberId": "<YOUR_PHONE_NUMBER_ID>",
  "customers": [
    {
      "number": "+1<10_DIGIT_NUMBER>"
    }
  ],
  "assistantOverrides": {
    "variableValues": {
      "lead_name": "<from form>",
      "lead_company_name": "<from form>",
      "lead_request": "<from form>"
    }
  }
}
```

**Response (key fields):**
```json
{
  "id": "<call_id>",
  "status": "queued",
  ...
}
```

### GET `/call/{id}` — Get Call Details

**Response (key fields when status == "ended"):**
```json
{
  "id": "<call_id>",
  "status": "ended",
  "endedReason": "assistant-ended" | "voicemail" | "customer-ended" | ...,
  "artifact": {
    "structuredOutputs": {
      "<uuid>": { "result": "<extracted_value>" },
      ...
    }
  }
}
```

---

## Vapi Structured Output UUIDs

> ⚠️ Replace these with YOUR UUIDs after creating structured outputs in Vapi dashboard.

| Field | UUID | Path in Response |
|-------|------|-----------------|
| service_interest | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |
| motivation | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |
| urgency | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |
| past_experience | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |
| budget | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |
| paid_intent | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |
| status | `TBD` | `artifact.structuredOutputs['<uuid>'].result` |

---

## Google Sheets Schema

**Sheet Name:** Outbound Lead Qualifier
**Tab:** Sheet1

| Column | Type | Source | Notes |
|--------|------|--------|-------|
| Date | string | n8n `$now.format('yyyy-MM-dd hh:mm a')` | Timestamp of processing |
| Name | string | Form: Name | |
| Phone | string | Form: Phone Number | Raw from form (before normalization) |
| Email | string | Form: Email | |
| Company | string | Form: Company Name | |
| Role | string | Form: Role | |
| Request | string | Form: Request | |
| Company Size | string | Form: Company Size | Dropdown value |
| Service Interest | string | Vapi structured output | |
| Motivation | string | Vapi structured output | |
| Urgency | string | Vapi structured output | |
| Past Experience | string | Vapi structured output | |
| Budget | string | Vapi structured output | |
| Intent? | string | Vapi structured output | Paid scoping willingness |
| Status | string | Workflow logic | `Complete` / `Call Back` / `Incorrect Phone #` |

---

## n8n Credentials Required

| Credential Name | Type | Used By |
|----------------|------|---------|
| Vapi | HTTP Bearer Auth | Call Lead, Get Call Details nodes |
| Google Sheets account | Google Sheets OAuth2 | All Google Sheets nodes |
