# Setup Guide — Outbound Lead Qualifier

## Prerequisites

| Service | Purpose | Account URL |
|---------|---------|-------------|
| n8n | Workflow orchestration (self-hosted or cloud) | https://n8n.io |
| Vapi | Outbound voice AI + telephony | https://dashboard.vapi.ai |
| Airtable | CRM (Contacts + Service Requests) | https://airtable.com |
| OpenAI API Key | LLM used by the Vapi assistant (GPT-4o) | https://platform.openai.com |
| Twilio *(optional)* | Verified caller ID for regions Vapi doesn't cover natively | https://console.twilio.com |

## Step-by-Step Setup

### Phase 1: Vapi Configuration

1. **Log into the Vapi Dashboard** → https://dashboard.vapi.ai
2. **Get a phone number:**
   - Go to Phone Numbers → Get Number
   - Copy the `phoneNumberId`
3. **Create the AI Assistant:**
   - Go to Assistants → Create Assistant
   - Model: OpenAI → GPT-4o
   - First Message: Set to "Wait for user to speak first"
   - System Prompt: Paste from `prompts/system-prompt-v2.md`
   - Copy the `assistantId`
   - Reference `vapi/vapi_assistant_full.json` for the complete assistant config (voice, model settings, tools) if you want to import it directly instead of configuring by hand
4. **Add Structured Outputs:**
   - In the assistant settings, add the structured output fields: `call_status`, `urgency`, `scope_of_call`, `system_type`, `unit_quantity`, `preferred_time`
   - Vapi assigns each a UUID on creation — **don't hardcode these**. The workflow's `Format Job Details` node looks fields up by their stable `name`, not UUID, so it survives assistant rebuilds. See `docs/api-contracts.md` for details.
5. **Get your Vapi API Key:**
   - Dashboard → API Keys → Copy private key
   - ⚠️ DO NOT commit this anywhere — store in n8n credentials only

### Phase 2: Airtable CRM

1. **Create a base** (e.g. "HVAC CRM") with two tables:

   **Contacts**
   | Field | Type |
   |-------|------|
   | Name | Single line text |
   | Phone | Single line text (match key) |
   | Email | Email |

   **Service Requests**
   | Field | Type |
   |-------|------|
   | Contact | Link to Contacts |
   | Date | Date |
   | Call Status | Single select: `wrong_number`, `call_back`, `complete` |
   | Service Type | Single select: `Repair`, `Maintenance`, `Installation`, `Inspection` |
   | Service Location | Long text |
   | Urgency | Long text |
   | Job Details | Long text |

2. **Generate a Personal Access Token** with read/write scope on this base — used for the n8n Airtable credential.

Full field-level schema and notes: `docs/api-contracts.md`.

### Phase 3: n8n Workflow

1. **Import the workflow:**
   - In n8n, go to Workflows → Import
   - Upload `workflows/outbound-call-hvac-updated.json`
2. **Configure credentials:**
   - **Vapi**: Create an HTTP Bearer Auth credential with your Vapi API key, attach it to the `Call Lead` and `Get Call Details` nodes
   - **Airtable**: Create an Airtable Personal Access Token credential, attach it to all Airtable nodes and point them at your base/tables from Phase 2
3. **Update node values:**
   - `Call Lead` node: replace the placeholder `assistantId` and `phoneNumberId` in the JSON body with your own from Phase 1
4. **Test the form trigger:**
   - Open the n8n form/webhook test URL for the `Form Submitted` node
   - Submit a test entry and watch the workflow execute

### Phase 4: Connect the Frontend

1. Open `frontend/app.js` and set the form's submit target to your n8n `Form Submitted` webhook's **production** URL (not the test URL)
2. Serve `frontend/` (e.g. a static host, or locally with `python -m http.server`) and submit a test lead to confirm end-to-end delivery

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Call doesn't initiate | Check the Vapi credential's API key, and the `assistantId`/`phoneNumberId` in `Call Lead` |
| Invalid phone format | Check `Standardize Data` — it expects PH (`09...`/`+63...`) or US (10-digit/`+1...`) numbers |
| Polling never ends | Check the `Wait` → `Get Call Details` → `Ended?` → `Polling` loop; confirm the status comparison matches Vapi's actual `status` field |
| Structured outputs empty | Confirm your assistant's structured output field **names** match what `Format Job Details` looks up (see `docs/api-contracts.md`) — UUIDs will differ per account/rebuild, names must not |
| Airtable write fails | Confirm the Airtable credential's token has access to the base, and that `Contacts`/`Service Requests` field names match exactly |
