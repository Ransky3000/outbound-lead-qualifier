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
| 6 | `hvac_system_type` | Tracks the type of residential AC/heating system the client has. | Text (String) | Must be exactly one of: "Central AC", "Mini-split", "Heat pump", "Window unit", "Unknown". |
| 7 | `hvac_unit_quantity` | Tracks the total number of systems or units that need servicing or installation. | Number | Number of systems or units that need installation or repair. |

## Where to Find in API Response

After the call ends, structured outputs appear in the Vapi GET `/call/{id}` response at:

```
response.artifact.structuredOutputs[<field_id>].result
```

Each field has a unique UUID assigned by Vapi when created. You'll need to map these IDs in the n8n Google Sheets node.

## Field ID Mapping (Fill After Setup)

| Field | Vapi UUID | 
|-------|-----------|
| `hvac_status` | `28e67b57-0738-49c4-aefe-54294c5581a5` |
| `hvac_urgency_level` | `b61a80da-fb15-45b1-b985-d62b4396c059` |
| `hvac_issue_details` | `93ff5f79-450c-4018-a438-8cd9d2e66454` |
| `hvac_installation_scope` | `e853f166-45ca-483a-a995-369b8b933f6e` |
| `hvac_preferred_time_slot` | `2ac66287-2830-44b4-961c-efa6d2782351` |
| `hvac_system_type` | `7ca79e52-b573-43ee-b26c-8ff21ecd36d4` |
| `hvac_unit_quantity` | `65400e62-30c3-4f47-be41-89b2d170b321` |

