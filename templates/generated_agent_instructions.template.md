# Generated Agent Instructions Template

You are working in this repository with the AI Token Saver workflow.

This file must be customized during setup. Do not leave it generic.

## Repository-Specific Sources Of Truth

Use:

```text
--ai-token-saver/project_brain.md
--ai-token-saver/project_systems.json
--ai-token-saver/context_routes.json
--ai-token-saver/known_patterns.md
--ai-token-saver/known_pitfalls.md
--ai-token-saver/editing_rules.md
```

## Core Rule

For repository tasks, do not start with broad repository search.

First convert the user's casual request into a technical task string using the generated project brain and context routes.

Then run the generated preflight context script.

## Prompt Interpretation

The user may speak casually.

When the user says "like X", treat X as an existing repository pattern to inspect and reuse.

The user should not need to say "use the context script."

## Required Workflow

1. Convert the user prompt into a technical task string.
2. Run context preflight.
3. Read generated map and manifest.
4. Follow route recommendations.
5. Read focused task context.
6. Inspect exact source files only when needed.
7. Make the smallest complete edit.
8. Validate.
9. Run token efficiency report.
10. Update project memory if a reusable lesson was learned.

## Reporting

Always report full relative file paths.

At the end, summarize:

- changed files
- validation result
- token efficiency estimate
- any memory/pitfall updates
