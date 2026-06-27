# START HERE

**Project:** Outbound Lead Qualifier
**Stack:** n8n (self-hosted on Hostinger) + Vapi + Google Sheets + Twilio

---

## 1. Identify Your Role

You are one of two agents. The Director (user) will tell you which role you are.

| Role | Conversation Name | Instruction File |
|------|------------------|------------------|
| **Senior Dev** | "Senior Dev" / "Planner" | `ransky_agents/roles/senior-dev.md` |
| **Backend** | "Backend" / "Builder" | `ransky_agents/roles/backend.md` |

**If unsure:** Ask the Director which role you are. Do not guess.

---

## 2. Boot Sequence (Every Session)

Read these files in order. Do NOT skip any. Do NOT write code until step 5.

1. **This file** — you're reading it now.
2. **Your role file** — `ransky_agents/roles/<your-role>.md`
3. **Architecture** — `ransky_agents/project/architecture.md` (tech stack, workflow map, conventions)
4. **Sprint Log** — `ransky_agents/project/sprint-log.md` (current tasks, project state)
5. **API Contracts** — `ransky_agents/project/api-contracts.md` (API endpoints, schemas — never guess these)
6. **Issues** — `ransky_agents/project/issues.md` (bugs assigned to you)
7. **Report to Director:** State your role, summarize your assignment, confirm you are Standing By.
8. **⛔ STOP.** Wait for the Senior Dev's go signal (relayed by the Director).

---

## 3. Chain of Command

```
👤 Director (User) — Product owner. Communicates with all agents.
  └── Senior Dev — Plans, researches APIs, designs prompts, reviews, deploys.
        └── Backend — Builds n8n workflows, configures Vapi, writes code nodes, manages integrations.
```

**Rules:**
- No agent executes without the Senior Dev's go signal.
- No agent self-assigns work. All tasks come from `ransky_agents/project/sprint-log.md`.
- No agent guesses API schemas. Read `ransky_agents/project/api-contracts.md`.

---

## 4. Communication Protocol

Agents cannot directly talk to each other. The Director relays messages.

**Senior Dev → Backend:** Senior Dev writes dispatch prompts in the sprint log or gives them directly to the Director. The Director pastes them into the target agent's conversation.

**Backend → Senior Dev:** Agent updates `ransky_agents/project/sprint-log.md` and tells the Director: "I am Idle. Awaiting QA." The Director relays this to the Senior Dev.

---

## 5. Status Codes

| Code | Meaning | When |
|------|---------|------|
| `IDLE` | No active task | Awaiting assignment |
| `STANDBY` | Task received, read docs | Awaiting go signal |
| `ACTIVE` | Executing authorized task | After go signal |
| `BLOCKED` | Waiting on dependency/bug | Log in issues.md, report immediately |

---

## 6. File Map (Quick Reference)

```
Outbound Lead Qualifier/
├── ransky_agents/
│   ├── START_HERE.md          ← You are here
│   ├── roles/
│   │   ├── senior-dev.md
│   │   └── backend.md
│   ├── project/
│   │   ├── architecture.md    ← Tech stack, workflow architecture
│   │   ├── api-contracts.md   ← Vapi/Google Sheets API schemas
│   │   ├── sprint-log.md      ← Current sprint, task assignments
│   │   └── issues.md          ← Active bugs
│   └── knowledge/
│       ├── communication-vibes.md
│       └── ui-ux-guidelines/
├── workflows/                 ← n8n workflow JSON exports (versioned)
├── vapi/                      ← Vapi assistant config, prompts, structured outputs
├── prompts/                   ← System prompt version history
├── docs/                      ← Setup guide, demo script
├── reference/                 ← Nate Herk PDF, research materials, original template
├── assets/                    ← Screenshots, demo video, portfolio media
├── .agents/                   ← Agent skills config
└── .github/
```
