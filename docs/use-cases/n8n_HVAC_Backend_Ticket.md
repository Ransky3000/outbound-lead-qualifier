# Backend Development Ticket: HVAC Conversion for n8n Workflow

**Status:** Ready for Implementation  
**Target Workflow:** `Outbound Call - HVAC` (ID: `izuwT3GEzZio8lS6`)  
**Objective:** Convert the existing B2B SaaS Nate Herk workflow template into a B2C HVAC outbound lead qualification workflow for Apex Heating & Air.

---

## 🛠️ Step-by-Step Backend Changes Required

### 1. Update Node: `On form submission` (Form Trigger)
Replace the existing B2B form fields with the following B2C fields:

| Field Name (Internal) | Field Label (UI) | Field Type | Required | Options (Dropdown) |
|---|---|---|:---:|---|
| `Full Name` | Name | `string` | Yes | — |
| `Phone Number` | Phone Number | `number` | Yes | — |
| `Email Address` | Email | `email` | Yes | — |
| `Service Location` | Service Location | `string` | Yes | — |
| `Service Type` | Service Type | `dropdown` | Yes | `Repair`, `Maintenance`, `New System / Installation` |
| `How can we help you?` | How can we help you? | `string` | Yes | — |

---

### 2. Update Node: `Call Lead` (Vapi POST /call HTTP Request)
Update the JSON body of the API request to send Layla's B2C dynamic overrides. 

**New JSON Request Body:**
```json
{
  "assistantId": "cba6dea6-8eb4-43cb-90f3-5f0ab228a972", // UPDATE: replace with Layla's Vapi Assistant ID once created
  "phoneNumberId": "79966c1a-008a-48c9-b0d8-3d59cee58106", // UPDATE: replace with assigned Vapi phone number ID
  "customers": [
    {
      "number": "={{ $json['Phone Number'] }}"
    }
  ],
  "assistantOverrides": {
    "variableValues": {
      "customer_name": "={{ $json['Full Name'] }}",
      "service_type": "={{ $json['Service Type'] }}",
      "request_details": "={{ $json['How can we help you?'] }}",
      "service_location": "={{ $json['Service Location'] }}"
    }
  }
}
```

---

### 3. Update Node: `Log Incorrect Phone` (Google Sheets)
Update the columns mapping to match the new HVAC spreadsheet headers.

**New Mappings:**
*   `Date`: `={{ $now.format('yyyy-MM-dd hh:mm a') }}`
*   `Name`: `={{ $json['Full Name'] }}`
*   `Phone`: `={{ $json['Phone Number'] }}`
*   `Email`: `={{ $json['Email Address'] }}`
*   `Service Location`: `={{ $json['Service Location'] }}`
*   `Service Type`: `={{ $json['Service Type'] }}`
*   `Customer Request`: `={{ $json['How can we help you?'] }}`
*   `Call Status`: `Incorrect Phone #`
*   *(Keep all other columns empty)*

---

### 4. Update Node: `Log Voicemal` (Google Sheets)
Update the column mappings.

**New Mappings:**
*   `Date`: `={{ $now.format('yyyy-MM-dd hh:mm a') }}`
*   `Name`: `={{ $('On form submission').item.json['Full Name'] }}`
*   `Phone`: `={{ $('On form submission').item.json['Phone Number'] }}`
*   `Email`: `={{ $('On form submission').item.json['Email Address'] }}`
*   `Service Location`: `={{ $('On form submission').item.json['Service Location'] }}`
*   `Service Type`: `={{ $('On form submission').item.json['Service Type'] }}`
*   `Customer Request`: `={{ $('On form submission').item.json['How can we help you?'] }}`
*   `Call Status`: `incomplete`
*   *(Keep all other columns empty)*

---

### 5. Update Node: `Log Complete` (Google Sheets)
Update mappings to reference the **new Layla Structured Output UUIDs**.

> ⚠️ **IMPORTANT for Developer:** You must first create the Structured Output fields in the Vapi dashboard to obtain the new UUIDs, then replace the placeholder UUIDs in the expressions below.

**New Mappings:**
*   `Date`: `={{ $now.format('yyyy-MM-dd hh:mm a') }}`
*   `Name`: `={{ $('On form submission').item.json['Full Name'] }}`
*   `Phone`: `={{ $('On form submission').item.json['Phone Number'] }}`
*   `Email`: `={{ $('On form submission').item.json['Email Address'] }}`
*   `Service Location`: `={{ $('On form submission').item.json['Service Location'] }}`
*   `Service Type`: `={{ $('On form submission').item.json['Service Type'] }}`
*   `Customer Request`: `={{ $('On form submission').item.json['How can we help you?'] }}`
*   `Call Status`: `={{ $json.artifact.structuredOutputs['<hvac_status_uuid>'].result }}`
*   `Urgency Level`: `={{ $json.artifact.structuredOutputs['<hvac_urgency_level_uuid>'].result }}`
*   `HVAC Issue Details`: `={{ $json.artifact.structuredOutputs['<hvac_issue_details_uuid>'].result }}`
*   `Installation Scope`: `={{ $json.artifact.structuredOutputs['<hvac_installation_scope_uuid>'].result }}`
*   `Preferred Time Slot`: `={{ $json.artifact.structuredOutputs['<hvac_preferred_time_slot_uuid>'].result }}`
