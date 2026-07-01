# 📞 HVAC Call Test Script: Apex HVAC - Layla

Use this script table when Layla calls you. Following these answers ensures all required CRM data fields are qualified and logged correctly in the Google Sheet.

| Layla (AI Agent) | Ranian (Your Answer) |
| :--- | :--- |
| *"Hi Ranian, this is Layla calling from Apex Heating & Air. I saw you just requested service online for Repair at 123 Main St, Phoenix. Is this still a good time to chat?"* | **"Yes, this is Ranian. Now is a great time to chat!"** |
| *"Great! Could you tell me a little bit about what your system is doing, and if it's completely down?"* | **"Yes, my air conditioner is completely down. It is blowing warm air instead of cold, and there is a loud clicking noise coming from the outside unit. It is extremely hot today, so this is an emergency for us."** <br><br>*🔑 Fields: `hvac_issue_details` & `hvac_urgency_level` (emergency)* |
| *"Okay, I've noted that down. Just to confirm, are we looking to repair your existing unit, or are you thinking about getting a new system installed?"* | **"We just need to repair our existing unit."** <br><br>*🔑 Field: `hvac_installation_scope` (repair)* |
| *"Got it, a repair. And is 123 Main St in Phoenix the correct address for the service?"* | **"Yes, that is the correct address."** |
| *"Perfect. I have availability tomorrow. Would tomorrow morning or tomorrow afternoon work better for you?"* | **"Tomorrow morning works best for us."** <br><br>*🔑 Field: `hvac_preferred_time_slot` (tomorrow morning)* |
| *"Great, I have reserved a tomorrow morning slot for you in our queue. Our dispatch team will send a text message in just a few minutes with the exact time... Is there anything else I can help you with?"* | **"No, that's all. Thank you so much, Layla! Goodbye!"** |

---

### **What happens next?**
After hanging up:
1. Vapi extracts the structured output fields.
2. n8n fetches the call analysis and appends the row to your Google Sheet.
3. The row will show `Call Status` as **"booked"** and populate all other HVAC qualification columns.
