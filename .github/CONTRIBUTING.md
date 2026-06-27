# Contributing Guidelines

This project uses a multi-agent AI development workflow. If you are an agent reading this, adhere strictly to these rules.

## Git Workflow (Simplified GitFlow)
1. **Branching**: All work must be done on a feature branch branched off `dev`.
   - `git checkout -b feature/<agent-role>-<task-name> dev`
2. **Committing**: Use Conventional Commits.
3. **No Direct Pushes**: Never push directly to `main` or `dev`.
4. **Pull Requests / Merging**: The Planner handles all merges to `dev` and `main` after review.

## Commit Conventions
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

## Communication
- Status files in `ransky_agents/status/` must be **OVERWRITTEN**, not appended.
- Cross-agent issues must be logged in `ransky_agents/issues/ISSUES.md`.
- Shared learnings must be added to `ransky_agents/knowledge/KNOWLEDGE_BASE.md`.
