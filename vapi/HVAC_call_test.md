# 📞 HVAC Call Test Script: Scenario 1 (Urgent Repair)

**Purpose:** Use this script when testing the assistant directly in the Vapi Dashboard (via the Web/Mic button). This "Happy Path" script is designed to successfully trigger all of Elliot's instructions, confirm the $89 diagnostic fee, and extract all required structured outputs for the CRM.

**Assumed Lead Data (from Webhook context):**
*   **Customer Name:** Ranian
*   **Service Type:** Repair
*   **Service Location:** 4928 Sycamore Drive in Scottsdale

---

### The Script

| Speaker | Dialogue |
| :--- | :--- |
| **Elliot (AI)** | *"Hi Ranian, this is Elliot calling from Apex Heating & Air. I saw you just requested service online for Repair at 4928 Sycamore Drive in Scottsdale. Is this still a good time to chat?"* |
| **Ranian (You)** | **"Yes, this is Ranian. Now is a good time."** |
| **Elliot (AI)** | *(Will likely thank you and ask about what the system is doing, if it's down, etc.)* |
| **Ranian (You)** | **"Yes, my air conditioner is completely down. It's blowing warm air and making a loud buzzing noise outside. We have a newborn in the house and it's getting really hot, so this is an emergency."** <br><br>*(🔑 Triggers `hvac_urgency_level`: emergency, `hvac_issue_details`)* |
| **Elliot (AI)** | *(Will express empathy and ask what type of system you have - Central AC, Mini-split, etc.)* |
| **Ranian (You)** | **"It's a central AC system. Just one unit for the whole house."** <br><br>*(🔑 Triggers `hvac_system_type`: Central AC, `hvac_unit_quantity`: 1)* |
| **Elliot (AI)** | *(Will note it down and explain the standard $89 dispatch/diagnostic fee.)* |
| **Ranian (You)** | **"Yes, the $89 fee is fine. We just need someone out here as soon as possible."** |
| **Elliot (AI)** | *(Will confirm the address is 4928 Sycamore Drive in Scottsdale and offer two scheduling windows, e.g., tomorrow morning or afternoon.)* |
| **Ranian (You)** | **"Tomorrow morning works best for us."** <br><br>*(🔑 Triggers `hvac_preferred_time_slot`: tomorrow morning)* |
| **Elliot (AI)** | *(Will confirm the booking, explain that a confirmation text is coming, mention the on-site diagnostic process, and ask if there's anything else.)* |
| **Ranian (You)** | **"No, that's all. Thank you so much!"** |
| **Elliot (AI)** | *(Will thank you for choosing Apex Heating & Air and hang up.)* |

---

### **Post-Call Verification Checklist:**
Once you end the test call in the Vapi dashboard, check the call logs/JSON output to verify Vapi successfully extracted:
- [ ] `hvac_status`: "complete"
- [ ] `hvac_urgency_level`: "emergency"
- [ ] `hvac_system_type`: "Central AC"
- [ ] `hvac_unit_quantity`: 1
- [ ] `hvac_issue_details`: (Should mention blowing warm air/buzzing noise)
- [ ] `hvac_preferred_time_slot`: "tomorrow morning"
