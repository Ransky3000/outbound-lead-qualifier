# Vapi Structured Outputs

> These are the fields Vapi extracts from the call and returns in the API response.
> Configure these in: **Vapi Dashboard → Assistant → Structured Outputs**

## Fields to Create

| # | Field Name | Type | Description (paste into Vapi) |
|---|-----------|------|-------------------------------|
| 1 | `service_interest` | string | What specific service or solution is the prospect interested in? |
| 2 | `motivation` | string | What is driving the prospect's need right now? What problem are they trying to solve? |
| 3 | `urgency` | string | What is the prospect's timeline? How soon do they need this? (e.g., "immediately", "next month", "exploring") |
| 4 | `past_experience` | string | Has the prospect used a similar solution or service before? What was their experience? |
| 5 | `budget` | string | What budget range does the prospect have in mind? |
| 6 | `paid_intent` | string | Is the prospect willing to do a paid scoping/discovery session? (yes/no/maybe) |
| 7 | `status` | string | Final call status: "complete", "not_a_good_time", "wrong_number", "hostile", "incomplete" |

## Where to Find in API Response

After the call ends, structured outputs appear in the Vapi GET `/call/{id}` response at:

```
response.artifact.structuredOutputs[<field_id>].result
```

Each field has a unique UUID assigned by Vapi. You'll need to map these IDs in the n8n Google Sheets node.

## Field ID Mapping (Fill After Setup)

| Field | Vapi UUID | 
|-------|-----------|
| service_interest | `TBD` |
| motivation | `TBD` |
| urgency | `TBD` |
| past_experience | `TBD` |
| budget | `TBD` |
| paid_intent | `TBD` |
| status | `TBD` |

> **Note:** The template JSON from Nate Herk has his UUIDs hardcoded. You MUST replace them with your own after creating structured outputs in your Vapi dashboard.
