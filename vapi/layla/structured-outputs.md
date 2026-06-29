# Vapi Structured Outputs — Layla (HVAC Agent)

> These are the fields Vapi extracts from the call and returns in the API response.
> Configure these in: **Vapi Dashboard → Assistant → Structured Outputs**

## Fields to Create

| # | Name | Basic Info -> Description | Result Format | Result Format -> Description / Options |
|---|------|---------------------------|---------------|----------------------------------------|
| 1 | `hvac_status` | The final outcome status of the HVAC call. | Text (String) | Must be exactly one of: `"complete"`, `"not_a_good_time"`, `"wrong_number"`, `"hostile"`, `"incomplete"`. |
| 2 | `hvac_urgency_level` | The level of urgency for the HVAC request. | Text (String) | Must be exactly one of: `"emergency"` (AC/heat completely down), `"routine"` (maintenance/repairs needed but system still running), `"quote_request"` (new installation inquiry). |
| 3 | `hvac_issue_details` | Detailed description of the system issues reported. | Text (String) | Provide details of the problem described (e.g. blowing warm air, making noise, thermostat blank). |
| 4 | `hvac_installation_scope` | Scope of the new installation if applicable. | Text (String) | Provide details of the house type, number of rooms or units to replace. |
| 5 | `hvac_preferred_time_slot` | The preferred appointment time slot agreed on. | Text (String) | Capture the scheduling window agreed upon (e.g. tomorrow morning, Thursday afternoon). |

## Where to Find in API Response

After the call ends, structured outputs appear in the Vapi GET `/call/{id}` response at:

```
response.artifact.structuredOutputs[<field_id>].result
```

Each field has a unique UUID assigned by Vapi when created. You'll need to map these IDs in the n8n Google Sheets node.

## Field ID Mapping (Fill After Setup)

| Field | Vapi UUID | 
|-------|-----------|
| `hvac_status` | *(Fill this in once created in Vapi Dashboard)* |
| `hvac_urgency_level` | *(Fill this in once created in Vapi Dashboard)* |
| `hvac_issue_details` | *(Fill this in once created in Vapi Dashboard)* |
| `hvac_installation_scope` | *(Fill this in once created in Vapi Dashboard)* |
| `hvac_preferred_time_slot` | *(Fill this in once created in Vapi Dashboard)* |
