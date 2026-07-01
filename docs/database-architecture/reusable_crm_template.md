# Reusable Speed-to-Lead CRM Database Architecture

This document outlines a modular, highly scalable database template design for B2B and B2C Speed-to-Lead voice agency systems. By dividing the schema into **Core** and **Niche** tables, you can duplicate this base in Airtable for new clients in seconds and swap out only the niche-specific details.

---

## 🏗️ The 3-Table Modular Architecture

To prevent data duplication and allow instant adaptation to new industries (Real Estate, Solar, SaaS, HVAC, etc.), we structure the database into three tables:

```mermaid
erDiagram
    CONTACTS ||--o{ INTERACTIONS : "has"
    CONTACTS ||--o{ HVAC_DETAILS : "owns"
    INTERACTIONS ||--o|| HVAC_DETAILS : "references"
```

### Table 1: `Contacts` (Core - Global)
*Stores permanent customer identity data. No duplicate contacts.*
*   **Full Name** (Single Line Text - Primary Field)
*   **Phone** (Phone Number - E.164 validated)
*   **Email** (Email)
*   **Service Location / Company Address** (Long Text)
*   **Interactions** (Link to `Interactions` table)
*   **Niche Details** (Link to `HVAC Details` or other niche tables)

### Table 2: `Interactions` (Core - Global)
*Logs the chronological details of the outbound call attempts, status, and transcripts.*
*   **Interaction ID** (Formula: `Name + Date` - Primary Field)
*   **Contact** (Link to `Contacts` table)
*   **Date** (Created Time / Date-Time)
*   **Call Status** (Single Select: `complete`, `incomplete`, `wrong_number`, `not_a_good_time`, `hostile`)
*   **Transcript** (Long Text)
*   **Call Cost / Duration** (Number)

### Table 3: `[Niche] Details` (Swappable - Niche Specific)
*Houses the qualification data extracted by the Vapi Voice Agent. Custom-tailored to the script requirements.*

#### Example: `HVAC Details` Table:
*   **Detail ID** (Formula or Auto-number - Primary Field)
*   **Contact** (Link to `Contacts` table)
*   **Service Type** (Single Select: `Repair`, `Maintenance`, `Installation`)
*   **Customer Request** (Long Text - original web form submission)
*   **Urgency Level** (Single Select: `emergency`, `routine`, `quote_request`)
*   **HVAC System Type** (Single Select: `Central AC`, `Mini-split`, `Heat pump`, `Window unit`, `Unknown`)
*   **HVAC Unit Quantity** (Number)
*   **HVAC Issue Details** (Long Text - Vapi summarized notes)
*   **Preferred Time Slot** (Single Line Text / Date-Time)

---

## 🚀 Agency Benefits & Scaling

1.  **Cloneable System:** Keep a "Master Template" base in Airtable. When you sign a new client, duplicate the master base, delete/add the Table 3 to fit their industry, and configure n8n to point to the new base ID.
2.  **Transcripts vs. Extraction:** Separation of concerns. Table 2 stores raw logs and technical details, while Table 3 isolates human-readable lead qualification data for the client's sales team.
3.  **Flexible CRM Views:** Allows you to create standard Kanban pipeline views (e.g. Lead Pipeline) for the client's dashboard without polluting their contact directory.
