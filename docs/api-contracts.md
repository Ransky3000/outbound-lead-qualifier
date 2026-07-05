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

Vapi keys `artifact.structuredOutputs` by UUID, not by field name — but each entry also
carries its own stable `name`, e.g. `{ "name": "urgency", "result": "..." }`. The n8n
`Format Job Details` node looks up values **by `name`**, not by hardcoded UUID, so it
survives Vapi assistant rebuilds that regenerate these IDs. The table below is reference
only (current as of 2026-07-02) — do not hardcode these UUIDs in new code.

| Field (`name`) | Current UUID (reference only) |
|-------|------|
| `call_status` | `fd578541-16b7-48dd-b6a8-8e971a50a793` |
| `urgency` | `63cdeb34-ebd4-4434-b384-d2f747cbb7be` |
| `scope_of_call` | `67720cb4-9f86-4505-8bdf-a08360ea7439` |
| `system_type` | `871d2fcc-0e71-4cc0-bb70-456ab2a6837e` |
| `unit_quantity` | `f34102d7-c6f1-4367-ba7e-4b9d4ce263bd` |
| `preferred_time` | `e0c88029-508c-40dd-a7b9-14ec0a2a00ef` |


---

## Airtable CRM Schema

**Base Name:** Apex HVAC CRM (`appTgp7XEjZ9A9nE3`)

### 1. Contacts Table (`tblSQb7u5OkLPdXs9`)
Used to store customer profiles. Match key is `Phone`.

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| `Name` | Single line text | Form: Full Name | |
| `Phone` | Single line text | Form: Phone Number | Standardized/cleaned phone number |
| `Email` | Email | Form: Email Address | |

`Service Location` was removed from this table (2026-07-02) — a customer's address is
per-job, not a stable identity attribute (rentals, multiple properties, etc.), so it now
lives on Service Requests instead. See below.

### 2. Service Requests Table (`tblOJ99hfaDq9dcAc`)
Used to log call status, service type, urgency, and job details.

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| `Contact` | Link to Contacts | Upserted Contact ID | Relation to customer profile |
| `Date` | Date/Time | n8n `{{ $now.toISODate() }}` | Date of call completion (date-only field — Airtable rejects a full timestamp) |
| `Call Status` | Single select | Vapi status / Wrong phone | `wrong_number`, `call_back`, `complete` |
| `Service Type` | Single select | Form Service Type | `Repair`, `Maintenance`, `Installation`, `Inspection` |
| `Service Location` | Long text | Form: Service Location (via `Standardize Data`) | The address for *this specific* call — authoritative per-request, does not get overwritten by later submissions |
| `Urgency` | Long text | Vapi structured output | Elliot's 1-sentence assessment of urgency |
| `Job Details` | Long text | n8n Format Job Details | Contains scope, system type, unit qty, and preferred time |

---

## n8n Credentials Required

| Credential Name | Type | Used By |
|----------------|------|---------|
| Vapi | HTTP Bearer Auth | Call Lead, Get Call Details nodes |
| Airtable account | Airtable Token | All Airtable nodes |

