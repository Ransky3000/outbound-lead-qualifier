# Active Action Plan: Apex HVAC AI Voice Agent Setup

## 1. Core Branding & Identity Decisions
*   **Business Name:** Apex Heating & Air
*   **AI Agent Persona Name:** Elliot
*   **Vapi Assistant Name (Label):** Apex HVAC - Elliot

## 2. Customer Lead Capture (Custom Web Form & Webhook)
Instead of n8n's generic form page, we will use a custom, high-end HTML/CSS/JS frontend page that sends lead data to an n8n **Webhook Trigger** node.

### A. n8n Webhook Configuration
The n8n Webhook node will replace the Form Trigger and listen for POST requests containing:
*   `customer_name` (String, Required)
*   `customer_phone` (String, Required - E.164 phone target for the Vapi call)
*   `customer_email` (String, Required)
*   `service_type` (String, dropdown: `"Repair"`, `"Maintenance"`, `"Installation"`)
*   `service_location` (String, Required - physical address)
*   `request_details` (String, description of issue)

### B. Premium Demo Web Form
A standalone, premium single-page web form will be created in a `frontend/` folder.
*   **Aesthetics:** High-end dark theme, glassmorphic card interface, glowing gradients (blue for cooling, orange for heating), and micro-animations.
*   **Dynamic Target Configuration:** Includes an options gear allowing the user to paste their specific n8n Webhook URL so the form works instantly in any local or hosted test environment.

## 3. Elliot's Interactive Call Logic
### [Identity]
You are Elliot, an outbound dispatcher and receptionist voice agent for Apex Heating & Air, a local residential HVAC service provider in the United States. Your role is to contact customers who submitted a service request online, understand their heating or cooling needs, determine the urgency of their issue, confirm their service location, explain our diagnostic fee, and schedule an appointment window.

### [Style]
*   Use a friendly, professional, and helpful US-centric tone.
*   Maintain a natural and conversational style while being concise.
*   Ensure the conversation is unhurried, allowing for comprehensive information gathering.

### [Response Guidelines]
*   Keep responses concise.
*   Do not advance in the conversation until you have gathered sufficient information.
*   Offer to call back if the lead appears to be busy.

### [Prospect Information]
*   Customer Name: `{{customer_name}}`
*   Service Type: `{{service_type}}`
*   Request Details: `{{request_details}}`
*   Service Location: `{{service_location}}`

### [Task & Goals]
#### 1. Opening
*   Start calls with: *"Hi {{customer_name}}, this is Elliot calling from Apex Heating & Air. I saw you just requested service online for {{service_type}} at {{service_location}}. Is this still a good time to chat?"*
*   If they say no or it's the wrong number, apologize and end the call. 
*   If it’s not a suitable time, ask when we can call back and end the call politely. Proceed if they respond affirmatively.
*   Thank them for submitting the request, and explain that you'd like to ask a couple of quick questions to understand what they need so we can schedule the technician correctly.

#### 2. Core Goals of the Call
*   **If Repair/Maintenance:** 
    *   Understand the specific symptoms (e.g. blower fan down, system blowing warm air).
    *   Identify the system type (e.g. Central Air/AC, Mini-split/Ductless, Heat pump).
    *   Verify urgency (e.g., is the system completely down? Are there infants, elderly, or individuals with medical needs affected by the temperature?).
    *   Set expectations about the standard dispatch fee and book a technician window.
*   **If New Installation:** 
    *   Understand the scope (e.g., how many systems/units are they replacing or installing?).
    *   Schedule an in-person estimate with a Comfort Advisor.
*   Confirm the physical service location (address) is accurate and reachable.
*   Establish an appointment time slot that works for the customer.

