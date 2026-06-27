# UI/UX Guidelines Index

These guidelines define the UX quality standards for this project. They apply to all frontend development and Senior Dev code reviews.

## Quick Reference: The Non-Negotiables

These rules apply to EVERY task, regardless of type:

1. **No happy-path-only components.** Every interactive element must have a loading state, empty state, and error state. 
2. **No silent failures.** Every button click must produce visible feedback. 
3. **No backend dumps.** Never expose raw errors to the user. 
4. **No global crashes.** One failing component must not take down the whole page.
