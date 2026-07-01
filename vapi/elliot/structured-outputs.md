# Vapi Structured Outputs — Elliot (Lead Qualifier)

> These are the fields Vapi extracts from the call and returns in the API response.
> Configure these in: **Vapi Dashboard → Assistant → Structured Outputs**

## Fields to Create

| # | Name | Basic Info -> Description | Result Format | Result Format -> Description |
|---|------|---------------------------|---------------|------------------------------|
| 1 | `service_interest` | Tracks if the prospect is interested in our service. | True/false (Boolean) | Set to true if the prospect expresses interest in our specific service or solution. |
| 2 | `paid_intent` | Tracks if the prospect is willing to pay for a discovery session. | True/false (Boolean) | Set to true if the prospect is willing to do a paid scoping/discovery session. |
| 3 | `Status` | The final outcome status of the call. | Text (String) | Must be exactly one of: "complete", "not_a_good_time", "wrong_number", "hostile", "incomplete". |
| 4 | `budget` | The prospect's budget. | Text (String) | What budget range does the prospect have in mind? |
| 5 | `urgency` | The prospect's timeline. | Text (String) | What is the prospect's timeline? How soon do they need this? (e.g. "immediately", "next month", "exploring") |
| 6 | `past_experience` | Has the prospect used a similar solution or service before? What was their experience? | Text (String) | Has the prospect used a similar solution or service before? What was their experience? |
| 7 | `motivation` | What is driving the prospect's need right now? What problem are they trying to solve? | Text (String) | What is driving the prospect's need right now? What problem are they trying to solve? |
| 8 | `hvac_system_type` | Tracks the type of residential AC/heating system the client has. | Text (String) | Must be exactly one of: "Central AC", "Mini-split", "Heat pump", "Window unit", "Unknown". |
| 9 | `hvac_unit_quantity` | Tracks the total number of systems or units that need servicing or installation. | Number | Number of systems or units that need installation or repair. |

## Where to Find in API Response

After the call ends, structured outputs appear in the Vapi GET `/call/{id}` response at:

```
response.artifact.structuredOutputs[<field_id>].result
```

Each field has a unique UUID assigned by Vapi. You'll need to map these IDs in the n8n Google Sheets node.

## Field ID Mapping (Fill After Setup)

| Field | Vapi UUID | 
|-------|-----------|
| service_interest | `683af6d7-2a4d-4c5b-a90c-155170996655` |
| motivation | `306135bb-63e2-4dc1-b4b4-58e1fd603559` |
| urgency | `300fa434-218e-4629-ba91-60cc62f76e39` |
| past_experience | `bebd0925-e04f-46d0-8bb8-aa57bdbfa7cc` |
| budget | `0335cf29-96d3-4efd-b20d-9fdaf0a9148a` |
| paid_intent | `d6459ce7-5104-4727-a62f-2ef523be641b` |
| status | `27f00fbf-c472-4e0a-8e66-0c8db4e46a4b` |
| hvac_system_type | `[WAITING FOR SETUP]` |
| hvac_unit_quantity | `[WAITING FOR SETUP]` |

> **Note:** The template JSON from Nate Herk has his UUIDs hardcoded. You MUST replace them with your own after creating structured outputs in your Vapi dashboard.

