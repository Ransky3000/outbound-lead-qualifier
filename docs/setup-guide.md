# Setup Guide — Outbound Lead Qualifier

## Prerequisites

| Service | Status | Account URL |
|---------|--------|-------------|
| n8n (self-hosted on Hostinger) | ✅ Ready | Your Hostinger n8n instance |
| Vapi | 🟡 Account created, not configured | https://dashboard.vapi.ai |
| Twilio | ✅ Trial active ($15.50 credit) | https://console.twilio.com |
| Google Sheets | ⬜ Not set up yet | https://sheets.google.com |
| OpenAI API Key | ⬜ Needed for Vapi | https://platform.openai.com |

## Step-by-Step Setup

### Phase 1: Vapi Configuration

1. **Log into Vapi Dashboard** → https://dashboard.vapi.ai
2. **Get a free US phone number:**
   - Go to Phone Numbers → Get Number
   - Select a free US number (Vapi provides 10 free)
   - Copy the `phoneNumberId`
3. **Create the AI Assistant:**
   - Go to Assistants → Create Assistant
   - Name: "Elliot" (or your chosen name)
   - Model: OpenAI → GPT-4o
   - First Message: Set to "Wait for user to speak first"
   - System Prompt: Paste from `vapi/system-prompt.md`
   - Copy the `assistantId`
4. **Add Structured Outputs:**
   - In the assistant settings, find Structured Outputs
   - Add each field from `vapi/structured-outputs.md`
   - Copy each field's UUID after creation
5. **Get your Vapi API Key:**
   - Dashboard → API Keys → Copy private key
   - ⚠️ DO NOT commit this anywhere — store in n8n credentials only

### Phase 2: Google Sheets

1. **Create a new Google Sheet** named "Outbound Lead Qualifier"
2. **Add these column headers** (Row 1):
   ```
   Date | Name | Phone | Email | Company | Role | Request | Company Size | Service Interest | Motivation | Urgency | Past Experience | Budget | Intent? | Status
   ```
3. **Connect to n8n:** Use Google Sheets OAuth2 credential in n8n

### Phase 3: n8n Workflow

1. **Import the workflow template:**
   - In n8n, go to Workflows → Import
   - Upload `workflows/outbound-lead-qualifier-v1.json`
2. **Configure credentials:**
   - Vapi: Create HTTP Bearer Auth credential with your Vapi API key
   - Google Sheets: Connect Google Sheets OAuth2
3. **Update node values:**
   - "Call Lead" node: Replace `YOUR ASSISTANT ID` and `YOUR PHONE NUMBER ID`
   - All Google Sheets nodes: Connect to your sheet
   - Update structured output UUIDs in "Log Results" node
4. **Test the form trigger:**
   - Open the n8n form URL
   - Submit a test entry
   - Watch the workflow execute

### Phase 4: Demo Test

1. **Submit form** with your verified PH number (+XXXXXXXXXXXX)
2. **Watch n8n** execute the workflow
3. **Answer the call** on your phone
4. **Have a conversation** with Elliot
5. **Check Google Sheets** for the logged results
6. **Record the demo** 🎬

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Call doesn't initiate | Check Vapi API key, assistantId, phoneNumberId |
| Invalid phone format | Verify the Code node normalizes correctly |
| Polling never ends | Check the Wait/Get Call/IF loop — ensure status comparison is correct |
| Structured outputs empty | Verify UUIDs match YOUR Vapi dashboard, not Nate's |
| Can't call PH number | Vapi US → PH should work. If not, check Twilio verified numbers |
