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
  "assistantId": "b95acc4e-94a4-475c-8073-67f5748551cb",
  "phoneNumberId": "79966c1a-008a-48c9-b0d8-3d59cee58106",
  "customer": {
    "number": "+1<10_DIGIT_NUMBER>"
  },
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

| Field | UUID | Path in Response |
|-------|------|-----------------|
| `hvac_status` | `28e67b57-0738-49c4-aefe-54294c5581a5` | `artifact.structuredOutputs['28e67b57-0738-49c4-aefe-54294c5581a5'].result` |
| `hvac_urgency_level` | `b61a80da-fb15-45b1-b985-d62b4396c059` | `artifact.structuredOutputs['b61a80da-fb15-45b1-b985-d62b4396c059'].result` |
| `hvac_issue_details` | `93ff5f79-450c-4018-a438-8cd9d2e66454` | `artifact.structuredOutputs['93ff5f79-450c-4018-a438-8cd9d2e66454'].result` |
| `hvac_installation_scope` | `e853f166-45ca-483a-a995-369b8b933f6e` | `artifact.structuredOutputs['e853f166-45ca-483a-a995-369b8b933f6e'].result` |
| `hvac_preferred_time_slot` | `2ac66287-2830-44b4-961c-efa6d2782351` | `artifact.structuredOutputs['2ac66287-2830-44b4-961c-efa6d2782351'].result` |

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