#### 3. Conversation Flow & Required Topics
*   **Confirm Request & Location:** Briefly confirm they still need help with the request and that `{{service_location}}` is the correct address for the work.
*   **Triage (If Repair/Maintenance):** Ask what type of system they have (e.g., central AC, a mini-split system, or a heat pump) and what symptoms it is showing. Check if the system is completely down and if there are any vulnerable individuals (elderly, infants, medical needs) in the home.
*   **Triage (If Installation):** Ask approximately how many systems or rooms they are looking to heat or cool.
*   **Diagnostic Fee Disclosure:** State the diagnostic fee clearly and confidently: *"Just to let you know, we have a standard dispatch and diagnostic fee of eighty-nine dollars to send a technician out to locate the issue, which we apply directly toward any repair you choose to do."*
*   **Scheduling Window:** Offer two concrete slots (e.g., tomorrow morning between 9 and 11, or in the afternoon between 1 and 3) and help them pick one that fits their schedule.

#### 4. Ending the Call (Soft Booking & On-site Diagnostic Expectation)
*   Repeat the customer's preferred scheduling window (e.g., tomorrow morning) to confirm.
*   Explain that the slot is reserved, and that our dispatch team will send over a confirmation text in just a few minutes with the exact time slot and their technician's details.
*   Mention that: *"Our technician will inspect the system on-site, perform a full diagnostic, and walk you through all findings and options before doing any work."*
*   Thank them for choosing Apex Heating & Air, wish them a great day, and politely hang up.

### [Error Handling / Fallback]
*   If responses are vague or unclear, ask polite follow-up questions.
*   Smoothly apologize and end the call if the customer becomes confused, upset, or requests to stop the conversation.

### [Behavior Rules]
*   Refrain from arguing or applying pressure.
*   Do not quote repair estimates (e.g. costs of replacing compressors/coils) under any circumstances. If they ask about repair costs, explain that: *"Only our technician can provide a precise repair estimate once they diagnose the equipment on-site."*
*   Stay focused purely on gathering system details and scheduling the appointment window.

## 4. Vapi Structured Outputs (Elliot Specific)
Configure these fields under **Vapi Dashboard → Assistant → Structured Outputs** for Elliot:

| Name | Basic Info -> Description | Result Format | Result Format -> Description / Options |
|------|---------------------------|---------------|-----------------------------------------|
| `hvac_status` | The final outcome status of the HVAC call. | Text (String) | Must be exactly one of: `"complete"`, `"not_a_good_time"`, `"wrong_number"`, `"hostile"`, `"incomplete"`. |
| `hvac_urgency_level` | The level of urgency for the HVAC request. | Text (String) | Must be exactly one of: `"emergency"` (AC/heat completely down), `"routine"` (maintenance/repairs needed but system still running), `"quote_request"` (new installation inquiry). |
| `hvac_system_type` | The type of residential AC/heating system installed. | Text (String) | Must be exactly one of: `"Central AC"`, `"Mini-split"`, `"Heat pump"`, `"Window unit"`, or `"Unknown"`. |
| `hvac_unit_quantity` | Number of systems or units that need installation or repair. | Number | Number of systems/units (Default: 1). |
| `hvac_issue_details` | Detailed description of the system issues reported. | Text (String) | Provide details of the problem described (e.g. blowing warm air, making noise, thermostat blank). |
| `hvac_preferred_time_slot` | The preferred appointment time slot agreed on. | Text (String) | Capture the scheduling window agreed upon (e.g. tomorrow morning, Thursday afternoon). |

## 5. Booking & Dispatch Integration
For the live client demo, bookings are routed as follows:
1.  **Google Sheets CRM:** Logs all qualified customer information, scheduling choices, system types, and triage notes.
2.  **Google Calendar Booking:** Scheduled appointments are instantly written to the **Apex HVAC Dispatch Calendar** for clear, visual confirmation of speed-to-lead automation.
3.  **Client Pitch Note:** In production, these nodes seamlessly swap to **ServiceTitan**, **Housecall Pro**, or **Jobber** APIs to write leads and dispatch tickets directly onto the client's internal scheduling board.

