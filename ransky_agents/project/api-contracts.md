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
  "assistantId": "cba6dea6-8eb4-43cb-90f3-5f0ab228a972",
  "phoneNumberId": "79966c1a-008a-48c9-b0d8-3d59cee58106",
  "customers": [
    {
      "number": "+1<10_DIGIT_NUMBER>"
    }
  ],
  "assistantOverrides": {
    "variableValues": {
      "customer_name": "<from form>",
      "service_type": "<from form>",
      "request_details": "<from form>",
      "service_location": "<from form>"
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
| `hvac_status` | `<hvac_status_uuid>` | `artifact.structuredOutputs['<hvac_status_uuid>'].result` |
| `hvac_urgency_level` | `<hvac_urgency_level_uuid>` | `artifact.structuredOutputs['<hvac_urgency_level_uuid>'].result` |
| `hvac_issue_details` | `<hvac_issue_details_uuid>` | `artifact.structuredOutputs['<hvac_issue_details_uuid>'].result` |
| `hvac_installation_scope` | `<hvac_installation_scope_uuid>` | `artifact.structuredOutputs['<hvac_installation_scope_uuid>'].result` |
| `hvac_preferred_time_slot` | `<hvac_preferred_time_slot_uuid>` | `artifact.structuredOutputs['<hvac_preferred_time_slot_uuid>'].result` |

---

## Google Sheets Schema

**Sheet Name:** Outbound Call - HVAC
**Tab:** Sheet1

| Column | Type | Source | Notes |
|--------|------|--------|-------|
| Date | string | n8n `$now.format('yyyy-MM-dd hh:mm a')` | Timestamp of processing |
| Name | string | Form: Full Name | |
| Phone | string | Form: Phone Number | Raw from form (before normalization) |
| Email | string | Form: Email Address | |
| Service Location | string | Form: Service Location | |
| Service Type | string | Form: Service Type | Dropdown value |
| Customer Request | string | Form: How can we help you? | |
| Call Status | string | Workflow logic / Vapi structured output | `Incorrect Phone #` / `incomplete` / Vapi `hvac_status` |
| Urgency Level | string | Vapi structured output | |
| HVAC Issue Details | string | Vapi structured output | |
| Installation Scope | string | Vapi structured output | |
| Preferred Time Slot | string | Vapi structured output | |

---

## n8n Credentials Required

| Credential Name | Type | Used By |
|----------------|------|---------|
| Vapi | HTTP Bearer Auth | Call Lead, Get Call Details nodes |
| Google Sheets account | Google Sheets OAuth2 | All Google Sheets nodes |
