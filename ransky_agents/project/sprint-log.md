# Project Sprint Log

## Current Sprint: M3 — Testing & Go-Live

| Agent | Status | Current Task |
|-------|--------|--------------|
| **Senior Dev** | `ACTIVE` | Designing end-to-end verification plan |
| **Backend** | `IDLE` | Sprint M2 tasks completed |

## Task Details

### M3 Tasks
- [ ] Submit a test form via n8n form trigger
- [ ] Answer the Vapi outbound call and verify Layla's conversational flow
- [ ] Verify call data is successfully extracted and updated in the "CRM - HVAC" Google Sheet
- [ ] Activate the workflow for production usage

---

## Completed Sprints

### M2 — HVAC B2C Transition
- [x] Read `docs/use-cases/n8n_HVAC_Backend_Ticket.md` to review the required node configurations
- [x] Update the `On form submission` node in `Outbound Call - HVAC` to collect B2C HVAC inputs
- [x] Update the `Call Lead` HTTP request payload to send `customer_name`, `service_type`, `request_details`, and `service_location`
- [x] Update `Log Incorrect Phone`, `Log Voicemail`, and `Log Complete` nodes in Google Sheets to match the HVAC spreadsheet columns
- [x] Map the new Vapi structured output UUIDs in the `Log Complete` node
- [x] Export the updated workflow JSON to `workflows/outbound-call-hvac.json`
- [x] Update `ransky_agents/project/api-contracts.md` with the new Google Sheets schema and Vapi payloads

### M1 — Vapi Setup & Initial Configuration
- [x] Read `reference/outbound_call_agent_context.md` for project goal
- [x] Connect Google Sheets Custom OAuth2 credentials in n8n workflow
- [x] Guide the user through setting up a Vapi.ai account and getting a free US number
- [x] Create Elliot assistant programmatically on Vapi using system prompt
- [x] Configure structured outputs in Vapi (`vapi/structured-outputs.md`)
- [x] Extract `VAPI_ASSISTANT_ID` and `VAPI_PHONE_NUMBER_ID` and map them to `api-contracts.md`
- [x] Ask the user to paste their keys into `.env` (but don't read them!)

### M0 — Project Initialization
- [x] Scaffold agent framework
- [x] Restructure directory for n8n/Vapi project
- [x] Create Vapi config templates
- [x] Sanitize repo and push to GitHub

