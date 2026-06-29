# HVAC Business Logic & AI Workflow

## 1. The Three Types of HVAC Jobs
When a customer contacts an HVAC company, the inquiry almost always falls into one of three categories:
*   **Emergency Repair (High Urgency):** e.g., "My AC is broken and it's 100 degrees outside." These leads need a technician dispatched ASAP.
*   **Estimates / Installations (Medium Urgency):** e.g., "I need a quote for a new AC system." These are high-value jobs ($5k-$15k) that require scheduling a sales rep or senior tech.
*   **Routine Maintenance (Low Urgency):** e.g., "I need my spring AC tune-up." Standard $99 service calls that can be scheduled flexibly.

## 2. The Current (Human) Booking Process
1. A lead submits a form on the HVAC website.
2. The form sits in an email inbox until a human dispatcher sees it.
3. The dispatcher calls the lead back (often resulting in a voicemail if too much time has passed).
4. If connected, the dispatcher asks:
    * *What exactly is the issue?*
    * *What is your address?*
    * *Are you a new or existing customer?*
    * *Is the unit accessible?*
5. The dispatcher books a "Service Window" (e.g., "Tomorrow between 1 PM and 4 PM") in their calendar software (like ServiceTitan or Housecall Pro).

## 3. The Proposed AI Agent Workflow (Vapi + n8n)
The goal of this workflow is to achieve **Speed-to-Lead** by replacing the human dispatcher for immediate online inquiries.

**Workflow Steps:**
1. Lead submits a "Request Service" web form.
2. n8n triggers the Vapi Outbound call instantly (within seconds).
3. **The Vapi AI Triage Logic:**
   * **Greeting:** "Hi, this is Elliot calling from XYZ Heating & Air. I saw you just requested service online, how can I help you today?"
   * **Triage:** The AI listens to the problem to determine urgency (Emergency vs. Estimate vs. Routine).
   * **Data Collection:** The AI collects the exact address and confirms if it's a residential property.
   * **The Close:** The AI offers a time window based on availability and confirms the booking.
4. n8n logs the collected data and updates the HVAC company's calendar/CRM.

## The Value Proposition for HVAC Owners
"You are missing emergency calls because you don't call web leads back fast enough. My AI calls them in 10 seconds, gets their address, figures out what's broken, and puts the job directly on your calendar. You never lose a lead to the competitor down the street again."
