# Vapi Agent Configurations

This directory contains the Vapi system prompts, configurations, and structured output definitions for the outbound lead qualification agents.

## Directory Structure

*   **[`elliot/`](./elliot/)**: Contains the original B2B SaaS lead qualification agent (Elliot) template based on the Nate Herk system.
*   **[`layla/`](./layla/)**: Contains the adapted, local B2C HVAC dispatcher and receptionist agent (Layla) for Apex Heating & Air.

## Sub-files for Each Agent

*   `system-prompt.md`: The system prompt defining the persona, style, and dialog guidelines.
*   `structured-outputs.md`: The custom fields extracted by Vapi at the end of each call.
*   `assistant-config.md`: The settings, provider details, and voice configurations.
