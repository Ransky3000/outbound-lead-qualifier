# MCP Server Setup for Claude Code

This project uses MCP (Model Context Protocol) servers for direct integration with n8n, Vapi, Airtable, and GitHub.

## Configuration

All MCP servers are configured in `.mcp.json` (project root). This file is **gitignored** — it contains API keys.

Claude Code reads `.mcp.json` automatically when you open the project. No manual setup needed.

## Available Servers

### n8n (Workflow Automation)
- **Connects to:** `https://n8n-lovp.srv1780014.hstgr.cloud`
- **Auth:** MCP API JWT token
- **Package:** `mcp-remote`
- **Use for:** Searching, creating, updating, executing workflows. Managing credentials and nodes.

### n8n-docs (Documentation Search)
- **Connects to:** `https://n8n.mcp.kapa.ai/`
- **Auth:** None required
- **Package:** `mcp-remote`
- **Use for:** Searching n8n documentation, finding node usage patterns.

### Vapi (Voice AI)
- **Auth:** Vapi API token
- **Package:** `@vapi-ai/mcp-server`
- **Use for:** Managing assistants, phone numbers, tools. Making/scheduling calls.

### Airtable (CRM)
- **Auth:** Airtable Personal Access Token (PAT)
- **Package:** `airtable-mcp-server`
- **Use for:** CRUD on Contacts and Service Requests tables. Schema management.
- **Base ID:** `appTgp7XEjZ9A9nE3` (Apex HVAC CRM)

### GitHub (Version Control)
- **Auth:** GitHub Personal Access Token
- **Package:** `@modelcontextprotocol/server-github`
- **Use for:** Creating PRs, pushing files, managing issues, searching code.
- **Repo:** `Ransky3000/outbound-lead-qualifier`

## If `.mcp.json` Is Missing

Recreate it by copying the template from `.env.example` keys into the format documented in the [Claude Code MCP docs](https://docs.anthropic.com/en/docs/claude-code/mcp).

## Verify MCP Connection

```bash
claude mcp list
```

All 5 servers (github, n8n, n8n-docs, vapi, airtable) should show as connected.
